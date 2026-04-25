import random

from Abilities import *


class Character:
    def __init__(self, nume):
        self.name = nume
        self.health = 100
        self.attackpwr = random.randint(15, 20)
        self.defpwr = random.randint(10, 15)
        abilities=[DamageReduction(),PowerStrike(),SecondWind(), fourthAbility()]
        self.ability = random.choice(abilities)



