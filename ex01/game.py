class GoTCharacter:
    def __init__(self, first_name, isAlive):
        self.first_name = first_name,
        self.isAlive = isAlive,


class Stark(GoTCharacter):
    """ A class representing the Stark Family.
    Or when bad things happen to good people """
    def __init__(self, first_name=None, isAlive=True):
        super().__init__(first_name, isAlive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.isAlive = False
