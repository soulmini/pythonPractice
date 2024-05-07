

class myClass:
    # constructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def whoIam(self) :
        print(self.name, self.age);

     


# Destructor:
    def __del__(self) :
        print('class has been clened')            


obj = myClass('ayuhs', 18)
# print(obj.name, obj.age)        
obj.whoIam()