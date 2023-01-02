class Cat: #self is the paramater we named that represents the instance of the class. python methods always take in a paramter for the instance of the class.
    def __init__(self,name): #constructor method is defined under __init__
        self.name = name
    
    def speak(self):
        print(self.name + ' said: meow')

my_cat = Cat('Amy')
other_cat = Cat('Jonny')

my_cat.speak()
other_cat.speak()