import random
import string


class RandomName:
    def __init__(self):
        self.name= ''.join(random.choices(string.ascii_letters, k=random.randint(3,9)))
    def getName(self):
        return str(self.name)
