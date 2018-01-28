

class Something:
    some = 'thing'
    __mama = 'papa'

    def set_mama(self, value):
        self.__mama = value

    def get_mama(self):
        return self.__mama

class Pet(Something):
    name = 'pet'
    __mama = 'OWO'

    def __init__(self):
        self.name = 'pet'






lilu = Pet()
#lilu.name = 'lilu'
print(vars(lilu))
print(lilu.name)
print(Pet.name)
print(lilu.get_mama())


