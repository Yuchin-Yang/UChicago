from specs.ships import Fighter , Destroyer, Cruiser, Battleship
import re
import random

class InvalidModuleException(Exception):
  def __init__(self):
    self.message = 'Invalid Module!'

class InvalidFleetException(Exception):
  def __init__(self):
    self.message = "Invalid Fleet!"

class Fleet:
  def __init__(self, userid):
    '''
    Creates a Fleet by reading in a matching text file in the fleets/ folder
    DO NOT CHANGE THIS FUNCTION.
    '''
    self.name = userid
    self.ships = []
    self.read_fleet_file()

  def read_fleet_file(self):
    '''
    This function attempts to load a fleet file and ensures a fleet file is valid.
    '''
    # TODO Phase 1
    total_cost = 0
    for lines in open("fleets/" + self.name + ".txt"):
      s = lines.split(' ')

      defen_size = 0
      attack_size = 0
  
      for modules in s[1]:
        if modules in "SAEP":
          defen_size += 1
  
        elif modules in "RLT":
          attack_size += 1
  
        elif modules.isalpha():
          raise InvalidModuleException()
  
      num_e = 0
      for m in s[1]:
        if m == "E":
          num_e += 1
      if num_e > 1:
        raise InvalidModuleException()

      if s[0] == "F":
        if defen_size > 0 or attack_size > 1:
          raise InvalidModuleException()
        else:
          self.ships.append(Fighter(s[1]))
          total_cost += 1
          
      elif s[0] == "D":
        if defen_size > 1 or attack_size > 2:
          raise InvalidModuleException()
        else:
          self.ships.append(Destroyer(s[1]))
          total_cost += 2
          
      elif s[0] == "C":
        if defen_size > 2 or attack_size > 3:
          raise InvalidModuleException()
        else:
          self.ships.append(Cruiser(s[1]))
          total_cost += 4
          
      elif s[0] == "B":
        if defen_size > 3 or attack_size > 4:
          raise InvalidModuleException()
        else:
          self.ships.append(Battleship(s[1]))
          total_cost += 8

      else:
        raise InvalidFleetException()
        
    if total_cost > 100:
      raise InvalidFleetException()

    
  def get_weapons(self, ship_type):
    '''
    Returns a list of all weapons in the fleet of ships that have not yet been destroyed and belong to the given ship type.
    '''
    # TODO Phase 2
    weapons_remain = []
    for ship in self.ships:
      if ship.hull <=0:
        continue
      if isinstance(ship, ship_type):
        for weapons in ship.weapons:
          weapons_remain.append(weapons)
    return weapons_remain
  
  def __str__(self):
    """
    Returns a string with the summary of a fleet.
    """
   
    # TODO Phase 2
    stats = self.get_stats()

    rep= f"Fleet random\n=========================================================\nShips: {stats['ships']}/{stats['total_ships']}, Command Points: {stats['cost']}/{stats['total_cost']}\nHull: {stats['hull']}/{stats['total_hull']}, Armor: {stats['armor']}/{stats['total_armor']}, Shields: {stats['shields']}/{stats['total_shields']}"

    
    return rep
    
  def get_stats(self):
    """
    Returns a dictionary with the fleets most important values.
    """
    # TODO: Phase 2
    stats = {
      "cost": 0,
      "ships": 0,
      "hull": 0,
      "armor": 0,
      "shields": 0,
      "total_cost": 0,
      "total_ships": 0,
      "total_hull": 0, # 1 just to avoid an intial div/0 error
      "total_armor": 0,
      "total_shields": 0,
      "damage_taken": 0
    }
    stats['total_ships'] = len(self.ships)
    for ship in self.ships:
      if ship.hull > 0:
        stats["ships"] += 1
        
    for ship in self.ships:
      stats['total_cost'] += ship.cost
      if ship.hull > 0:
        stats['cost'] += ship.cost

    for ship in self.ships:
      stats['total_hull'] += int(ship.max_hull)
      if ship.hull > 0:
        stats['hull'] += int(ship.hull)

    for ship in self.ships:
      stats['total_armor'] += int(ship.max_armor)
      if ship.hull > 0:
        stats['armor'] += int(ship.armor)

    for ship in self.ships:
      stats['total_shields'] += int(ship.max_shields)
      if ship.hull > 0:
        stats['shields'] += int(ship.shields)

    hull_dmg = stats['total_hull'] - stats['hull']
    armor_dmg = stats['total_armor'] - stats['armor']
    shields_dmg = stats['total_shields'] - stats['shields']
    stats['damage_taken'] = hull_dmg + armor_dmg + shields_dmg
      
      
    return stats
    
  def list_ships(self):
    # DO NOT CHANGE THIS METHOD
    print("T |  H   |  A   |  S   |  PD  |  E   | DPS |")
    print("==|======|======|======|======|======|=====|")
    for ship in self.ships:
      print(ship)

def create_random_fleet():
  """
  This function will update `random.txt` with a new, randomly composed fleet.
  DO NOT CHANGE THIS FUNCTION
  """
  file = open("fleets/random.txt", "w")
  s = ""

  cp = 0
  while(cp != 100):
    # create random ship type
    type = random.choice("FFFFDDDCCB")

    # if ship type would exceed command points try again, 
    # otherwise increase command points and fill ship with modules
    if type == 'B' and cp + 8 > 100:
      continue
    elif type == 'B':
      cp += 8
      s += "B " + random_weapon_modules(4) + random_defense_modules(3) + "\n"
    elif type == 'C' and cp + 4 > 100:
      continue
    elif type == 'C':
      cp += 4
      s += "C " + random_weapon_modules(3) + random_defense_modules(2) + "\n"
    elif type == 'D' and cp + 2 > 100:
      continue
    elif type == 'D':
      cp += 2
      s += "D " + random_weapon_modules(2) + random_defense_modules(1) + "\n"
    elif type == 'F':
      cp += 1
      s += "F " + random_weapon_modules(1) + "\n"

  file.write(s)
  file.close()


def random_weapon_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    s += random.choice("RLT")
  return s

def random_defense_modules(count):
  # DO NOT CHANGE THIS FUNCTION
  s = ""
  while len(s) < count:
    module = random.choice("SAEP")
    if module == "E" and "E" in s:
      continue
    s += module
  return s