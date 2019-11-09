import random

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=0):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)


    def stealability(self):
        '''calculates the price divided by the weight, and then
            returns a message: if the ratio is less than 0.5 return "Not so stealable...",
            if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
            and otherwise return "Very stealable!"'''
        price_by_weight = self.price / self.weight
        
        if price_by_weight < 0.5:
            return 'Not so stealable'
        elif (price_by_weight >= 0.5) & (price_by_weight < 1):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'


    def explode(self):
        '''calculates the flammability times the weight, and then
            returns a message: if the product is less than 10 return "...fizzle.", if it is
            greater or equal to 10 but less than 50 return "...boom!", and otherwise
            return "...BABOOM!!"'''

        flam_weight = self.flammability * self.weight

        if flam_weight < 10:
            return '...fizzle'
        elif (flam_weight >= 10) & (flam_weight < 50):
            return '...boom!'
        else:
            return '...KABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=0):
        super().__init__(name, price=price, weight=weight, flammability=flammability, identifier=identifier)


    def set_weight(self, weight):
        self.weight = weight


    def explode(self):
        return "...it's a glove"


    def punch(self):
        '''calculates whether the weigh of a product will hurt you when punched'''

        if self.weight < 5:
            return 'That tickles'
        elif (self.weight >= 5) & (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!!!'

