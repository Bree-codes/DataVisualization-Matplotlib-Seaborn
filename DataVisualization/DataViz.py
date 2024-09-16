"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [34, 45, 56, 12, 10]

plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('Weather Analysis')
plt.plot(x,y,'rD--')
#plt.plot(x, y,color='red',linewidth=3)
plt.grid()
plt.show()"""

import matplotlib.pyplot as plt

# Data for the first graph (Line 1)
x1 = [1, 2, 3, 4, 5]
y1 = [34, 45, 56, 12, 10]

# Data for the second graph (Line 2)
x2 = [1, 2, 3, 4, 5]
y2 = [20, 30, 40, 50, 60]

# Data for the third graph (Line 3)
x3 = [1, 2, 3, 4, 5]
y3 = [5, 15, 25, 35, 45]

# Plot the three graphs in the same figure
plt.plot(x1, y1, 'rD--', label='Nairobi')
plt.plot(x2, y2, 'b*:', label='Nyeri')
plt.plot(x3, y3, 'g+-', label='Kiambu')

# Add labels and a title
plt.xlabel('Days')
plt.ylabel('Temperatures')
plt.title('Multiple Graphs in One Plot')

# Show a legend to differentiate between the graphs
plt.legend()

# Show the grid
plt.grid()

# Display the graph
plt.show()
