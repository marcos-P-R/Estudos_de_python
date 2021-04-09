class Pessoa():
    """criando uma pessoa"""

    def __init__(self, nome, idade):
        """Inicializando atributos"""
        self._nome = nome
        self._idade = idade
    
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_idade(self):
        return self._idade
        
    def set_idade(self, idade):
        self._idade = idade
