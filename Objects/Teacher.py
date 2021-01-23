class Teacher:
    id: int
    first: str
    last: str
    classTeaching: str
    chanceInfected: float

    def __init__(self, id, firstname, lastname, classTeaching):
        self.first = firstname
        self.last = lastname
        self.id = id
        self.classTeaching = classTeaching