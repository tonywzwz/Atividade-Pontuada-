import sys
sys.path.append('/workspaces/Atividade/project/')
from models.Endereco import Endereco
from models.Funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = self._verificar_crea_valido(crea)
    
    def _verificar_crea_valido(self, crea):
        if not isinstance(crea, str):
            raise TypeError("Digite um Crea válido.")
        if not crea.strip():
            raise ValueError("Crea Inválido.")
        return crea
    
    def salario_final(self) -> float:
        return 6500.00
    
    def __str__(self) -> str:
        return super().__str__() + f"\nCrea: {self.crea}" + f"\nSalário Final: {self.salario_final()}"

# endereco = Endereco("123", "asd", "asda", "40711600", "asdas")
# Engenheiro = Engenheiro("Douglas", "71988426379", "dougxandy@gmail.com", endereco, "123")
# print(Engenheiro)    
