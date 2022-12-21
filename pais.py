class Pais:

    def __init__(self, name: str, population: int, area: float):


        assert population >= 0, f"Population {population} is not greater than or equal to zero!"
        assert area >= 0, f"Area {area} is not greater than or equal to zero!"

        self.__name = name
        self.__population = population
        self.__area = area

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value 

    @property
    def population(self):
        return self.__population        
    
    @population.setter
    def population(self, value):
        if value >= 0:
            self.__population = value
        else:
            raise Exception("Population can't be less than zero!")
    
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, value):
        if value > 0:
            self.__area = value
        else:
            raise Exception("Area can't be less or equal to zero")

    def __str__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__population}, {self.__area})"
    
    def density(self):
        population = self.population
        area = self.area
        density = float(population)/area
        return f"The density of {self.__name} is {density}"

    