import matplotlib.pyplot as plt
import math

x_axis_values = [1,3,5]
y_axis_values = [2,3.5,6]

plt.plot([1,5,2,8,3])
plt.show()
#plt.savefig("plot8.png")


print("plot x-y line and save file to plot.png")
plt.plot(x_axis_values,y_axis_values)
plt.show()
#plt.savefig('plot.png')
print("saved files!")