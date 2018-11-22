import random

# Ability class
# attack_strength is refferring to the max attack a user can have which is defined when we instantiate the class.
# attack_val is the value after we do a math operation to get what our attack value is (within min-max attack range)
class Ability:
    int_value = 20 // 8
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = int(attack_strength)
    # this func should return attack value
    def attack(self):
        # Calculate lowest attack value as an integer.
        lowest_attack_val = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        # random.randint(lowest_attack_val, self.attack_strength)
        # Return attack value between 0 and the full attack.
        attack_val = random.randint(lowest_attack_val, self.attack_strength)
        return attack_val
    def update_attack(self, attack_strength):
        # Update attack value
        return self.attack_strength

# Hero class
class Hero:
    def __init__(self, name, health=100): # Initialize starting values
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        for i in
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total_defense=0
        if self.health < 1:
            return 0
        # armors or abilities here?
        for pieceOfArmor in self.armors:
            armor_defense = pieceOfArmor.defend()
            total_defense += armor_defense
            # or return sum([a.attack() for a in self.abilities])
        # this calculates how much our heroes are defended on the whole team..
        return total_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health-=damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills+=num_kills

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    # this func should run attack() on every ability hero has
    def attack(self):
        totalAttack = 0
        # self.abilities = list()
        # Call the attack method on every ability in our ability list
        # i refers to ability
        for i in self.abilities:
            # i.attack()
            totalAttack+=i.attack()
            # print("total attack is: ", totalAttack)
        # Add up and return the total of all attacks
        return (totalAttack)

    # had to create func to add armor to list of armors a hero can have.
    def add_armor(self, armor):
        self.armors.append(armor)
# hero should be able to choose weapon, this extends Ability class but different attack computation.
class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
    # this func should return attack value (0, attack_strength) - method overriding
    # m.o - specify a different functionality for methods that are inherited from the superclass.
    def attack(self):
        # Return attack value between 0 and the full attack.
        attack_val = random.randint(0, self.attack_strength)
        return attack_val

