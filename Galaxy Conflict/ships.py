# f.cop
from specs.weapons import Railgun, Laser, Torpedo


class Ship:
    def __init__(self,
                 modules=None,
                 base=None,
                 dmg_modifier=None,
                 accuracy=None,
                 evasion=None,
                 pd=None):
        # TODO Phase 1
        self.modules = modules
        self.base = base
        self.dmg_modifier = dmg_modifier
        self.accuracy = accuracy

        self.weapons = []
        self.max_hull = base
        #this is the one that we start with
        self.max_armor = base
        self.max_shields = base
        self.evasion = evasion
        self.pd = pd

        for i in modules:
            if i == "S":
                self.max_shields += base * .5
            elif i == 'A':
                self.max_armor += base * .5
            elif i == 'E':
                self.evasion *= 2
            elif i == 'P':
                self.pd += (1 / 3)
            elif i == "R":
                self.weapons.append(Railgun(self, accuracy))
            elif i == "L":
                self.weapons.append(Laser(self, None, accuracy))
            elif i == "T":
                self.weapons.append(Torpedo(self))

        print(self.weapons)
        self.hull = self.max_hull
        #modifiy thorughout battle
        self.armor = self.max_armor
        self.shields = self.max_shields

        total_dmg = 0
        total_cooldown = 0
        for i in self.weapons:
            total_dmg += i.damage
            total_cooldown += i.cooldown

        self.DPS = total_dmg / total_cooldown

    def __str__(self):
        # TODO Phase 1
        type = ''
        if isinstance(self, Fighter):
            type = "F"
        elif isinstance(self, Destroyer):
            type = "D"
        elif isinstance(self, Cruiser):
            type = "C"
        elif isinstance(self, Battleship):
            type = "B"

        return "{:>3} | {:>3} | {:>3} | {:>3} | {:>3}% | {:>3}% | {:>3} |".format(
            type, self.base, self.max_armor, self.max_shields,
            round(self.pd * 100), round(self.evasion * 100), round(self.DPS))


class Fighter(Ship):
    def __init__(self,
                 modules=None,
                 base=None,
                 dmg_modifier=None,
                 accuracy=None,
                 evasion=None,
                 pd=None):
        super().__init__(modules, 100, dmg_modifier, 1, 0.8, 0)
        # TODO Phase 1
        self.cost = 1
        # self.weapons = []
        self.weapon_slot = 1
        self.defense_slot = 0
        self.damage_multiplier = 1
        self.fire_priority = "First"


class Destroyer(Ship):
    # TODO Phase 1
    def __init__(self,
                 modules=None,
                 base=None,
                 dmg_modifier=None,
                 accuracy=None,
                 evasion=None,
                 pd=None):
        super().__init__(modules, 300, dmg_modifier, 1, 0.4, 0)
        self.cost = 2
        # self.weapons = []
        self.weapon_slot = 2
        self.defense_slots = 1
        self.damage_multiplier = 1
        self.fire_priority = "Second"


class Cruiser(Ship):
    # TODO Phase 1.
    def __init__(self,
                 modules=None,
                 base=None,
                 dmg_modifier=None,
                 accuracy=None,
                 evasion=None,
                 pd=None):
        super().__init__(modules, 600, dmg_modifier, 0.9, 0.2, 0)
        self.cost = 4
        # self.weapons = []
        self.weapon_slot = 3
        self.defense_slots = 2
        self.damage_multiplier = 1.2
        self.fire_priority = "Third"

        for i in range(len(self.weapons)):
            self.weapons[i].damage *= self.damage_multiplier


class Battleship(Ship):
    # TODO Phase 1
    def __init__(self,
                 modules=None,
                 base=None,
                 dmg_modifier=None,
                 accuracy=None,
                 evasion=None,
                 pd=None):
        super().__init__(modules, 1000, dmg_modifier, 0.8, 0.1, 0)
        self.cost = 8
        # self.weapons = []
        # for i in self.weapons:
        #  self.weapons.append(i)

        self.weapon_slot = 4
        self.defense_slot = 3
        self.damage_multiplier = 1.5
        self.fire_priority = "Last"

        for i in range(len(self.weapons)):
            self.weapons[i].damage *= self.damage_multiplier


# thing= Destroyer()
# print(thing)
