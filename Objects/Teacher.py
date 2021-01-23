class Teacher:
    id: int
    classTeaching: str
    infectivity: float
    chanceInfected: float

    def __init__(self, id, classTeaching, infectivity):
        self.id = id
        self.classTeaching = classTeaching
        self.infectivity = infectivity