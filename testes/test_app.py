
import unittest
from API import app
import json


class BasicTestCase(unittest.TestCase):
  def setUp(self):
      self.app = app.create_app()


  def test_adiciona(self):
    resposta={
      "geladeira": {"preco": 1500,"quantidade": 1},
      "ventilador": {"preco": 200,"quantidade": 3}}
    with self.app.test_client() as cliente:
      cliente.post("/adicionaproduto", json={"produto": "ventilador", "preco":200,"quantidade":3})
      req_resposta = cliente.get("/carinho")
      dados= json.loads(req_resposta.data)
      self.assertEqual(resposta, dados)

  def test_total(self):
    resolucao = {"valortotal": 2100 }
    with self.app.test_client() as cliente:
      req_resposta = cliente.get("/total_da compra")
      total = json.loads(req_resposta.data)
      self.assertEqual(total, resolucao)

  def test_total_itens(self):
    resp = {'total_de_itens': 4}
    with self.app.test_client() as cliente:
      req_resposta = cliente.get("/total_de_itens")
      itens = json.loads(req_resposta.data)
      self.assertEqual(itens, resp)

  def test_atualiza_preco(self):
    resposta = {
      "geladeira": {"preco": 1500, "quantidade": 1},
      "ventilador": {"preco": 300, "quantidade": 3}}

    with self.app.test_client() as cliente:
      cliente.post("/atualizar_preco", json={"produto": "ventilador", "preco":300})
      req_resposta = cliente.get("/carinho")
      dados= json.loads(req_resposta.data)
      self.assertEqual(resposta, dados)