class DollHouse:
    def __init__(self):
        self.height = 128
        self.color = "pink"
        self.age = 1
        self.material = "plastic"

    def about(self):
        print("This is a doll house")


class Doll(DollHouse):
    def __init__(self):
        super().__init__()
        self.material = "wood"
        self.dress = "red"

    def about_myself(self):
        print("This is a doll")


class Barbi(Doll):
    def __init__(self):
        super().__init__()
        print(self.height)
        print(self.color)
        print(self.age)
        print(self.material)
        print(self.dress)


pp = Doll()
pp.about_myself()



Barbara = Barbi()
Barbara.about_myself()
Barbara.about()
