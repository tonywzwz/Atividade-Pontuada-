import sys
sys.path.append('/workspaces/Atividade-Pontuada-/project/')
from models.Endereco import Endereco
from models.Funcionario import Funcionario
from models.Medico import Medico
import pytest

@pytest.fixture
def medico_valido():
    medico = Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
    return medico

def test_nome_medico_valido(medico_valido):
    assert medico_valido.nome == "Douglas"

def test_numero_medico_valido(medico_valido):
    assert medico_valido.telefone == "71988322399"

def test_email_medico_valido(medico_valido):
    assert medico_valido.email == "douglas@gmail.com"

def test_logradouro_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua beila"

def test_numero_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.numero == "123"

def test_complemento_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.complemento == "1º Andar"

def test_cep_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.cep == "40711788"

def test_cidade_endereco_medico_valido(medico_valido):
    assert medico_valido.endereco.cidade == "Salvador"

def test_crm_medico_valido(medico_valido):
    assert medico_valido.crm == "123_CRM"

def test_cep_valor_invalido(medico_valido):
    with pytest.raises(ValueError, match = "O CEP Digitado é Inválido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "407111788", "Salvador"),
                                    "123_CRM")

def test_cep_vazio(medico_valido):
    with pytest.raises(ValueError, match = "O CEP Digitado é Inválido."):
         Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", " ", "Salvador"),
                                    "123_CRM")
         
def test_cep_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um CEP Válido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", 40711788, "Salvador"),
                                    "123_CRM")

def test_logradouro_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um Logradouro Válido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco(123, "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
        
def test_logradouro_vazio(medico_valido):
    with pytest.raises(ValueError, match = "O Logradouro é Inválido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco(" ", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")

def test_numero_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match= "Digite um Número Válido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", 123, "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")

def test_numero_vazio(medico_valido):
    with pytest.raises(ValueError, match = "O Número é Inválido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", " ", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")

def test_complemento_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um Complemento Válido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", 123, "40711788", "Salvador"),
                                    "123_CRM")

def test_complemento_vazio(medico_valido):
    with pytest.raises(ValueError, match = "O Complemento é Inválido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", " ", "40711788", "Salvador"),
                                    "123_CRM")

def test_cidade_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite uma Cidade Válida."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", 123),
                                    "123_CRM")

def test_cidade_vazio(medico_valido):
    with pytest.raises(ValueError, match = "A Cidade é Inválida."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", " "),
                                    "123_CRM")

def test_nome_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = ""):
        Medico(123,
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
        
def test_nome_vazio(medico_valido):
    with pytest.raises(ValueError, match="O Espaço do nome não pode ficar Vazio. Digite o nome do Usuário."):
        Medico(" ",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
        
def test_telefone_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um telefone Válido."):
        Medico("Douglas",
                                    123,
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
def test_telefone_invalido(medico_valido):
    with pytest.raises(ValueError, match = "Número de Telefone Inválido."): 
        Medico("Douglas",
                                    " ",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")

def test_email_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um Email Válido."):
        Medico("Douglas",
                                    "71988322399",
                                    123,
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")

def test_email_vazio(medico_valido):
    with pytest.raises(ValueError, match = "O Espaço de email não pode estar Vazio."):
        Medico("Douglas",
                                    "71988322399",
                                    " ",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "123_CRM")
def test_crm_tipo_invalido(medico_valido):
    with pytest.raises(TypeError, match = "Digite um CRM válido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    123)
def test_crm_vazio(medico_valido):
    with pytest.raises(ValueError, match = "CRM Inválido."):
        Medico("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    " ")