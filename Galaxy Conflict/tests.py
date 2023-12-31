from specs.weapons import Railgun, Laser, Torpedo
from specs.ships import Battleship, Fighter

def test_ships():
  '''
  This file tests if you implemented your ships and weapon
  classes correctly. It will not catch all possible mistakes. 
  Feel free to modify this file for your own sake.
  '''

  ship = Battleship("PRTRLAA")

  assert ship.max_hull == 1000, \
    f"BS Health should be 1000, is: {ship.max_hull}"
  
  assert ship.max_hull == ship.hull, \
    "health should be the same as max_health."

  assert ship.max_shields == 1000, \
    f"BS Shields should be 1000, is: {ship.max_shields}"
  
  assert ship.max_shields == ship.shields, \
    "shields should be the same as max_shields."

  assert ship.max_armor == 2000, \
    f"BS Armor should be 2000, is: {ship.max_armor}"
  
  assert ship.max_armor == ship.armor, \
    "armor should be the same as max_max_armor."

  assert ship.evasion == 0.1, \
    "BS evasion should be 0.1"

  assert ship.pd == 1/3, \
    "BS pd should be 1/3."

  assert len(ship.weapons) == 4, \
    f"BS should have 4 weapons, has: {len(ship.weapons)}"

  t = 0; r = 0; l = 0
  for weapon in ship.weapons:
    if isinstance(weapon, Torpedo):
      t += 1 
      assert weapon.damage == 180, \
        f"BS Torpedo damage should be 180, was: {weapon.damage}"

      assert weapon.cooldown == 15, \
        f"BS Torpedo max_cooldown should be 15, was: {weapon.cooldown}"

    if isinstance(weapon, Laser):
      l += 1 
      assert weapon.damage == 90, \
        f"BS Laser damage should be 90, was: {weapon.damage}"

      assert weapon.cooldown == 5, \
        f"BS Laser cooldown should be 5, was: {weapon.cooldown}"

    if isinstance(weapon, Railgun):
      r += 1 
      assert weapon.damage == 15, \
        f"BS Railgun damage should be 15, was: {weapon.damage}"

      assert weapon.cooldown == 1, \
        f"BS Railgun cooldown should be 1, was: {weapon.cooldown}"

    assert weapon.target == None, \
      f"BS weapon target should be None, was: {weapon.target}"

  assert l == 1 and r == 2 and t == 1, \
    "BS has the incorrect number of weapons."

  ship = Fighter("R")

  assert ship.max_hull == 100, \
    f"F Health should be 100, is: {ship.max_hull}"
  
  assert ship.max_hull == ship.hull, \
    "health should be the same as max_health."

  assert ship.max_shields == 100, \
    f"F Shields should be 100, is: {ship.max_shields}"
  
  assert ship.max_shields == ship.shields, \
    "shields should be the same as max_shields."

  assert ship.max_armor == 100, \
    f"F Armor should be 100, is: {ship.max_armor}"
  
  assert ship.max_armor == ship.armor, \
    "armor should be the same as max_max_armor."

  assert ship.evasion == 0.8, \
    "F evasion should be 0.8."

  assert ship.pd == 0, \
    "F pd should be 0."

  assert len(ship.weapons) == 1, \
    f"F should have 1 weapons, has: {len(ship.weapons)}"

  assert isinstance(ship.weapons[0], Railgun), \
    "F Weapon is not a Railgun."

  assert ship.weapons[0].damage == 10, \
    f"F Weapon damage should be 10, was: {ship.weapons[0].damage}"


