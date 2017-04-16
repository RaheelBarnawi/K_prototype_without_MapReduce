import matplotlib.pyplot as plt
# -----------d-squezeer
'''''
x_axis1=[100,200,300,400,500,600,700,800,900,1000]
y_axis1=[0.035,0.065,0.075,0.1158,0.124,0.137,0.191,0.199,0.216,0.375]
plt.plot (x_axis1,y_axis1)
plt.title(" The execution time versus different number of tuples.")
plt.xlabel(" The number of tuples in 1000")
plt.ylabel("Exection Time in second")
plt.show()
# -----------k-prototype--------
'''''

x_axis=[100,200,300,400,500,600,700,800,900,1000]
y_axis=[10.46,25.86,42.05,59.79,78.17,100.77,121.30,147.50,175.44,201]

plt.plot (x_axis,y_axis,'bs')
plt.title(" The execution time versus different number of tuples.")
plt.xlabel(" The number of tuples in 1000")
plt.ylabel("Exection Time in second")

plt.show()
