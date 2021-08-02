from carrinho_de_flask.loja import CarrinhoDeCompras
import unittest
class teste_carrinho(unittest.TestCase):
    def setUp(self):
        self.carrinho = CarrinhoDeCompras('geladeira', 1500, 2)
        self.carrinho.incluir_item('micro-ondas', 300, 3)
# A classe setup serve para definir os itens que estaram
# dentro do carrinho de compras
    def test_busca_produto(self):
        dict_de_produtos = self.carrinho.get_produtos()
        self.assertIn('geladeira', dict_de_produtos)

    def test_busca_preço_de_produto(self):
        dict_de_produtos = self.carrinho.get_produtos()
        preco = dict_de_produtos['geladeira']['preco']
        self.assertEqual(1500, preco)

    def test_incluir_novo_item(self):
        dict_de_produtos = self.carrinho.get_produtos()
        self.assertIn('micro-ondas', dict_de_produtos)

    def test_verifica_total_da_compra(self):
        valor_total = self.carrinho.get_valor_total_da_compra()
        self.assertEqual(3900, valor_total)

    def test_verifica_total_de_itens(self):
        total_de_itens = self  .carrinho.get_total_de_itens()
        self.assertEqual(5, total_de_itens)

    def test_verifica_total_de_itens_com_inclusao_de_novos_itens(self):
        self.carrinho.incluir_item('micro-ondas', 300, 10)
        total_de_itens = self.carrinho.get_total_de_itens()
        self.assertEqual(15, total_de_itens)

    def test_atualizaçao_preço(self):
        self.carrinho.atualizar_preço('micro-ondas',400)
        dict_de_produtos = self.carrinho.get_produtos()
        preço = dict_de_produtos['micro-ondas']['preco']
        self.assertEqual(400, preço)

    def test_atualizaçao_quantide(self): 
        self.carrinho.atualizar_quantidade('micro-ondas', 4)
        dict_de_produtos = self.carrinho.get_produtos()
        quantidade = dict_de_produtos['micro-ondas']['quantidade']
        self.assertEqual(4,quantidade)

    def test_atualizaçao_delete_apartir_de_quantidade(self): 
        self.carrinho.atualizar_quantidade('micro-ondas', 0)
        dict_de_produtos = self.carrinho.get_produtos()
        self.assertNotIn('micro-ondas',dict_de_produtos)

    def test_atualizaçao_delete_apartir_de_quantidade_negativo(self): 
        self.carrinho.atualizar_quantidade('micro-ondas', -1)
        dict_de_produtos = self.carrinho.get_produtos()
        self.assertNotIn('micro-ondas',dict_de_produtos)

    def test_excluindo_itens(self):
        self.carrinho.excluir('geladeira')
        dict_de_produtos = self.carrinho.get_produtos()
        self.assertNotIn('geladeira', dict_de_produtos)


