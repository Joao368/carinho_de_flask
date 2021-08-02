class CarrinhoDeCompras():
    def __init__(self, nome_produto, preco, quantidade):
        self.produtos = {
            nome_produto: {
                'preco': preco,
                'quantidade': quantidade
            }

        }


    def get_produtos(self):
        return self.produtos

    def incluir_item(self, nome_novo_produto, preco, quantidade):
       # try:
        if nome_novo_produto in self.produtos:
            preco_registrado = self.produtos[nome_novo_produto]['preco']
            if preco is preco_registrado:
                self.produtos[nome_novo_produto]['quantidade'] += quantidade
            else:
                print("ALERTA: Produto ja registrado nao pode ter preços diferentes")

        else:
            self.produtos[nome_novo_produto] = {
                    'preco': preco,
                    'quantidade': quantidade
                }

    def get_valor_total_da_compra(self):
        total_da_compra = 0
        for key in self.produtos:
           total_da_compra += self.produtos[key]['preco'] * self.produtos[key]['quantidade']
        return total_da_compra

    def get_total_de_itens(self):
        total_de_itens = 0
        for key in self.produtos:
            total_de_itens += self.produtos[key]['quantidade']
        return total_de_itens
    
    def atualizar_preço(self,nome_produto, novo_preço):
       self.produtos[nome_produto] ['preco'] = novo_preço
    

    def atualizar_quantidade(self, nome_produto, nova_quantidade):
        if nova_quantidade <= 0:
            del(self.produtos[nome_produto])
        else:
            self.produtos[nome_produto]['quantidade'] = nova_quantidade
                    

    def excluir(self, nome_produto):
        del(self.produtos[nome_produto])


