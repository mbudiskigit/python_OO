class Car:

    make = 'Volks'
    
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color

    def drive(self):
        print(self.name + ' started')

    @staticmethod
    def open():
        print('Open')

    @classmethod
    def wash(cls):
        print(cls.make)