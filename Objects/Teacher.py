class Teacher:
    id: int
    classTeaching: str
    chanceInfected: float

    def __init__(self, id, classTeaching):
        self.id = id
        self.classTeaching = classTeaching