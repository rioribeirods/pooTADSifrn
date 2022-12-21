class Pecas:
    all = []
    def __init__(self, ladoE: int, ladoD: int):
        
        assert ladoE >= 1 and ladoE <= 6, f"Valor {ladoE} inválido! Insira valores entre 1 e 6"
        assert ladoD >= 1 and ladoD <= 6, f"Valor {ladoD} inválido! Insira valores entre 1 e 6"

        self.__ladoE = ladoE
        self.__ladoD = ladoD

        Pecas.all.append(self)
    
    @property
    def ladoE(self):
        return self.__ladoE

    @property
    def ladoD(self):
        return self.__ladoD

    @ladoE.setter
    def ladoE(self, value):
        if value >= 1 and value <= 6:
            self.__ladoE = value 
        else:
            raise Exception(f"Valor {value} inválido! Insira valores entre 1 e 6")
    
    @ladoD.setter
    def ladoD(self, value):
        if value >= 1 and value <= 6:
            self.__ladoD = value 
        else:
            raise Exception(f"Valor {value} inválido! Insira valores entre 1 e 6")

    def __str__(self):
        return f"{self.__class__.__name__}('{self.__ladoE}', '{self.__ladoD}')"

    @classmethod
    def combina(cls):
        if cls.all[0].ladoE == cls.all[1].ladoD or cls.all[0].ladoE == cls.all[1].ladoE:
            return "Combina"
        elif cls.all[0].ladoD == cls.all[1].ladoD or cls.all[0].ladoE == cls.all[1].ladoE:
            return "Combina"
        else:
            return "Não combina"