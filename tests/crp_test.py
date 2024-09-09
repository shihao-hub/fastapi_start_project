class Dog:
    def say(self):
        print("I am Dog")


class Huskey:
    def __init__(self):
        self._base = Dog()

    def say(self):
        return self._base.say()


huskey = Huskey()
huskey.say()
