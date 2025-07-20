class Bird():
    def walk(self):
        print('HOPPING ARROUND')
class Mammal():
    def walk(self):
        print("jogging around...")
class Movements:
    @classmethod
    def move(self,thing):
        thing.walk()


bird=Bird()
Dog=Mammal()
Movements.move(bird)        
Movements.move(Dog)