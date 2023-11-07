# example Taken from 
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

# importing the required module
import matplotlib.pyplot as plt

file = open("outru")
lines = file.read().splitlines()

x = []
y = []

for line in lines:
  data = line.split()
  # x axis values
  x.append(int(data[0]))

  # corresponding y axis values
  y.append(int(data[1]))

file.close()
# plotting the points 
plt.plot(x, y, label = "Random")
  
file = open("outsu")
lines = file.read().splitlines()

x = []
y = []

for line in lines:
  data = line.split()
  # x axis values
  x.append(int(data[0]))

  # corresponding y axis values
  y.append(int(data[1]))


file.close()
# plotting the points 
plt.plot(x, y, label = "Sorted")

# naming the x axis
plt.xlabel('n')
# naming the y axis
plt.ylabel('Number of Comparisons')
  
# giving a title to my graph
plt.title('Quicksort Performance (Unmodified)')

# show a legend
plt.legend()
  
# function to show the plot
plt.show()