# team class manages all of our superheroes.
# team name is team name. I made that var name change from just name because it was confusing me.

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        # self.team_kills = 0
        # self.heroDeathCount=0

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        totalAttackStrength=0
        # totalAttackStrength = sum([hero.attack() for hero in self.heroes])
        # this is the same as saying
        for hero in self.heroes:
            # print("hero attack here")
            # print(hero.attack())
            totalAttackStrength+= hero.attack()
        # print(totalAttackStrength)
        # for i in self.heroes:
        kills=0
        kills = other_team.defend(totalAttackStrength)
        # print(self.update_kills)(enemiesKilledThisRound)
        for i in self.heroes:
            i.add_kill(kills)
            # print(kills)
        for i in other_team.heroes:
            i.deaths += kills
            # print(i.deaths)

        # print(self.team_kills)
        # print("hero death count: ")
        # print(self.heroDeathCount)


    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes
        with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        totalDefense=0
        excessDamageOnHero=0
        for armorpiece in self.heroes:
            totalDefense += armorpiece.defend()
        if damage_amt > totalDefense:
            excessDamageOnHero = damage_amt - totalDefense

        return self.deal_damage(excessDamageOnHero)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack 'to the deal damage function'.
        """
        lenOfHeroes = len(self.heroes)
        distributedDmg = damage // lenOfHeroes
        heroesDied = 0
        for i in self.heroes:
            i.health -= distributedDmg
            if i.health <= 0:
                heroesDied+=1
        return heroesDied

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for i in self.heroes:
            i.health = i.start_health
            # print(i.start_health)
    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        for hero in self.heroes:
            print("kills: {} : deaths: {}".format(hero.kills, hero.deaths))
        return 0
    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for i in self.heroes:
            if i.health <= 0:
                i.kills+=1

    def add_hero(self, hero):
        """Add Hero object to heroes list."""
        self.heroes.append(hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        hero = self.find_hero(name)
        # print("Look for hero: {}".format(name))
        # print("Found hero: {}".format(hero))
        if hero == 0:
            return 0
        if hero is not None:
            # print(hero)
            self.heroes.remove(hero)
        else:
            print("not here")
            return 0

    def find_hero(self, name):
        print(name)
        # indexOfHero = -1
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        # if Hero not in heroes:
        #     return 0
        # name is a string.. so this might not work..
        # for hero in heroes:
        #     if hero == Hero
        #     return hero
        # for index, hero in enumerate(self.heroes):
        #     if hero.name == name:
        #         indexOfHero = index
        # return hero
        # if hero.name not in self.heroes:
        #     return 0
        # print(self.heroes)
        if len(self.heroes) == 0:
            return 0
        for hero in self.heroes:
            print("in for looop")
            print(hero)
            if hero.name == name:
                return hero
            else:
                print("return 00000 ")
                return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print("viewing")
        # print(self.heroes)
        for hero in self.heroes:
            print(hero.name)

    # Ikey's idea to create more modular code, use this in the Arena Class.
    # def stillStanding(self):
    #     for hero in self.heroes:
    #         if hero.health > 0:
    #             return True
    #         return False


#  teams duel each other
# heroes should have armor that they can wear to help defend themselves.
# need an amount of health that they can lose in a fight.
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = int(defense)

    def defend(self):
        # print("defend run")
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        damageProtection = random.randint(0, self.defense)
        return damageProtection

# making sure that all of our rules are followed in our game.
# It will be responsible for creating and managing our teams and regulating how they fight.
class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """
        self.team_one = self.build_team_one()
        self.team_two = self.build_team_two()
        # self.team_one = self.build_team_one()
        # self.team_two = self.build_team_two()

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        # Create Team
        self.team_one = input('What is your team name? ')
        self.team_one = Team(self.team_one)
        print("Welcome to the arena, team " + str(self.team_one.name) + "!")
        # usersHero = Hero(input("Hero: "))
        # usersHeroAbility = Ability(input(""))
        # add ability name and attack_strength
        # self.team_one.add_hero(usersHero)
        addingHeroes = True
        addingAbilities = True
        # Add a Hero to Team
        while addingHeroes:
            usersHero = input("Add a Hero: ")
            # create a hero and pass in the name
            heroObj = Hero(usersHero)
            # add hero to this list of hero objects
            self.team_one.add_hero(heroObj)
            # for hero in self.team_one.heroes:
            #     print(hero)
            # Add Ability to Hero in Team
            addingArmor = True
            while addingAbilities:
                ability_name = input("Give your hero an ability: ")
                ability_attack_strength = input("What attack strength should {} have? ".format(ability_name))
                new_ability = Ability(ability_name, ability_attack_strength)
                print(usersHero)
                heroObj.add_ability(new_ability)
                userWantsToAddMore = input("Wanna add more? Y or N: ")
                if userWantsToAddMore == "Y" or userWantsToAddMore == "y":
                    addingAbilities = True
                else:
                    addingAbilities = False
            # Add Armor to Hero in Team
            while addingArmor:
                armor_name = input("Name the armor: ")
                armor_defense = input("Armor Defense: ")
                new_armor = Armor(armor_name, armor_defense)
                heroObj.add_armor(new_armor)
                userWantsToAddMore = input("Wanna add more? Y or N: ")
                if userWantsToAddMore == "Y" or userWantsToAddMore == "y":
                    addingArmor = True
                else:
                    addingArmor = False
            userWantsToAddMore = input("Wanna add a new hero? Y or N: ")
            if userWantsToAddMore == "N" or userWantsToAddMore == "n":
                addingHeroes = False
            else:
                addingHeroes = True
        print("Cool thanks for creating your team.. let's continue. Player 2")
        return self.team_one
    def build_team_two(self):
        """
        This method should allow a user to build team one.
        """
        # Create Team
        self.team_two = input('What is your team name? ')
        self.team_two = Team(self.team_two)
        print("Welcome to the arena, team " + str(self.team_two.name) + "!")
        # usersHero = Hero(input("Hero: "))
        # usersHeroAbility = Ability(input(""))
        # add ability name and attack_strength
        # self.two.add_hero(usersHero)
        addingHeroes = True
        addingAbilities = True
        # Add a Hero to Team
        while addingHeroes:
            usersHero = input("Add a Hero: ")
            heroObj = Hero(usersHero)
            self.team_two.add_hero(heroObj)
            # for hero in self.two.heroes:
            #     print(hero)
            # Add Ability to Hero in Team
            addingArmor = True
            while addingAbilities:
                ability_name = input("Give your hero an ability: ")
                ability_attack_strength = input("What attack strength should {} have? ".format(ability_name))
                new_ability = Ability(ability_name, ability_attack_strength)
                heroObj.add_ability(new_ability)
                userWantsToAddMore = input("Wanna add more? Y or N: ")
                if userWantsToAddMore == "Y" or userWantsToAddMore == "y":
                    addingAbilities = True
                else:
                    addingAbilities = False
            # Add Armor to Hero in Team
            while addingArmor:
                armor_name = input("Name the armor: ")
                armor_defense = input("Armor Defense: ")
                new_armor = Armor(armor_name, armor_defense)
                heroObj.add_armor(new_armor)
                userWantsToAddMore = input("Wanna add more? Y or N: ")
                if userWantsToAddMore == "Y" or userWantsToAddMore == "y":
                    addingArmor = True
                else:
                    addingArmor = False
            userWantsToAddMore = input("Wanna add a new hero? Y or N: ")
            if userWantsToAddMore == "N" or userWantsToAddMore == "n":
                addingHeroes = False
            else:
                addingHeroes = True
        print("Cool thanks for creating your team.. let's continue. Player 2")
        return self.team_two

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        # team one attack team two
        # team two can then defend, update their health and team members
        # team two will next attack back
        battling = True
        while battling == True:
            # print(self.team_one)
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            if self.is_team_dead(self.team_one) == True:
                print(self.team_two.name + " WINS!")
                battling=False
                break
            if self.is_team_dead(self.team_two) == True:
                print(self.team_one.name + " WINS!")
                battling=False
                break
        # while self.team_one.stillStanding() and self.team_one.stillStanding():
        #     self.team_one.attack(self.team_two)
        #     self.team_two.attack(self.team_one)
        #     if self.team_one.stillStanding():
        #         print("Team one wins the fight")
        #         self.show_stats()
        #     else:
        #         print("Team two wins the fight")
        #         self.show_stats()

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print("Here's the game stats...")
        print("Team One:")
        self.team_one.stats()
        print("Team Two:")
        self.team_two.stats()

    # check to see if team is dead, if so return True of False for program to know.
    def is_team_dead(self, team):
        heroes_dead = 0
        for hero in team.heroes:
            if hero.health <= 0:
                heroes_dead += 1
        # if all our heroes have died!
        if heroes_dead == len(team.heroes):
            return True
        else:
            return False

# Ikey's words of wisdom becausee we don't know what the main is doing.
arena = Arena()
arena.team_battle()
arena.show_stats()

# if __name__ == "__main__":
    # game_is_running = True

    # Instantiate Game Arena
    # arena = Arena()

    #Build Teams
    # arena.build_team_one()
    # arena.build_team_two()

    # while game_is_running:

    #     arena.team_battle()
    #     arena.show_stats()
    #     play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        # if play_again.lower() == "n":
        #     game_is_running = False

        # else:
            #Revive heroes to play again
            # arena.team_one.revive_heroes()
            # arena.team_two.revive_heroes()
