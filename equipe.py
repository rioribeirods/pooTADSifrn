from jogador import Jogador

class Equipe:
    def __init__(self, pais: str, jogs: list):

        assert pais != "", f"Insira um nome válido"

        self.__pais = pais
        self.__jogs = jogs
    
    def listar(self):
        sorted_by_name = sorted(self.jogs, key=lambda x: x.nome)
        for i in range(0, len(sorted_by_name)):
            print(sorted_by_name[i].__str__())
        return 0

    def camisas(self):
        camisas = sorted(self.jogs, key=lambda x: x.camisa)
        for i in range(0, len(camisas)):
            print(camisas[i].__str__())
        return 0
    
    def artilheiros(self):
        artilheiros = sorted(self.jogs, key=lambda x: x.num_gols, reverse=True)
        for i in range(0, 3):
            print(artilheiros[i].__str__())
        return 0

    @property
    def pais(self):
        return self.__pais
    
    @property
    def jogs(self):
        return self.__jogs

    @jogs.setter
    def inserir(self, value):
        return self.__jogs.append(value)


    def __str__(self):
        return f"{self.__class__.__name__}('{self.__pais}', {len(self.__jogs)})"
