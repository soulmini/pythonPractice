class room :
    # cons
    # def __init__(self, laptop) :
    #     self.laptop = laptop
    def speak(self) :
        print('Animal Sleaking')        


class room2(room) : 
    def bark(self) :
        print('Dog Is barking')



obj1 = room()
obj2 = room2()
# obj2 = room2('charger_avita', 'Avita')

obj1.speak()
obj2.bark()