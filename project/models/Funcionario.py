import sys
sys.path.append('/workspaces/Atividade-Pontuada-/project/')
from models.Endereco import Endereco
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome:str, telefone:str, email:str, endereco:Endereco) -> None:
        
        self.nome = self._verificar_nome_valido(nome)
        self.telefone = self._verificar_telefone_valido(telefone)
        self.email = self._verificar_email_valido(email)
        self.endereco = endereco 

    def _verificar_nome_valido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("Nome Inválido, Digite um Nome Válido.")
        if not nome.strip():
            raise ValueError("O Espaço do nome não pode ficar Vazio. Digite o nome do Usuário.")
        return nome
    
    def _verificar_telefone_valido(self, telefone):
        if not isinstance(telefone, str):
            raise TypeError("Digite um telefone Válido.")
        if len(telefone)!=11 or not telefone.strip():
            raise ValueError("Número de Telefone Inválido.")
        return telefone
    
    def _verificar_email_valido(self, email):
        if not isinstance(email, str):
            raise TypeError("Digite um Email Válido.")
        if not email.strip():
            raise ValueError("O Espaço de email não pode estar Vazio.")
        return email
    
    @abstractmethod
    def salario_final() -> float:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereco :{self.endereco}" 
            )
    
# endereco = Endereco("123", "asd", "asda", "40711600", "asdas")
# funcionario = Funcionario("Douglas", "71988426379", "dougxandy@gmail.com", endereco)
# print(funcionario)