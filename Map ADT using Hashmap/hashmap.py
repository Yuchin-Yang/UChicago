#Nahom Ayele, Yuqin Yang
"""Implementation of the Map ADT using closed hashing and a probe with 
double hashing.

This is an incomplete file, students will have to fill in the missing
parts to make the hash map work correctly.
"""

class HashMap :
  """ A closed hashing (one key per slot) with a double hashing
      probe (one hash function that maps into two different capacities)
  
  Attributes:
    CAP; int; max capacity of the hash table.
    _array; arraylist of MapArray items; element is None if nothing stored; 
            to store data; has max capacity CAP. 
    _size; int; how many items are in the array.
    _collisions; int; number of items with same hash value.
  """

  def __init__( self, capacity):                                     
    """Creates an empty map instance.
    Parameters:
      capacity; int; number of slots available in array."""

    # Define the size of the table
    self.CAP = capacity

    # Create the data storage (empty hash table)
    self._array = [None] * self.CAP

    # how many items in the array
    self._size = 0
    
    # how many collisions so far
    self._collisions = 0
      
  def __len__( self ):
    """Returns the number of entries in the map."""
    return self._size

  def _hash1( self, key ):                               
    """The main hash function for mapping keys to table entries.
    Parameter: 
      key; hashable key.
    Return:
      int; value from hash function."""
    return abs( hash( key ) ) % len( self._array )
  
  def _hash2( self, key ):
    """ The second hash function used for backup.
    Parameter: 
      key; hashable key.
    Return:
      int; value from hash function."""
    
    return 1 + abs( hash( key ) ) % ( len( self._array ) - 2 )    
  
  def add( self, key, value ):
    """ If the key does not exist, adds a new entry to the map.
        If the key exists, update its value.
      Paramters:
        key; any valid value to use in hashfunciton.
        value; to store in hashmap.
      Return:
        None
    """
    slot, contents = self._lookup(self._hash1, key)

    if slot is not None:
        if contents is not None:
            self._array[slot].value = value 
        else:
            self._array[slot] = _MapEntry(key, value)
            self._size +=1
    else:
        self._collisions += 1
        slot, contents = self._lookup(self._hash2, key)
        if slot is not None: 
            if contents is not None:
                self._array[slot].value = value 
            else:
                self._array[slot] = _MapEntry(key, value)
                self._size +=1 
     
    
  
      
  def peek( self, key ):
    """ Returns the value associated with the key or returns None.
    Parameters:
      key; key to look up in hashmap.
    Return:
      value associated with key or None"""
    slot,contents = self._lookup(self._hash1, key)
    if contents == None:
      slot,contents = self._lookup(self._hash2, key)
      
    if contents == None:
      return None
    else:
      return contents.value

  def _lookup(self, hashFunction, key):
    """ Parameters:
        hashFunciton, function to use;
        key; key to look up using hashFunction;
      Returns:
        a tuple with two values.
          If the slot it should occupy contains the matching key, it 
            returns (slot, contents).
          If the slot it should occupy is empty it returns (slot,None).
          If the slot it should occupy has other contents, it returns 
          (None,None). """ 
    # Compute the slot.
    slot = hashFunction( key )
    contents = self._array[slot]
    if contents == None:
      return slot, None
    elif contents.key != key:
      return None, None 
    else:
      return slot, contents
      
      

    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    
    
  def __iter__(self):
    """ Return: an iterator for the hashmap. """

   
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    return  _MapIterator(self._array)
  
  def printStats( self ):
    """Print the number of items in the table and the total
    number of collisions due to insertion."""
    print( 'Entry count : ', self._size )
    print( 'Collision count : ', self._collisions )

  def remove( self, key ):
    """ Removes the entry associated with the key.
        If the key is not in the map, does nothing. 
    Parameters: 
      key; hashable key value
    Return:
      None
    """
    (slot, content) = self._lookup(self._hash1, key)
    (slot2, content2) = self._lookup(self._hash2, key)

    if slot is not None:
      self._array[slot]= None
      self._size -= 1
      
    elif slot2 is not None:
      self._array[slot2]=  None
      self._size -= 1
      
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    

# Storage class for holding a key/value pair.   
class _MapEntry :                       

  """
  Storage class for holding a key/value pair. 
    Attributes:
      key; hashable key.
      value; 
  """
  def __init__( self, key, value ):
    """Create the entry with key and value """
    self.key = key
    self.value = value 
   
  
  def __eq__( self, other ):
    """Overload __eq__ so key, value pairs can be compared using '=='.
    Parameters:
      self; instance of the _MapEntry class.
      other; instance of the _MapEntry class."""
    if other == None:
      return False
    return ( self.key == other.key and self.value == other.value )

## STUDENTS WILL PUT AN ITERATOR CLASS HERE.
class _MapIterator:
    def __init__(self, array):
      self._array = array
      self._index = 0
    
    def __next__(self):
        while self._index < len(self._array):
            contents = self._array[self._index]
            self._index +=1 

            if contents is not None:
                return contents.key
        raise StopIteration()

    def __iter__(self):
        return self._array[self._index]
