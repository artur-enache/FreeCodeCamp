class AppException(Exception):
    pass

class AttributeValidation(AppException):
    pass

class AbilityValidation(AppException):
    pass

class AbilityCoreAttributeConflict(AppException):
    pass

class CreatureDuplicate(AppException):
    pass

class CreatureMissing(AppException):
    pass

class Creature:
    creature_count = 0 # This never gets decremented

    def __init__(self, name, hit_points, strength, defense):
        if not isinstance(name, str) or not 0 < len(name) <= 10:
            raise AttributeValidation('Name must be a string, between 0 and 10 characters')

        for attribute in hit_points, strength, defense:
            if not isinstance(attribute, int) or not 0 < attribute <= 10:
                raise AttributeValidation('All attributes must be an integer, between 0 and 10')
        self.core_stats = ['core_stats', 'name', 'hit_points', 'strength', 'defense']
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.defense = defense

        Creature.creature_count += 1

        print(f'Creature {name} has been created successfully!')

    def __str__(self):
        return f'{self.name} (HP: {self.hit_points} | STR: {self.strength} | DEF: {self.defense})'

    def __len__(self):
        return self.hit_points + self.strength + self.defense

    def __repr__(self):
        return f'Creature(\'{self.name}\')'

    def __eq__(self, opponent):
        are_equal = True
        for self_attribute, opponent_attribute in zip([self.hit_points, self.strength, self.defense], [opponent.hit_points, opponent.strength, opponent.defense]):
            if self_attribute == opponent_attribute:
                continue
            else:
                are_equal = False
                break

        return self.name.lower() == opponent.name.lower() and are_equal

    def learn_ability(self, ability_name, description):
        for element in ability_name, description:
            if not isinstance(element, str) or not 0 < len(element) <= 255:
                raise AbilityValidation('The ability name and description must be a non-empty string')

        if ability_name.lower() in self.core_stats:
            raise AbilityCoreAttributeConflict(f'The ability \'{ability_name.title()}\' conflicts with a core attribute!')

        if hasattr(self, ability_name.lower()):
            #raise AbilityValidation(f'There already exists an ability {ability_name.title()}!')
            return f'There already exists an ability {ability_name.title()}!'
        else:
            setattr(self, ability_name.lower(), description)
            return f'Creature \'{self.name}\' has learned \'{ability_name}\'!'

    def use_ability(self, ability_name):
        try:
            return getattr(self, ability_name.lower())
        except AttributeError:
            return f'Creature {self.name} does not have the {ability_name.title()} ability!'

    def forget_ability(self, ability_name):
        try:
            delattr(self, ability_name.lower())
            return f'Ability \'{ability_name.title()}\' has been deleted successfully!'
        except Exception:
            return f'Nothing to remove, the creature does not have this ability.'

    def list_abilities(self):
        return [ item.title() for item, value in self.__dict__.items() if hasattr(self, item.lower()) and item.lower() not in self.core_stats ]

class Arena:
    def __init__(self):
        self.roster = []

    def register(self, creature):
        for item in self.roster:
            if item == creature:
                raise CreatureDuplicate(f'Creature \'{creature.name}\' has already been added to the roster!')
        self.roster.append(creature)

    def roster_summary(self):
        empty_roster = 'The roster is empty.'
        non_empty_roster = f'\n{'\n'.join(str(item) for item in self.roster)}'
        return non_empty_roster if self.roster else empty_roster

    def battle(self, attacking_creature, defending_creature):
        for contender in attacking_creature, defending_creature:
            if not contender in self.roster:
                raise CreatureMissing(f'The creature \'{contender.name}\' is missing from the roster!')

        try:
            attacker_hp = attacking_creature.hit_points
            attacker_dmg = (attacking_creature.strength - defending_creature.defense)
            attacker_dmg = attacker_dmg if attacker_dmg > 0 else 1

            defender_dmg = (defending_creature.strength - attacking_creature.defense)
            defender_dmg = defender_dmg if defender_dmg > 0 else 1

            defender_hp = defending_creature.hit_points
            while attacker_hp > 0 and defender_hp > 0:
                #print(f'Creature \'{attacking_creature.name}\' attacks!')
                defender_hp -= attacker_dmg
                #print(f'Creature \'{attacking_creature.name}\' hits for {attacker_dmg} hit points!')
                if defender_hp <= 0:
                    break
                #print(f'It is \'{defending_creature.name}\'s\' turn!')
                attacker_hp -= defender_dmg
                #print(f'Creature \'{defending_creature.name}\' hits for {defender_dmg} hit points!')
                if attacker_hp <= 0:
                    break

            if attacker_hp <= 0:
                print(f'Creature \'{attacking_creature.name}\' has been defeated!')
                return defending_creature
            elif defender_hp <=0:
                print(f'Creature \'{defending_creature.name}\' has been defeated!')
                return attacking_creature
        except Exception as e:
            raise AppException('Something fatal has happened') from e

def main():
    test = Creature('Developer', 10, 10, 2)
    print('Creature count: ', Creature.creature_count)
    test2 = Creature('Tester', 10, 1, 1)
    test3 = Creature('c', 10, 1, 8)
    #test2 = Creature('a', 10, 1, 8)
    print('Creature count: ', Creature.creature_count)
    #print(test == test2)
    print('String test: ', test)
    print('Length test: ', len(test))
    print('Repr test: ', [test, test2])
    print(test.learn_ability('Test Ability', 'a'))
    #print(test.learn_ability('name', 'This is a failure'))
    #test.learn_ability('Test ability', '68')
    print('Test the ability: ', test.use_ability('Tst Ability'))
    print('Test removing the ability: ', test.forget_ability('Tet Ability'))
    print('Equality test: ', test == test2)
    #print(test.__dict__.keys())
    print('Ability list: ', test.list_abilities())
    arena = Arena()
    arena.register(test)
    arena.register(test2)
    arena.register(test3)
    print(arena.roster_summary())
    try:
        print('Winner 1: ', arena.battle(test, test2))
        print('Winner 2: ', arena.battle(test, test3))
    except CreatureMissing:
        print('ERROR: another one')
    except AppException:
        print('ERROR: Something went wrong!')
if __name__ == '__main__':
    main()