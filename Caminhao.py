from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, carga):
        super().__init__(marca, modelo, placa, ano)
        self.__carga = carga
    
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
 - Capacidade de carga: {self.__carga}'''