from Abilities import *
from Characters import *
import random
import argparse
import Output



abilities = {
    "1": DamageReduction(),
    "2": PowerStrike(),
    "3": SecondWind(),
    "4" : fourthAbility()
}




#The battle method gets the two characters as parameters
def battle(firstCharacter, secondCharacter):

    Output.output(f"{firstCharacter.name} attacks! ")



    damageGiven, usedAbilityAttack = firstCharacter.ability.activation(firstCharacter,firstCharacter.attackpwr,is_attacker=True)

    damageGiven -= secondCharacter.defpwr

    damageTaken,usedAbilityDefense = secondCharacter.ability.activation(secondCharacter,damageGiven,is_attacker=False)

    secondCharacter.health = max(0, secondCharacter.health - damageTaken)


    if  usedAbilityAttack is not True and usedAbilityDefense is not True :
        Output.output("No abilities used!")

    Output.output(f"{secondCharacter.name} has {secondCharacter.health} health! ")

#The duel method can get the configuration of one or two characters as parameters
#Also, the perRound flag if we want to change the abilities of the characters at the start of every round
def duel(x = None,y = None, perRound = None):


    if x is None and y is None: #If the configuration of the two characters is not received, it creates them now

        c1 = Character("Character 1")
        c2 = Character("Character 2")

        while c1.attackpwr - c2.defpwr < 0 or c2.attackpwr - c1.defpwr < 0: #Chech if the configurations are viable(the attack power must be bigger then the other's defense power)

            c1 = Character("Character 1")
            c2 = Character("Character 2")
    else:
        c1 = x
        c2 = y

    Output.output(f"{c1.name}: attack = {c1.attackpwr}, defense = {c1.defpwr}")
    Output.output(f"{c2.name}: attack = {c2.attackpwr}, defense = {c2.defpwr}")



    #Random choice of who begins
    choice = random.randint(1,2)
    if choice == 1:
        first = c1
        second = c2
    else:
        first = c2
        second = c1

    roundnum = 1

    while True:
        #After the 100th round we declare stalemate
        if roundnum > 100:
            Output.output("REMIZA!")
            return 0
        Output.output(f"ROUND {roundnum}:")
        roundnum+=1

        battle(first, second)

        if c1.health <= 0:
            Output.output(f"{c2.name} won!")
            return 2

        if c2.health <= 0:
            Output.output(f"{c1.name} won!")
            return 1

        #If --per-Round is present in the run command
        if perRound is True:

            randomChoice = random.choice(list(abilities.keys()))
            c1.ability = abilities.get(randomChoice,abilities[randomChoice])
            Output.output(f"{c1.name} now has the {c1.ability.nume} ability! ")

            randomChoice = random.choice(list(abilities.keys()))
            c2.ability = abilities.get(randomChoice,abilities[randomChoice])
            Output.output(f"{c2.name} now has the {c2.ability.nume} ability! ")




        first,second = second, first





#For reading character configurations from the user
def characterStatsInput():


    print("Character 1 configuration:")
    c1 = Character("Character 1")
    c2 = Character("Character 2")
    pwr = int(input("Character 1 attack power: "))
    dfs = int(input("Character 1 defense power: "))
    print("Ability list: 1.Damage Reduction, 2.Power Strike, 3.Second Wind, 4.THE FOURTH ABILITY (enter the number)")
    ability_choice = input("Character 1 ability: ")
    randomKey = random.choice(list(abilities.keys()))
    c1.ability = abilities.get(ability_choice,abilities[randomKey])


    c1.attackpwr = pwr
    c1.defpwr = dfs

    pwr = int(input("Character 2 attack power: "))
    dfs = int(input("Character 2 defense power: "))
    c2.attackpwr = pwr
    c2.defpwr = dfs
    ability_choice = input("Character 2 ability: ")
    randomKey = random.choice(list(abilities.keys()))
    c2.ability = abilities.get(ability_choice,abilities[randomKey])


    return c1,c2


#Main menu method
def menu():

    parser = argparse.ArgumentParser()
    parser.add_argument("--per-round",action= "store_true",help="You can choose if you want the ability assignment to be at the beginning of the game or at the beginning of every round")
    args = parser.parse_args()
    perRound = args.per_round


    print("Duel Game!")
    print("Menu: ")
    print("1. Duel")
    print("2. Test Win Rates")
    print("3. Exit")
    print("--per-round - toggle between fixed and per-round ability assignment")
    comanda = input()

    match comanda:
        case "1":
            print("Duel")
            duel(None,None,perRound)
        case "2":
            print("Where to print the battles: (enter the number)")
            print("1. Console")
            print("2. txt file within the main folder (if it already exists it will be overwritten)")
            print("3. Don't print")
            Output.printChoice = int(input())

            if Output.printChoice == 2:
                Output.file = open("Battles.txt","w")



            print("Test Win Rates")
            c1,c2 = characterStatsInput()
            counter = 1

            firstCharacterWins = 0
            secondCharacterWins = 0
            remize = 0
            while counter <= 1000:
                winner = duel(c1,c2,perRound)
                c1.health = 100
                c2.health = 100
                if winner == 1:
                    firstCharacterWins += 1
                elif winner == 2:
                    secondCharacterWins += 1
                elif winner == 0:
                    remize +=1
                counter +=1

            print("RESULT")
            print(f"The first character has {firstCharacterWins} wins")
            print(f"The second character has {secondCharacterWins} wins")
            print(f"There were {remize} stalemates")
            print(f"Percentages: Character 1: {firstCharacterWins/10}%, Character 2: {secondCharacterWins/10}%, Stalemates: {remize/10}")
            if Output.printChoice == 2:
                Output.file.close()

        case "3":
            print("Exiting")
            return
        case _:
            print("Invalid input")
            return




menu()




