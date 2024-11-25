class Endereco():
    def __init__(self, logradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.logradouro = self._verificar_logradouro_valido(logradouro)
        self.numero = self._verificar_numero_valido(numero)
        self.complemento = self._verificar_complemento_valido(complemento)
        #O metodo de Verificação dentro da classe precisa ter como parametro o objeto que ele esta verificando:
        self.cep = self._verificar_cep_valido(cep)
        self.cidade = self._verificar_cidade_valido(cidade)

#Metodo Verificar se estar vazio e metodo de verificar tipo; ADICIONAR AO CODIGO

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
        )
    
    def _verificar_logradouro_valido(self, logradouro):
        if not isinstance(logradouro, str):
            raise TypeError("Digite um Logradouro Válido.")
        if not logradouro.strip():
            raise ValueError("O Logradouro é Inválido.")
        return logradouro
    
    def _verificar_numero_valido(self, numero):
        if not isinstance(numero, str):
            raise TypeError("Digite um Número Válido.")
        if not numero.strip():
            raise ValueError("O Número é Inválido.")
        return numero 
    
    def _verificar_complemento_valido(self, complemento):
        if not isinstance(complemento, str):
            raise TypeError("Digite um Complemento Válido.")
        if not complemento.strip():
            raise ValueError("O Complemento é Inválido.")
        return complemento
    
    def _verificar_cidade_valido(self, cidade):
        if not isinstance(cidade, str):
            raise TypeError("Digite uma Cidade Válida.")
        if not cidade.strip():
            raise ValueError("A Cidade é Inválida.")
        return cidade

    def _verificar_cep_valido(self, cep):
        if not isinstance(cep, str):
            raise TypeError("Digite um CEP Válido.")
        if len(cep) != 8 or not cep.strip():
            raise ValueError("O CEP Digitado é Inválido.")
        return cep

# endereco = Endereco("123", "asd", "asda", "40711600", "asdas")
# print(endereco)