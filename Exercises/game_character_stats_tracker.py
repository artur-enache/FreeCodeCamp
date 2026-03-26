# name getter
# health getter, setter
# level getter, setter
# mana getter, setter
# max_health and max_mana

class GameCharacter:
    _max_health = 100
    _max_mana = 50
    def __init__(self, name):
        self._name = name
        self._health = GameCharacter._max_health
        self._mana = GameCharacter._max_mana
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            new_health = 0

        if new_health > GameCharacter._max_health:
            new_health = GameCharacter._max_health

        self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            new_mana = 0
        if new_mana > GameCharacter._max_mana:
            new_mana = GameCharacter._max_mana

        self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = GameCharacter._max_health
        self.mana = GameCharacter._max_mana
        print(f'{self.name} leveled up to {self.level}!')

    def __str__(self):
        return f'Name: %s\nLevel: %s\nHealth: %s\nMana: %s'%(self.name, self.level, self.health, self.mana)

def main():
    kratos = GameCharacter('Kratos')
    kratos.level_up()
if __name__ == '__main__':
    main()