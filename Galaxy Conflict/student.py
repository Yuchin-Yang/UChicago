import random


from specs.ships import *

def set_targets(myFleet, enemyFleet):
  '''
  This should ensure that each weapon of the attacker's ships 
  points towards a valid target (ship) of the defender.
  This function must only change weapons's target property!
  The target property must be a ship in the enemy Fleet.
  '''
  # TODO Phase 3
  minheap_Hull= MinHeap()
  minheap_Shield= MinHeap()
  minheap_Armor= MinHeap()
  minheap_Point_Defense = MinHeap()
  minheap_Evasion = MinHeap()
  
  # do not shoot at destroyed ships
  valid_ships = []
  for ship in enemyFleet.ships:
    if ship.hull > 0:
      # check shields 
      if ship.shields>0:
        minheap_Shield.insert(ship.shields, ship)
      # check armor
      if ship.armor>0:
        minheap_Armor.insert(ship.armor, ship)
      # check pd
      if ship.pd>0:
        minheap_Point_Defense.insert(ship.pd, ship)
      # check evasion
      if ship.evasion>0:
        minheap_Evasion.insert(ship.evasion, ship )

      valid_ships.append(ship)      
      
  
  # minheap.minHeap()
  # shoot at a random target
  for ship in myFleet.ships:
    for weapon in ship.weapons:
      if len(valid_ships) > 0:
        # Torpedo
          if isinstance(weapon, Torpedo):
            # if isinstance(ship, Battleship): 
          
            if len(minheap_Evasion.heap_list) != 0:
              weapon.target = minheap_Evasion.delete_min()
              
            elif len(minheap_Point_Defense.heap_list) != 0:
              weapon.target = minheap_Point_Defense.delete_min()
          else:
            weapon.target= random.choice(valid_ships)
            # minheap.remove()
        # Laser
          if isinstance(weapon, Laser):
            
            if len(minheap_Armor.heap_list) != 0:
              weapon.target = minheap_Armor.delete_min()
            elif len(minheap_Armor.heap_list) == 0 and len(minheap_Shield.heap_list) != 0:
              weapon.target = minheap_Shield.delete_min()
          else:
            weapon.target= random.choice(valid_ships)
      
        # Railgun
          if isinstance(weapon, Railgun):
            
            if len(minheap_Shield.heap_list) > 20:
              weapon.target = minheap_Shield.delete_min()
    
            else:
              weapon.target= random.choice(valid_ships)
      else:
        # to prevent weapons shoot on anihalated fleets
        weapon.target = None
  
  
  
  
  
  
  for ship in myFleet.ships:
    for weapon in ship.weapons:
      if len(valid_ships) > 0:
        if len(minheap_Hull.heap_list) != 0:   
    
          weapon.target=random.choice(valid_ships)
      else:
        # to prevent weapons shoot on anihalated fleets
        weapon.target = None
  


class Node:
  def __init__(self, data, item):
    self.data=data
    self.item= item 


class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i].data < self.heap_list[i // 2].data:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2
 
    def insert(self, k, item ):
        """
        Inserts a value into the heap
        """
        N= Node(k,item)

        # Append the element to the heap
        self.heap_list.append(N)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i].data > self.heap_list[mc].data:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2].data < self.heap_list[(i*2)+1].data:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return
 
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list
 
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
 
        # Return the min value of the heap
        return root.item



      