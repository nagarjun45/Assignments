class Person():
    def __init__(self):
        pass

    def get_gender(self):
        pass

class Male(Person):
    #def __init__(self):
    def get_gender(self):
        print("male")

class Female(Person):
    def get_gender(self):
        print("Female")

obj = Male()
obj.get_gender()
obj2 = Female()
obj2.get_gender()


        
