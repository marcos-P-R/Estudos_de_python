from pessoa import Pessoa

class Pessoa_fisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self._CPF = CPF

    def get_CPF(self):
        return self._CPF
    
    def set_CPF(self, CPF):
        self._CPF = CPF