from datetime import datetime

from aeroporto import *

# print(f'----------------- Crie o aeroporto -----------------')
cidade = 'Sousa'
capacidade_voos = 10
nome = 'Aeroporto de Sousa'
aeroporto = Aeroporto(cidade, capacidade_voos, nome)

# print(f'----------------------------------------------------')

codigo = '01'
partida = 'Sousa'
internacional = False
destino = 'RJ'
assentos = 50
Hora = datetime.now().strftime('%H:%M:%S')
Data = datetime.now().strftime('%Y/%m/%d')


voo = Voo(codigo, partida, Data, Hora, destino, aeroporto, assentos, internacional)
    
passageiro = Passageiro()
operador = Operadores()

menu = 0 
while menu == 0:
    menu = int(input(f'O deseja fazer agora?\n[1] Fazer uma reserva\n[2] Cancelar reserva\n'))
        
    while menu == 1:

        reserva = passageiro.CriaReserva(len(voo.reservas), passageiro)
        print(f'Você fez uma reserva, restam {voo.AcentosLivres()} assentos livres.')

        menu = int(input('Deseja pagar? \n[1] Sim\n[2] Não\n'))
        
        if menu == 1:
            passageiro.PagarPassagem(voo, reserva)
            
        if menu == 2:
            menu = 0 
                
                
    while menu == 2:
        
        operador.CancelarReserva(voo, 1)
            
        menu = int(input('Deseja cancelar outra?\n[1] Sim\n[2] Não\n'))
        
        if menu == 1:
            pass
        
        if menu == 2:
            menu = 0 