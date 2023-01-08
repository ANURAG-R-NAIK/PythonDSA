class animals():
    def __init__(self, name, age , color):
        
        self.name = name
        self.age = age
        self.color = color
        
        
tom = animals("Cat", 3, "Black")
jerry = animals("Rat", 4, "Brown")

print("tom is a {}".format(tom.name))

print("hello world")