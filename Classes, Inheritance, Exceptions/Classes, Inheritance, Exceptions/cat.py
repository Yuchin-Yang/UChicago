from pet import *
class Cat(Pet):
  def __init__(self, name, age):
    super().__init__(name, age)
  def __str__(self):
      s = super().__str__()
      if self._activity == Pet.WALKING:
        return "Walk? Dude, seriously?\n" + s
      if self._activity == Pet.EATING:
        return "Lasagna, please.\n" + s
      if self._activity == Pet.SLEEPING:
        return "Yes. I need 23 hours of this each day!\n" + s
      return s
  