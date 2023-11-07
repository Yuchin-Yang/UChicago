from random import random


class Weapon:
  def __init__(self, ship, damage,accuracy, base = None, hull_dmg = None, armor_dmg = None, shield_dmg = None, specials = None ):
    '''
    Base constructor for weapons
    '''
    # TODO Phase 1
    self.ship = ship
    self.damage = damage
    self.accuracy = accuracy 
    self.target = None

    print(self)
    self.hull_modifier = hull_dmg
    self.armor_modifier = armor_dmg
    self.shield_modifier = shield_dmg
    # self.cooldown
    

  def fire(self, combat_round):
    '''
    First checks if a weapon is eligible for firing, otherwise do nothing (charge).
    
    Resolves a weapon applying damage to a specific target.

    If a hit would deduct more damage than the remaining shields the remaining damage of that specific shot is voided. E.g. A ship has 100 shields left. Your weapon made 150 damage. Instead of disabling the shields and doing 50 damage to the armor of the target it will only disable the shield. The next weapon hit will damage armor. Also make sure hull, armor and shields only go down to 0, not become negative values.
    '''
    # TODO Phase 2

    # Target
    if self.target == None:
      return

    # cooldown
    elif combat_round % self.cooldown==0:
        # Torpedo
      if isinstance(self, Torpedo):
        pt_defense = random()
        if self.target.pd < pt_defense: 
          
          if self.target.armor > 0:
            self.target.armor -= (self.damage * self.armor_modifier)
            if self.target.armor < 0:
              self.target.armor = 0
          else:
            if self.target.hull > 0:
               self.target.hull -= (self.damage * self.hull_modifier)
            else:
              self.target.hull = 0
         
      else: 
        if self.accuracy and self.target.evasion != None:
          if random() < self.accuracy and random() > self.target.evasion:
              if self.target.shields > 0:
                self.target.shields -= (self.damage*self.shield_modifier)
                if self.target.shields < 0:
                  self.target.shields = 0
              else:
                self.target.shileds = 0
                if self.target.armor > 0:
                  self.target.armor -= (self.damage*self.armor_modifier)
                else:
                  self.target.armor = 0 
                  if self.target.hull > 0:
                    self.target.hull-= (self.damage*self.hull_modifier)
                  else:
                    self.target.hull = 0


class Railgun(Weapon):
  # TODO Phase 1
  def __init__(self, ship,accuracy=None, damage=None, base = None, hull_dmg = None, armor_dmg = None, shield_dmg = None, specials = None):
    super().__init__(ship,damage,accuracy, 10, 0.9, 0.4, 1.2)
    self.accuracy=accuracy
    self.damage = 10
    self.cooldown = 1

class Laser(Weapon):
  # TODO Phase 1
  def __init__(self, ship, damage=None,accuracy=None, base = None, hull_dmg = None, armor_dmg = None, shield_dmg = None, specials = None):
    super().__init__(ship,damage,accuracy, 60, 1, 1.2, 0.4)
    self.accuracy=accuracy
    self.damage = 60
    self.cooldown = 5
    
class Torpedo(Weapon):
  # TODO Phase 1
  def __init__(self, ship, damage = None,accuracy=None, base = None, hull_dmg = None, armor_dmg = None, shield_dmg = None, specials = None):
    super().__init__(ship, damage, accuracy, 120, 1.2, 1, None, 1)
    self.accuracy = accuracy
    self.damage = 120
    self.cooldown = 15
    self.specials = 1