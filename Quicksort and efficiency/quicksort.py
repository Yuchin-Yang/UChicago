""" Quicksort and Efficiency lab, CSCI 204 """
comps = 0

def sort( myList ):
  """ 
  Sort the given list using the quicksort algorithm. 
  Also returns the comparison count.
  """
  global comps
  comps = 0
  quicksort( myList, 0, len(myList) - 1 )
  return comps

def quicksort( myList, first, last ):
  """ 
  Sort the given list using the quicksort algorithm. 
  Sorts the portion of the list between the 
  first and last indices (inclusive).
  """
  
  # base case: done when the indices touch or overlap.
  if first >= last:
    return

  # recursive case: partition the myList and recurse on both sides
  split = partition( myList, first, last )
  quicksort( myList, first, split-1 )
  quicksort( myList, split+1, last )

def partition( myList, first, last ):
    """ Partition the given list into two parts. The first part will
        contain smaller values, the second part will contain larger values.
        There will be a pivot value between them. Partitions the
        portion of the list between the first and last indices (inclusive).
        Return the index of the pivot element.
    """
    # We will track to index of the last number we found for the 'small' side.
    # We starts out with: "pivot, smalls, lastSmall, larges, unchecked".
    # Every time we find a small value in the unchecked section, we swap it
    # with the first large and label it as the new lastSmall.
    # In the end, we will have: "pivot, smalls, lastSmall, larges"
    # and we will swap the pivot and the lastSmall so the order is
    # "smalls, pivot, larges".
    
    lastSmall = first
    pivot = myList[ first ]
    global comps

    # Seperate the list into "pivot, smalls, lastSmall, larges".
    for i in range( first+1, last+1 ): # first+1 ... last (inclusive)
        # if myList[i] is small, swap it onto the 'small' side.
        if myList[ i ] <= pivot: # KEY COMP
            lastSmall = lastSmall + 1
            swap( myList, lastSmall, i )
        comps+=1
    
    # Swap the pivot with lastSmall to get "smalls, pivot, larges".
    swap( myList, first, lastSmall )

    # Return the location of the pivot
    return lastSmall

def swap( myList, first, second ):
    """ Swap the items at the first and second indices in the given list. Assumes the indices are legal and occupied in the list.
    """
    tmp = myList[ first ]
    myList[ first ] = myList[ second ]
    myList[ second ] = tmp






"""copies"""


def sortm( myList ):
  """ 
  Sort the given list using the quicksort algorithm. 
  Also returns the comparison count.
  """
  global comps
  comps = 0
  quicksortm( myList, 0, len(myList) - 1 )
  return comps

def quicksortm( myList, first, last ):
  """ 
  Sort the given list using the quicksort algorithm. 
  Sorts the portion of the list between the 
  first and last indices (inclusive).
  """
  
  # base case: done when the indices touch or overlap.
  if first >= last:
    return

  # recursive case: partition the myList and recurse on both sides
  split = partitionm( myList, first, last )
  quicksortm( myList, first, split-1 )
  quicksortm( myList, split+1, last )

def partitionm( myList, first, last ):
    """ Partition the given list into two parts. The first part will
        contain smaller values, the second part will contain larger values.
        There will be a pivot value between them. Partitions the
        portion of the list between the first and last indices (inclusive).
        Return the index of the pivot element.
    """
    global comps
    # We will track to index of the last number we found for the 'small' side.
    # We starts out with: "pivot, smalls, lastSmall, larges, unchecked".
    # Every time we find a small value in the unchecked section, we swap it
    # with the first large and label it as the new lastSmall.
    # In the end, we will have: "pivot, smalls, lastSmall, larges"
    # and we will swap the pivot and the lastSmall so the order is
    # "smalls, pivot, larges".
    middle=(first + last) //2
    
    lastSmall = first
    last = last
    middle = (first + last) // 2
    if myList[lastSmall] < myList[last]:
      comps+=1
      if myList[lastSmall] < myList[middle]:
        comps+=1
        if myList[middle] < myList[last]:
          comps+=1
          swap(myList, middle, lastSmall)
        else:
          swap(myList, last, lastSmall)
      else:
        swap(myList, lastSmall, lastSmall)

    if myList[lastSmall] > myList[last]:
      comps+=1
      if myList[lastSmall] > myList[middle]:
        comps+=1
        if myList[middle] > myList[last]:
          comps+=1
          swap(myList, middle, lastSmall)
        else:
          swap(myList, lastSmall, last)
      else:
        swap(myList, lastSmall, lastSmall)
        
    pivot = myList[ first ]
    

    # Seperate the list into "pivot, smalls, lastSmall, larges".
    for i in range( first+1, last+1 ): # first+1 ... last (inclusive)
        # if myList[i] is small, swap it onto the 'small' side.
        if myList[ i ] <= pivot: # KEY COMP
            lastSmall = lastSmall + 1
            swap( myList, lastSmall, i )
        comps+=1
    
    # Swap the pivot with lastSmall to get "smalls, pivot, larges".
    swap( myList, first, lastSmall )

    # Return the location of the pivot
    return lastSmall
