from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime


class InterfaceReserva(ABC):

    @abstractmethod
    def CriaReserva(self):
        pass
    
    @abstractmethod
    def CancelarReserva(self):
        pass

class Passageiro(InterfaceReserva):

    def CriaReserva(self, ID, Passageiro, *args, **kwargs):
        return Operadores.CriaReserva(ID, Passageiro)

    def PagarPassagem(self, Voo, reserva):
        # print(len(Voo.reservas))
        if len(Voo.reservas) <= Voo.assentos:
            Voo.reservas.append(reserva)
        else:
            raise ValueError('Voo Lotado.')

    def CancelarReserva(self, operador, voo):
        operador.CancelarReserva(voo)
        
class Operadores(InterfaceReserva):

    def CriaReserva(ID, Passageiro, *args, **kwargs):
        print("Reserva Criada!")
        return Reserva(ID, Passageiro)

    def CancelarReserva(self, voo, id, *args, **kwargs):
        print(f'Existem {len(voo.reservas)} reservas')
        del voo.reservas[id - id]
        print(f'Assentos livres {voo.AcentosLivres()}')
        print('Reserva deletada!')

        
class Reserva():

    def __init__(self, ID:int, Passageiro):
        self.__ID = ID
        self.__Passageiro = Passageiro

    ######## Getters e Setters ########
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, new_ID):
        self.__ID = new_ID
        
    @property
    def passageiro(self):
        return self.__Passageiro
    
    @passageiro.setter
    def passageiro(self, novo_Passageiro):
        self.__Passageiro = novo_Passageiro
        
    def __str__(self) -> str:
        return f'Reserva concluida {self.__Passageiro}!'
        
class Voo():

    def __init__(self, codigo, data, hora, partida, destino, aeroporto, assentos, internacional:bool):
        
        self.__data = data
        self.__hora = hora
        self.__partida = partida
        self.__destino = destino
        self.__codigo = codigo
        self.__aeroporto = aeroporto
        self.__voo_internacional = internacional
        self.__reservas = []
        self.__assentos = assentos
    
    ######## Getters e Setters ########

    @property
    def partida(self):
        return self.__partida
    
    @partida.setter
    def partida(self, nova_partida):
        self.__partida = nova_partida

    @property
    def assentos(self):
        return self.__assentos

    @assentos.setter
    def assentos(self, nova_capacidade):
        self.__assentos = nova_capacidade

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, nova_hora):
        self.__hora = nova_hora
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, novo_destino):
        self.__destino = novo_destino
    
    @property
    def aeroporto(self):
        return self.__aeroporto
    
    @aeroporto.setter
    def aeroporto(self, novo_aeroporto):
        self.__aeroporto = novo_aeroporto

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data: datetime):
        self.__data = nova_data
    
    @property
    def reservas(self):
        return self.__reservas
    
    @reservas.setter
    def reservas(self, nova_reserva):
        self.__reservas = nova_reserva

    @property
    def voo_internacional(self):
        return self.__voo_internacional
    
    @voo_internacional.setter
    def voo_internacional(self, mudar_voo: bool):
        self.__voo_internacional = mudar_voo

    def __str__(self) -> str:
        return f'Codigo de Voo {self.__codigo}, com destino à {self.__destino}'

    ######### Métodos #########

    def AcentosLivres(self):
        AcentosLivres = self.__assentos - len(self.__reservas) 
        print(f'Tem {AcentosLivres} Acentos Livres!') 
        return f'{AcentosLivres}'

class Aeroporto():

    def __init__(self, cidade, capacidade, nome):
        self.__cidade = cidade
        self.__capacidade = capacidade
        self.__nome = nome
    
    ######## Getters e Setters ########

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        self.__capacidade = nova_cidade
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.__capacidade = nova_capacidade
       
    @property    
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def __str__(self) -> str:
        return self.__nome
