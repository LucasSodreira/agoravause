from datetime import datetime


class Usuario:

    def __init__(self, id, nome, login, senha):
        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__senha = senha


    '''Getters e Setters'''

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, novo_login):
        self.__login = novo_login
    
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    

    '''Métodos da Classe'''

    def __str__(self) -> str:
        return f'{self.nome}'
    

class Postagem:


    def __init__(self, id, titulo, texto, usuario):
        self.__id = id
        self.__titulo = titulo
        self.__texto = texto
        self.__data_publicacao = datetime.today()
        self.__usuario = usuario
        
    
    '''Getters e Setters'''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, value):
        self.__texto = value

    @property
    def data_publicacao(self):
        return self.__data_publicacao

    @data_publicacao.setter
    def data_publicacao(self, value):
        self.__data_publicacao = value
    

    '''Métodos da Classe'''

    def __str__(self) -> str:
        return f'\033[1;31;0m{self.titulo}\033[m\n\n\033[1;30;40m{self.texto}\033[0;0m\n\nPublicada por {self.__usuario}\n{self.data_publicacao}\n'

class Blog():


    def __init__(self) -> None:
        self.__postagens = []
        self.__publicacoes = []
        self.__autenticado = False


    '''Getters e Setters'''

    @property
    def postagens(self):
        return self.__postagens

    @postagens.setter
    def postagens(self, nova_postagem):
        self.__postagens.append(nova_postagem)

    @property
    def publicacoes(self):
        return self.__publicacoes

    @publicacoes.setter
    def publicacoes(self, nova_publicacao):
        self.__publicacoes.append(nova_publicacao)

    @property
    def autenticado(self):
        return self.__autenticado
    
    @autenticado.setter
    def autenticado(self, nova_autenticacao):
        if nova_autenticacao != False or True:
            raise Exception('Esse tipo de autenticação não existe.')
        else:
            self.__autenticado = nova_autenticacao


    '''Métodos da Classe'''

    def autenticar(self, usuario):
        if self.__autenticado == True:
            raise Exception('Você já autenticado.')
        else:
            self.__autenticado = True
    

    def logout(self):
        if self.__autenticado == False:
            raise Exception('Você já deslogado.')
        else:
            self.__autenticado = False


    def adicionar_postagem(self, postagem):
        if self.__autenticado == True:
            self.postagens.append(postagem)
        else:
            raise Exception('Você não está autenticado')


    def publicar_postagem(self, postagem):
        if self.__autenticado == True:
            self.publicacoes.append(postagem)
        else:
            raise Exception('Você só pode fazer uma publicação com uma conta autenticada.')


    def listar_postagem_publicadas(self):
        print(f'({len(self.publicacoes)}) Publicadas:')
        for x in range(len(self.publicacoes)):
            print(self.postagens[x])


    def listar_todas_postagens(self):
        print(f'({len(self.postagens)}) Postadas:')
        for x in range(len(self.postagens)):
            print(self.postagens[x])


    def apagar_postagem(self, id_postagem):
        if self.__autenticado == True:
            for i in range(len(self.postagens)):
                if id_postagem == self.postagens[i].id:
                    del self.postagens[i]
                    break
        else:
            raise Exception('Para excluir uma postagem deve estar autenticado.')