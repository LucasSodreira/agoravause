class Produto():

    def __init__(self, codigo: int, valor: float, descricao: str) -> None:
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao
    

    '''Getters e Setters'''

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor
    

    '''Métodos da Classe'''

    def __str__(self):
        return self.descricao


class Pedido():


    class ItemPedido():


        def __init__(self, quantidade:int, produto: Produto) -> None:
            self.__quantidade = quantidade
            self.produto = produto
        

        '''Getters e Setters'''

        @property
        def quantidade(self):
            return self.__quantidade
        
        @quantidade.setter
        def quantidade(self, nova_quantidade):
            self.__quantidade += nova_quantidade

    
    def __init__(self) -> None:
        self.__valor_total = 0
        self.__pedidos = []

    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, novo_valor):
        self.__valor_total = novo_valor
    
    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, novo_pedido):
        self.__pedidos.append(novo_pedido)


    '''Métodos da Classe'''

    def adicionar_item(self, item: ItemPedido):
        valor_do_pedido = item.produto.valor * item.quantidade
        self.pedidos.append(item.produto.valor)

    
    def obter_total(self):
        valor_total = 0
        for valor in range(len(self.pedidos)):
            valor_total+=self.pedidos[valor]
        print(f'Valor total a pagar: R${valor_total:.2f}')
