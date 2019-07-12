import random

class Product:
    price = 10
    weight = 20
    flammability = 0.5
    identifier = random.randint(1000000,9999999)

    def __init__(self, name):
        self.name = name
        """
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000,9999999)
        """

    def stealability(self):
        if (self.price/self.weight) < 0.5:
            status = 'Not so stealable...'
        if (self.price/self.weight) < 1.0:
            status = 'Kinda stealable.'
        else:
            status = 'Very stealable!'
        return status

    def explode(self):
        if (self.flammability * self.weight) < 10:
            product = 'fizzle'
        if (self.flammability * self.weight) < 50:
            product = '...boom!'
        else:
            product = '...BABOOM!!'
        return product

class BoxingGlove(Product):
    weight = 10

    def __init__(self, name):
        self.name = name
        self.weight = 10
        self.price = Product.price

    def explode(self):
        return '...it\'s a glove'

    def punch(self):
        if self.weight < 5:
            message = 'That tickles'
        if self.weight < 15:
            message = 'Hey that hurt!'
        else:
            message = 'OUCH!'
        return message



"""
prod = Product('A Cool Toy')
print(prod.name)
print(prod.weight)
print(prod.flammability)
print(prod.identifier)

print(prod.stealability())
print(prod.explode())


glove = BoxingGlove('Punchy the Third')
print(glove.price)
print(glove.weight)
print(glove.punch())
print(glove.explode())
"""
