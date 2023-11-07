class BasicCounter:
  def __init__(self, initial_count = 0):
    self.initial_count = initial_count
    self.counted = initial_count

  def __str__(self):
    return f"{str(self.initial_count)}"

  def count(self):
    self.counted += 1
   
    

  def un_count(self):
    self.counted -= 1
   

  def reset(self):
    self.counted = self.initial_count

  def set_count_to(self, val):
    self.counted = val
   

  def get_count_value(self):
    return self.counted



class LimitedCounter(BasicCounter):
  DEFAULT_MIN=0
  DEFAULT_MAX=0

  def __init__(self, min_count = DEFAULT_MIN, max_count = DEFAULT_MAX):
    super().__init__(initial_count = min_count)
    self.min_count = min_count
    self.max_count = max_count

  def is_at_min(self):
    if self.counted == self.min_count:
      return True
    else:
      return False

  def is_at_max(self):
    if self.counted == self.max_count:
      return True
    else:
      return False

  def get_min(self):
    return self.min_count

  def get_max(self):
    return self.max_count

class StoppingCounter(LimitedCounter):
  def __init__(self,min_count= LimitedCounter.DEFAULT_MIN, max_count=LimitedCounter.DEFAULT_MAX):
    super().__init__(min_count , max_count)
  
   
  def count(self):
    if self.counted == self.max_count:
      return self.counted
    else:
      super().count()

  def un_count(self):
    if self.counted == self.min_count:
      return self.counted
    else:
      super().un_count()
  
  
class RollOverCounter(LimitedCounter):
  def __init__(self, min_count = LimitedCounter.DEFAULT_MIN, max_count=LimitedCounter.DEFAULT_MAX):
    super().__init__(min_count , max_count)
  
   
  def count(self):
    if self.counted == self.max_count:
      self.counted = self.min_count
      return self.counted
    else:
      super().count()

  def un_count(self):
    if self.counted == self.min_count:
      self.counted = self.max_count
      return self.counted
    else:
      super().un_count()
  
class WarningCounter(LimitedCounter):
  def __init__(self,min_count= LimitedCounter.DEFAULT_MIN, max_count=LimitedCounter.DEFAULT_MAX):
    super().__init__(min_count , max_count)
  
   
  def count(self):
    try:
      super().count()
      if self.counted == self.max_count:
        raise CounterException(message="This value is too large, try again!")
    except:
      print("This value is too large")
  
      return self.counted
         

  def un_count(self):
    try:
      super().count()
      if self.counted == self.min_count:
        raise CounterException(message="This value is too small, try again!")
    except:
      print("This value is too small")
  
      return self.counted

class CounterException(Exception):

  def __init__(self, message = 'Counter Exception'):
    super().__init__()
    print('Exception in ' + message)

  
 

  
class ValueTooSmallError(CounterException): 
  '''This value is too small, try again!'''
  def __init__(self, message = 'Counter Exception'):
    super().__init__()
    print('Exception in ' + message)

  
      
class ValueIncorrectError(CounterException):
  '''Number error, try again!'''
  def __init__(self, message = 'Counter Exception'):
    super().__init__()
    print('Exception in ' + message)

  

class ValueTooLargeError(CounterException):
 '''This value is too large, try again!'''
 def __init__(self, message = 'Counter Exception'):
    super().__init__()
    print('Exception in ' + message)

 


  
