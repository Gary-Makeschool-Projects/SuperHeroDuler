from random import randint, choice
import sys


def user_input():
    user = input('>> ')
    return user


class Ability(object):
    def __init__(self, name, max_damage):
        self.name = str(name)
        self.max_damage = int(max_damage)

    def attack(self):
        return randint(0, self.max_damage)


class Weapon(Ability):

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        half = self.max_damage // 2
        full = self.max_damage
        return randint(half, full)


class Armor(object):
    def __init__(self, name, max_block):
        self.name = str(name)
        self.max_block = int(max_block)

    def block(self):
        return randint(0, self.max_block)


class Hero(object):
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """

    def __init__(self, name, starting_health=100):
        '''The Constructor for the Hero CLass
        @Instance variables:
            abilities: List
            name: String
            starting_health: Integer
            current_health: Integer
            deaths: Integer
            kills = Integer
        '''
        self.name = str(name)
        self.starting_health = int(starting_health)
        self.current_health = self.starting_health
        self.deaths = 0
        self.kills = 0
        self.abilities = []
        self.armors = []

    def add_deaths(self, num_deaths):
        """The function to add two Complex Numbers.

    Parameters:
            num (ComplexNumber): The complex number to be added.

    Returns:
            ComplexNumber: A complex number which contains the sum.
        """
        self.deaths += num_deaths

    def add_kill(self, num_kills):
        ''' Update kills with num_kills
        '''
        self.kills += num_kills

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities
        weapon: Ability object
        '''
        self.abilities.append(weapon)

    def add_ability(self, Ability):
        '''Add weapon to self.abilities
        Ability: Ability object
        '''
        self.abilities.append(Ability)

    def attack(self):
        total = 0
        for powers in self.abilities:
            attack_dmg = int(powers.max_damage)
            total += attack_dmg
        return total

    def hero_stats(self):
        if self.deaths > 0:
            KD = self.kills // self.deaths
            sys.stdout.write("Hero: " + self.name + "has a " + str(KD)+ " K/D")
        else:
            sys.stdout.write(
                f"Hero: {self.name} had a KD ratio of {self.kills}")

    def add_armor(self, Armor):
        '''Add Armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(Armor)

    def defend(self, damage_amt=0):
        total = 0
        for armor in self.armors:
            block_val = int(armor.block())
            total += block_val
        return abs(total - damage_amt)

    def take_damage(self, damage):
        taken_damage = self.defend(damage)
        updated_health = self.current_health - taken_damage
        self.current_health = updated_health

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            sys.stdout.write('\x1b[1;31m' + 'Draw!' + '\x1b[0m')

        else:
            while True:
                if self.is_alive():
                    opponent.take_damage(self.attack())
                else:
                    sys.stdout.write('\x1b[1;32m' + opponent.name +
                                     ' won!' '\x1b[0m' + '\n')
                    opponent.add_kill(1)
                    self.add_deaths(1)
                    break

                if opponent.is_alive():
                    self.take_damage(opponent.attack())
                else:
                    sys.stdout.write('\x1b[1;32m' + self.name +
                                     ' won!' + '\x1b[0m' + '\n')
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    break


class Team(object):
    def __init__(self, name):
        self.name = str(name)
        self.heroes = []

    def add_hero(self, Hero):
        """
        description:
        """
        self.heroes.append(Hero)

    def remove_hero(self, name):
        '''
        description: Remove hero from heroes list. If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(str(name))
            else:
                return 0

    def view_all_heros(self):
        for hero in self.heroes:
            sys.stdout.write(hero.name)

    def attack(self, opposing):
        '''
        descrption: Battle each team against each other
        '''
        while len(self.team_alive()) > 0 and len(opposing.team_alive()) > 0:
            hero = choice(self.team_alive())
            enemy = choice(opposing.team_alive())
            hero.fight(enemy)

    def team_alive(self):
        return [x for x in self.heroes if x.is_alive()]

    def revive_heroes(self, health=100):
        '''description: Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            hero.hero_stats()


class Arena(object):
    def __init__(self):
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')

    def create_ability(self):
        '''description: Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What ability does your hero have?")
        sys.stdout.write(
            '\x1b[1;32m' + 'Whats the max damage' + '\x1b[0m' + '\n')
        max_damage = user_input()  # Defaults to 0

        return Ability(name, max_damage)

    def create_weapon(self):
        '''description: Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input('\x1b[1;32m' + "Name of the weapon?" + '\x1b[0m' + '\n')
        sys.stdout.write('\x1b[1;32m' + 'Max damage' + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        max_damage = user_input()
        return Weapon(name, max_damage)

    def create_armor(self):
        '''description: Prompt user for Armor information
            return Armor with values from user input.
        '''
        name = input("Name of your armor?")
        sys.stdout.write(
            '\x1b[1;32m' + 'How much damage do you want it to absorb?' + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        max_block = user_input()
        return Armor(name, max_block)

    def create_hero(self):
        # Getting name and basic health
        sys.stdout.write('\x1b[1;32m' +
                         'Sup? Whats the name of your hero?' + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        name = user_input()

        sys.stdout.write(
            '\x1b[1;32m' + "Whats up {}".format(name) + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        sys.stdout.write(
            '\x1b[1;32m' + 'Default health is 100 you can change it if you want' + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        health = user_input()

        hero = Hero(name, health)

        add_abilities = input(
            '\x1b[1;32m' + "Do you want to add abilities? (yah/nah)" + '\x1b[0m' + '\n')
        if 'y' in add_abilities:
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                another_ability = input('\x1b[1;32m' +
                                        "Add more abilities? (yah/nah)" + '\x1b[0m' + '\n')
                if "y" not in another_ability:
                    break

        add_weapons = input('\x1b[1;32m' +
                            "Do you want to add weapons? (yah/nah)" + '\x1b[0m' + '\n')
        if 'y' in add_weapons:
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                another_weapon = input('\x1b[1;32m' +
                                       "Do you want to add more weapons (yah/nah)" + '\x1b[0m' + '\n')
                if "y" not in another_weapon:
                    break

        add_armor = input('\x1b[1;32m' +
                          "Krikey mate! Do you want to add some armor (yah/nah)" + '\x1b[0m' + '\n')
        if 'y' in add_armor:
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                another_armor = input('\x1b[1;32m' +
                                      "Add more armor? (yah/nah)" + '\x1b[0m' + '\n')
                if "y" not in another_armor:
                    break

        return hero

    def build_team_one(self):
        '''description: Prompt the user to build team_one '''
        sys.stdout.write(
            '\x1b[1;32m' + "How many heros are in your team?" + '\x1b[0m' + '\n')
        sys.stdout.write('\n')
        num_of_heros = int(user_input())

        for i in range(num_of_heros):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build two '''
        sys.stdout.write('\x1b[1;32m' +
                         " How many heros on team two?" + '\x1b[0m' + '\n')
        num_of_heros = user_input()
        for i in range(int(num_of_heros)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    running = True

    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while running:
        arena.team_battle()
        arena.show_stats()
        play_again = input(
            '\x1b[1;32m' + "Do you want to play again? yuh or nah: " + '\x1b[0m' + '\n')

        if "y" not in play_again.lower():
            running = False
        else:
            arena.revive_teams()
