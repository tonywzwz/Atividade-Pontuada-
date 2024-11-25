from models.Medico import Medico
from models.Endereco import Endereco
from models.Engenheiro import Engenheiro
from os import system

def limpar():
    system("cls||clear")

def medico_valido():
    limpar()
    endereco_medico = Endereco("Rua 321", "143 - E", "1º Andar", "40117006", "Salvador")
    medico = Medico("Douglas", "71984278202", "dg@gmail.com", endereco_medico, "123_CRM")
    print(medico)

def engenheiro_valido():
    limpar()
    endereco_engenheiro = Endereco("Rua 123", "123 - E", "2º Andar", "40517092", "Salvador")
    engenheiro = Engenheiro("Átila", "71940028922", "Atila123@gmail.com", endereco_engenheiro, "123_CREA")
    print(engenheiro)



#Instâncias para Testes:

#engenheiro_valido()
#medico_valido()