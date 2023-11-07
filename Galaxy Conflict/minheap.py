"""
Min Heap Implementation in Python
"""
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
 
    def insert(self, k, item):
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
            return 'Empty heap'
 
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
"""
Driver program
"""
# my_heap = MinHeap()
# my_heap.insert(5)
# my_heap.insert(6)
# my_heap.insert(7)
# my_heap.insert(9)
# my_heap.insert(13)
# my_heap.insert(11)
# my_heap.insert(10)


# for i in my_heap.heap_list:
#   print(my_heap.delete_min())
class Node:
  def __init__(self, data, item):
    self.data=data
    self.item= item 


class Car:
  def __init__(self, type, number_of_wheels ):
    self.type = type
    self.n = number_of_wheels 

  # def __str__(self):
  #   s = 'hi'
  #   return s

f= Car("a",5)
a= Car("b",3)
t= Car("a",17)
l= Car("a",10)
fu= Car("a",84)
b = Car('a', 19)
c = Car('a', 6)
d = Car('a', 22)
e = Car('a', 9)


minheap= MinHeap()

minheap.insert(f.n, f)
minheap.insert(a.n,a)
minheap.insert(t.n,t)
minheap.insert(l.n,l)
minheap.insert(fu.n,fu)
minheap.insert(b.n,fu)
minheap.insert(c.n,c)
minheap.insert(d.n, d)
minheap.insert(e.n, e)

for i in minheap.heap_list[:-1]:
  print(minheap.delete_min())
  # print(minheap)

