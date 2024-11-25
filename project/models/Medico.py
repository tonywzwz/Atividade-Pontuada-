import sys
sys.path.append('/workspaces/Atividade-Pontuada-/project/')
from models.Endereco import Endereco
from models.Funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = self._verificar_crm_valido(crm)

    def _verificar_crm_valido(self, crm):
        if not isinstance(crm, str):
            raise TypeError("Digite um CRM válido.")
        if not crm.strip():
            raise ValueError("CRM Inválido.")
        return crm
    
    def salario_final(self) -> float:
        return 7800.00
    
    def __str__(self) -> str:
        return super().__str__() + f"\ncrm: {self.crm}" + f"\nSalário Final: {self.salario_final()}"

# endereco = Endereco("123", "asd", "asda", "40711600", "asdas")
# medico = Medico("Douglas", "71988426379", "dougxandy@gmail.com", endereco, "123")
# print(medico)    
