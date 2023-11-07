import random
try:
  ri = random.randint(0, 2)
  print('random value : ' + str(ri))
  if ri == 0:
    infinity = 1/0
    raise ZeroDivisionError
  elif ri == 1:
    raise ValueError("Message")
  elif ri == 2:
    raise ValueError # Without message
except ZeroDivisionError:
  print('Divided by zero')
except ValueError as valerr:
  print("Value error: " + str(valerr))

except: # Any other exception
  print('Unknown error')
finally: # Optional
  pass # Clean up
class CustomValueError(ValueError): pass # Custom exception

try:
  raise CustomValueError
  raise TypeError
except (ValueError, TypeError): # Value error catches custom, a derived class, as well
  pass                        # A tuple catches multiple exception classes