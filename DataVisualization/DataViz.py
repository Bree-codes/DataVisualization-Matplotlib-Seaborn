import matplotlib.pyplot as plt

#Line Plot
x = [1, 2, 3, 4, 5]
y = [34, 45, 56, 12, 10]

plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('Weather Analysis')
plt.plot(x,y,'rD--')
#plt.plot(x, y,color='red',line width=3)
plt.grid()
plt.show()

#Line Plot
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

#Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 8, 5]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.grid()
plt.show()

#Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y, color='black')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter Plot Example')
plt.grid()
plt.show()

#Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9]

plt.hist(data, bins=5, color='grey', edgecolor='black')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.grid()
plt.show()

#Pie Chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()

#Box Plot
data = [7, 8, 5, 9, 11, 13, 5, 6, 10, 12, 15, 13, 9]

plt.boxplot(data)
plt.ylabel('Values')
plt.title('Box Plot Example')
plt.show()


