"""Verifica a publicação com repositórios Git temporários, sem rede nem GitHub."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/publicar_apostila.sh'


class PublicacaoApostila(unittest.TestCase):
    def setUp(self):
        self.temporario = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporario.cleanup)
        self.raiz = Path(self.temporario.name)
        self.origem = self.raiz / 'origin.git'
        self.trabalho = self.raiz / 'trabalho'
        self.trabalho.mkdir()
        self.git('init', '--bare', str(self.origem), cwd=self.raiz)
        self.git('init', '-b', 'main')
        self.identidade(self.trabalho)
        (self.trabalho / 'VERSION').write_text('1.1.0\n')
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf anterior')
        self.commit('fontes iniciais')
        self.git('remote', 'add', 'origin', str(self.origem))
        self.git('push', 'origin', 'main')
        self.source_sha = self.git('rev-parse', 'HEAD')

    def git(self, *argumentos, cwd=None, check=True):
        resultado = subprocess.run(
            ['git', *argumentos], cwd=cwd or self.trabalho,
            check=check, capture_output=True, text=True,
        )
        return resultado.stdout.strip()

    def identidade(self, caminho):
        for chave, valor in [('user.name', 'Teste'), ('user.email', 'teste@example.invalid'),
                              ('commit.gpgsign', 'false'), ('tag.gpgsign', 'false')]:
            self.git('config', chave, valor, cwd=caminho)

    def commit(self, mensagem):
        self.git('add', '.')
        self.git('commit', '-m', mensagem)

    def publicar(self, source_sha=None, check=True):
        return subprocess.run(
            ['bash', str(SCRIPT)], cwd=self.trabalho,
            env={**os.environ, 'SOURCE_SHA': source_sha or self.source_sha},
            capture_output=True, text=True, check=check,
        )

    def remoto(self, referencia):
        return self.git('--git-dir', str(self.origem), 'rev-parse', referencia)

    def tags_remotas(self):
        return self.git('--git-dir', str(self.origem), 'tag', '--list')

    def test_pdf_e_tag_apontam_para_a_mesma_edicao(self):
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf novo')
        self.publicar()
        self.assertEqual(self.remoto('main'), self.remoto('v1.1.0^{commit}'))
        self.assertEqual(self.git('--git-dir', str(self.origem), 'cat-file', '-t', 'v1.1.0'), 'tag')
        self.assertEqual(self.git('--git-dir', str(self.origem), 'show', 'v1.1.0:apostila_jamovi.pdf'), 'pdf novo')

    def test_pdf_identico_tambem_recebe_tag(self):
        self.publicar()
        self.assertEqual(self.remoto('main'), self.source_sha)
        self.assertEqual(self.remoto('v1.1.0^{commit}'), self.source_sha)

    def test_tag_existente_nao_e_movida(self):
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf da edicao')
        self.publicar()
        tag_publicada = self.remoto('v1.1.0')
        (self.trabalho / 'nota.txt').write_text('outra revisao da main')
        self.commit('revisao posterior')
        self.git('push', 'origin', 'main')
        self.source_sha = self.git('rev-parse', 'HEAD')
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf posterior')
        self.publicar()
        self.assertEqual(self.remoto('v1.1.0'), tag_publicada)
        self.assertNotEqual(self.remoto('main'), self.remoto('v1.1.0^{commit}'))
        self.assertEqual(self.git('--git-dir', str(self.origem), 'show', 'main:apostila_jamovi.pdf'), 'pdf posterior')

    def test_execucao_antiga_nao_publica(self):
        (self.trabalho / 'nota.txt').write_text('novos fontes')
        self.commit('novos fontes')
        self.git('push', 'origin', 'main')
        atual = self.remoto('main')
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf antigo recompilado')
        self.publicar(source_sha=self.source_sha)
        self.assertEqual(self.remoto('main'), atual)
        self.assertEqual(self.tags_remotas(), '')

    def test_versao_invalida_nao_publica(self):
        (self.trabalho / 'VERSION').write_text('1.1.0/versao-invalida\n')
        self.commit('versao invalida')
        self.git('push', 'origin', 'main')
        self.source_sha = self.git('rev-parse', 'HEAD')
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf novo')
        resultado = self.publicar(check=False)
        self.assertNotEqual(resultado.returncode, 0)
        self.assertEqual(self.remoto('main'), self.source_sha)
        self.assertEqual(self.tags_remotas(), '')

    def test_avanco_remoto_rejeita_pdf_e_tag_juntos(self):
        outro = self.raiz / 'outro'
        self.git('clone', '--branch', 'main', str(self.origem), str(outro), cwd=self.raiz)
        self.identidade(outro)
        (outro / 'nota.txt').write_text('alteracao concorrente')
        self.git('add', '.', cwd=outro)
        self.git('commit', '-m', 'avanco remoto', cwd=outro)
        self.git('push', 'origin', 'main', cwd=outro)
        atual = self.remoto('main')
        (self.trabalho / 'apostila_jamovi.pdf').write_bytes(b'pdf que perdeu a corrida')
        resultado = self.publicar(check=False)
        self.assertNotEqual(resultado.returncode, 0)
        self.assertEqual(self.remoto('main'), atual)
        self.assertEqual(self.tags_remotas(), '')


if __name__ == '__main__':
    unittest.main()
