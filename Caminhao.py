from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, carga):
        super().__init__(marca, modelo, placa, ano)