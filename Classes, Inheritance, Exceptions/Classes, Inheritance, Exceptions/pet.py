

class Pet:
  '''The following constants define pet activities'''
  UNKNOWN = 0
  WALKING = 1
  EATING = 2
  SLEEPING = 3
  def __init__(self, name, age):
    self._age = age
    self._name = name
    self._activity = Pet.UNKNOWN
  
  def __str__(self):
    if self._activity == Pet.UNKNOWN: 
      return f"{str(self._name)} (age: {str(self._age)}) is doing UNKNOWN"
    if self._activity == Pet.WALKING: 
      return f"{str(self._name)} (age: {str(self._age)}) is WALKING"
    if self._activity == Pet.EATING: 
      return f"{str(self._name)} (age: {str(self._age)}) is EATING"
    if self._activity == Pet.SLEEPING: 
      return f"{str(self._name)} (age:{str(self._age)}) is SLEEPING"

    
  def walk(self):
    self._activity=Pet.WALKING
    return self._activity

  def eat(self):
    self._activity=Pet.EATING
    return self._activity
  def sleep(self):
    self._activity=Pet.SLEEPING
    return self._activity
    





