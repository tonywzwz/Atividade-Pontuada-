import sys
sys.path.append('/workspaces/Atividade-Pontuada-/project/')
from models.Endereco import Endereco
from models.Funcionario import Funcionario
from models.Engenheiro import Engenheiro
import pytest

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")
    return engenheiro

def test_nome_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Douglas"

def test_numero_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "71988322399"

def test_email_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.email == "douglas@gmail.com"

def test_logradouro_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Rua beila"

def test_numero_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "123"

def test_complemento_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "1º Andar"

def test_cep_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "40711788"

def test_cidade_endereco_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Salvador"

def test_crea_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "1234_Crea"

def test_cep_valor_invalido(engenheiro_valido):
    with pytest.raises(ValueError, match = "O CEP Digitado é Inválido."):
        Engenheiro("Douglas",
                    "71988322399",
                    "douglas@gmail.com",
                    Endereco("Rua beila", "123", "1º Andar", "407111788", "Salvador"),
                        "1234_Crea")

def test_cep_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "O CEP Digitado é Inválido."):
         Engenheiro("Douglas",
                    "71988322399",
                    "douglas@gmail.com",
                    Endereco("Rua beila", "123", "1º Andar", " ", "Salvador"),
                        "1234_Crea")
         
def test_cep_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um CEP Válido."):
        Engenheiro("Douglas",
                    "71988322399",
                    "douglas@gmail.com",
                    Endereco("Rua beila", "123", "1º Andar", 12312332, "Salvador"),
                        "1234_Crea")

def test_logradouro_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um Logradouro Válido."):
        Engenheiro("Douglas",
                    "71988322399",
                    "douglas@gmail.com",
                    Endereco(123, "123", "1º Andar", "40711788", "Salvador"),
                        "1234_Crea")
        
def test_logradouro_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "O Logradouro é Inválido."):
        Engenheiro("Douglas",
                    "71988322399",
                    "douglas@gmail.com",
                    Endereco(" ", "123", "1º Andar", "40711788", "Salvador"),
                        "1234_Crea")

def test_numero_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match= "Digite um Número Válido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", 123, "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")

def test_numero_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "O Número é Inválido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", " ", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")

def test_complemento_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um Complemento Válido."):
        Engenheiro(
                    "Dg",
                    "71988322399",
                    "dg@gmail.com",
                    Endereco("Rua beila", "123", 123, "40711788", "Salvador"),
                    "1234_Crea")

def test_complemento_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "O Complemento é Inválido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", " ", "40711788", "Salvador"),
                                    "1234_Crea")

def test_cidade_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite uma Cidade Válida."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", 123),
                                    "1234_Crea")

def test_cidade_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "A Cidade é Inválida."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", " "),
                                    "1234_Crea")

def test_nome_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = ""):
        Engenheiro(123,
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")
        
def test_nome_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match="O Espaço do nome não pode ficar Vazio. Digite o nome do Usuário."):
        Engenheiro(" ",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")
        
def test_telefone_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um telefone Válido."):
        Engenheiro("Douglas",
                    123,
                    "douglas@gmail.com",
                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                    "1234_Crea")

def test_telefone_invalido(engenheiro_valido):
    with pytest.raises(ValueError, match = "Número de Telefone Inválido."): 
        Engenheiro("Douglas",
                    " ",
                    "douglas@gmail.com",
                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                    "1234_Crea")

def test_email_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um Email Válido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    123,
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")

def test_email_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "O Espaço de email não pode estar Vazio."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    " ",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    "1234_Crea")

def test_crea_tipo_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match = "Digite um Crea válido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    123)

def test_crea_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "Crea Inválido."):
        Engenheiro("Douglas",
                                    "71988322399",
                                    "douglas@gmail.com",
                                    Endereco("Rua beila", "123", "1º Andar", "40711788", "Salvador"),
                                    " ")