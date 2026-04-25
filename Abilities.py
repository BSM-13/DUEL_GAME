import Output
import random

#Using class inheritance to make adding new abilities easier

class Ability:
    def __init__(self, nume):
        self.nume = nume

    def activation(self,character,damage,is_attacker): #Every activation method gets as parameters the character that uses it, the damage taken or given and if the character is an attacker or being attacked
        pass #Also, it returns usually the damage dealt and if the ability actually activated


class PowerStrike(Ability):
    def __init__(self):
        super().__init__("Power Strike")

    def activation(self, character, attack,is_attacker):
        if is_attacker and random.randint(1,4)==4:
            Output.output(f"{character.name} activates Power Strike! ")
            return attack * 1.5, True
        return attack, False



class DamageReduction(Ability):
    
    def __init__(self):
        super().__init__("Damage Reduction")

    def  activation(self,character, damage, is_attacker):
        if not is_attacker and random.randint(1,4)==4:
            Output.output(f"{character.name} activates Damage Reduction! ")
            return damage/2, True
        return damage, False

class SecondWind(Ability):

    def __init__(self):
        super().__init__("Second Wind")

    def activation(self,character, damage,is_attacker):
        if not is_attacker and random.randint(1,4)==4 and character.health - damage<30:
            Output.output(f"{character.name} activates Second Wind! ")
            character.health +=5
            return damage, True
        return damage, False


class fourthAbility(Ability):
    def __init__(self):
        super().__init__('Fourth Ability')

    def activation(self,character, damage,is_attacker):
        if random.randint(1,4)==4 and is_attacker:
            Output.output(f"{character.name} activates THE FOURTH ABILITY! (10% chance to give triple damage) ")
            if random.randint(1,10) == 10:
                Output.output(f"{character.name} DEALS TRIPLE DAMAGE! ")
                return damage * 3,True
            Output.output(f"Even though {character.name} activated THE FOURTH ABILITY, he has no luck and deals normal damage! ")
        return damage, False



