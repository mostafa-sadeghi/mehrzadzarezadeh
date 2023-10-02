class Dog:
    def __init__(self, dog_name, dog_gender, dog_age):
        self.name = dog_name
        self.gender = dog_gender
        self.age = dog_age

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, good boy eatup")

        else:
            print(f"{self.name}, good girl eatup")

    def bark(self, is_loud):
        if is_loud == True:
            print("WOOF WOOF WOOF")
        else:
            print("WOOF")


# german = Dog("jessi", "girl", 5)
# hoski = Dog("loffi", "boy", 7)

# german.eat()
# hoski.eat()

# german.bark(True)
# hoski.bark(False)


class Beagle(Dog):
    def __init__(self, dog_name, dog_gender, dog_age, is_gun_shy):
        super().__init__(dog_name, dog_gender, dog_age)
        self.is_gun_shy = is_gun_shy

    def hunt(self):
        print(f"{self.name} is hunting good")


b1 = Beagle("blalal", "girl", 11, True)
b1.eat()
b1.hunt()
