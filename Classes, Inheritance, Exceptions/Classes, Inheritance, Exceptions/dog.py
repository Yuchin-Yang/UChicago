from pet import *
class Dog(Pet):
  def __init__(self, name, age):
    super().__init__(name, age)

  def __str__(self):
    s = super().__str__()
    if self._activity == Pet.WALKING:
      return "Walk?!?! Oh boy oh boy!!! Pant! Pant! Pant!\n" + s
    if self._activity == Pet.EATING:
      return "Begging for food... kibbles and bits please.\n" + s
    if self._activity == Pet.SLEEPING:
      return "Zzzzzz (drooling)...\n" + s
    return s