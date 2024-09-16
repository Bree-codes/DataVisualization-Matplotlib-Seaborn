import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [34, 45, 56, 12, 10]

plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('Weather Analysis')
plt.plot(x, y,color='red',linewidth=3)
plt.show()

