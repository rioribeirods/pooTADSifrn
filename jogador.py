class Jogador:
    all = []
    def __init__(self, nome: str, camisa: int, num_gols: int):

        assert camisa > 0 and camisa <= 99, f"Número {camisa} inválido! Tente algum número entre 0 e 99."
        assert num_gols >=0, f"Número de gols não pode ser negativo."
        assert nome != "", f"Insira um nome válido"

        self.__nome = nome
        self.__camisa = camisa
        self.__num_gols = num_gols

        Jogador.all.append(self)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def camisa(self):
        return self.__camisa

    @property
    def num_gols(self):
        return self.__num_gols

    @nome.setter
    def nome(self, value):
        if len(value) > 10:
            raise Exception("Nome muito extenso, máximo de 10 dígitos")
        else:
            self.__nome = value 

    @camisa.setter
    def camisa(self, value):
        if value > 0 and value <= 99:
            self.__camisa = value  
        else:
            raise Exception(f"Número {value} inválido! Tente algum número entre 0 e 99.")  

    @num_gols.setter
    def num_gols(self, value):
        if value >= 0:
            self.__num_gols = value
        else:
            raise Exception(f"Número de gols não pode ser negativo.")  
    
    @staticmethod
    def ordenar():
        sortedByName = sorted(Jogador.all, key=lambda x: x.nome)
        for i in range(0, len(sortedByName)):
            print(sortedByName[i].__str__())
        return ""

    @staticmethod
    def combina(jogador1, jogador2):
        if jogador1.num_gols == jogador2.num_gols and jogador1.camisa == jogador2.camisa:
            return "Número de gols e camisas combinam"
        elif jogador1.camisa == jogador2.camisa:
            return "Camisas combinam"
        elif jogador1.num_gols == jogador2.num_gols: 
            return "Número de gols combinam"
        else:
            return "Não combina"

    def __str__(self):
        return f"{self.__class__.__name__}('{self.__nome}', {self.__camisa}, {self.__num_gols})"

