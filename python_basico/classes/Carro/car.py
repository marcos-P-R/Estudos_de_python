class Carro():
    """ criando um carro """

    def __init__(self, marca, cor, velocidade_maxima):
        self.marca = marca
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerando(self):
        if self.velocidade_maxima >= self.velocidade_atual:
            self.velocidade_atual = self.velocidade_atual + 10
            return self.velocidade_atual
        else:
            return "Velocidade Maxima alcançada"

    def get_velocidade_atual(self):
        return self.velocidade_atual