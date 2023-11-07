# Python3 implementation of Min Heap

# Python3 implementation of Min Heap

import sys

class MinHeap:
  
  def __init__(self, maxsize, Car):
    self.maxsize = maxsize
    self.size = 0
    self.Heap = [0]*(self.maxsize + 1)
    temp=Car
    temp.n=-1 * sys.maxsize
    self.Heap[0] = temp.n
    self.FRONT = 1
  
  # Function to return the position of
  # parent for the node currently
  # at pos
  def parent(self, pos):
    return pos//2
  
  # Function to return the position of
  # the left child for the node currently
  # at pos
  def leftChild(self, pos):
    return 2 * pos
  
  # Function to return the position of
  # the right child for the node currently
  # at pos
  def rightChild(self, pos):
    return (2 * pos) + 1
  
  # Function that returns true if the passed
  # node is a leaf node
  def isLeaf(self, pos):
    return (pos*2).__gt__(self.size)
  
  # Function to swap two nodes of the heap
  def swap(self, fpos, spos):
    self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
  
  # Function to heapify the node at pos
  def minHeapify(self, pos):
    
    # If the node is a non-leaf node and greater
    # than any of its child
    if not self.isLeaf(pos):
      if ((self.Heap[pos]).__gt__(self.Heap[self.leftChild(pos)])) or ((self.Heap[pos]).__gt__(self.Heap[self.rightChild(pos)])):
    
    # Swap with the left child and heapify
    # the left child
        if (self.Heap[self.leftChild(pos)]).__lt__(self.Heap[self.rightChild(pos)]):
          self.swap(pos, self.leftChild(pos))
          self.minHeapify(self.leftChild(pos))
      
    # Swap with the right child and heapify
    # the right child
        else:
          self.swap(pos, self.rightChild(pos))
          self.minHeapify(self.rightChild(pos))
    
  # Function to insert a node into the heap
  def insert(self, element):
    if (self.size).__ge__(self.maxsize):
      return
    self.size+= 1
    self.Heap[self.size] = element
    
    current = self.size
    
    # while (self.Heap[current]).__lt__(self.Heap[self.parent(current)])==True:
    #   self.swap(current, self.parent(current))
    #   current = self.parent(current)

    while (self.Heap[current]).__lt__(self.Heap[self.parent(current)])==True:
      self.swap(current, self.parent(current))
      current = self.parent(current)
    
  # Function to print the contents of the heap
  def Print(self):
    
  
    for i in range(1, (self.size//2)+1):
      print(" PARENT : "+ str(self.Heap[i].n)+" LEFT CHILD : "+
            str(self.Heap[2 * i].n)+" RIGHT CHILD : "+
            str(self.Heap[2 * i + 1].n))
   
  
  # Function to build the min heap using
  # the minHeapify function
  def minHeap(self):
  
    for pos in range(self.size//2, 0, -1):
      self.minHeapify(pos)
  
  # Function to remove and return the minimum
  # element from the heap
  def remove(self):
  
    popped = self.Heap[self.FRONT]
    self.Heap[self.FRONT] = self.Heap[self.size]
    self.size-= 1
    self.minHeapify(self.FRONT)

    return popped

  def __lt__(self, other):
    # print( type(self), type (other))
    if not isinstance(self,int) and not isinstance(other,int) :
      if self.n < other.n:
        return True
      else:
        return False
    elif isinstance(self,int) and not isinstance(other,int):
      if self < other.n:
        return True
      else:
        return False
    elif not isinstance(self,int) and isinstance(other,int):
      if self.n < other:
        return True
      else:
        return False
    elif self < other:
      return True 
    else:
      return False
  def __gt__(self, other):
    if not isinstance(self,int) and not isinstance(other,int) :
      if self.n > other.n:
        return True
      else:
        return False
    elif isinstance(self,int) and not isinstance(other,int):
      if self > other.n:
        return True
      else:
        return False
    elif not isinstance(self,int) and isinstance(other,int):
      if self.n > other:
        return True
      else:
        return False
    elif self > other:
      return True 
    else:
      return False
  def __ge__(self, other):
    if not isinstance(self,int) and not isinstance(other,int) :
      if self.n >= other.n:
        return True
      else:
        return False
    elif isinstance(self,int) and not isinstance(other,int):
      if self >= other.n:
        return True
      else:
        return False
    elif not isinstance(self,int) and isinstance(other,int):
      if self.n >= other:
        return True
      else:
        return False
    elif self >= other:
        return True 
    else:
        return False
    
  def __le__(self, other):
    if not isinstance(self,int) and not isinstance(other,int) :
      if self.n <= other.n:
        return True
      else:
        return False
    elif isinstance(self,int) and not isinstance(other,int):
      if self <= other.n:
        return True
      else:
        return False
    elif not isinstance(self,int) and isinstance(other,int):
      if self.n <= other:
        return True
      else:
        return False
    elif self <= other:
      return True 
    else:
      return False

# Driver Code
# if __name__ == "__main__":
	
# 	print('The minHeap is ')
# 	minHeap = MinHeap(15)
# 	minHeap.insert(5)
# 	minHeap.insert(3)
# 	minHeap.insert(17)
# 	minHeap.insert(10)
# 	minHeap.insert(84)
# 	minHeap.insert(19)
# 	minHeap.insert(6)
# 	minHeap.insert(22)
# 	minHeap.insert(9)
# 	minHeap.minHeap()

# 	minHeap.Print()
# 	print("The Min val is " + str(minHeap.remove()))

# Driver Code


  
  
	
# print('The minHeap is ')
# minHeap = MinHeap(15)
# minHeap.insert(5)
# minHeap.insert(3)
# minHeap.insert(17)
# minHeap.insert(10)
# minHeap.insert(84)
# minHeap.insert(19)
# minHeap.insert(6)
# minHeap.insert(22)
# minHeap.insert(9)

# minHeap.minHeap()
# print(minHeap.Heap[1])
# minHeap.Print()
# print("The Min val is " + str(minHeap.remove()))



class Car:
  def __init__(self, type, number_of_wheels ):
    self.type = type
    self.n = number_of_wheels 

f= Car("a",5)
a= Car("b",3)
t= Car("a",17)
l= Car("a",10)
fu= Car("a",84)
b = Car('a', 19)
c = Car('a', 6)
d = Car('a', 22)
e = Car('a', 9)

# print(f.n)

minheap= MinHeap(10,f)

minheap.insert(f)
minheap.insert(a)
minheap.insert(t)
minheap.insert(l)
minheap.insert(fu)
minheap.insert(b)
minheap.insert(c)
minheap.insert(d)
minheap.insert(e)
minheap.minHeap()
print('x')
minheap.Print()
# for i in minheap.Heap[1:]:
#   print(i)
# print(minheap.Heap)
# minheap.Print()