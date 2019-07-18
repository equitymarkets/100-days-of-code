#Day 88: Continuing with functions to work on modules
#
#
import matplotlib.pyplot as plt
import Fib

data = Fib.Fib_Func()

print(data)


x = len(data)
xaxis = []

for x in range(x,0,-1):
    xaxis.append(x)

x_axis = sorted(xaxis)

plt.figure("D/C Plotted")
plt.plot(x_axis, data, color="darkorchid")
plt.xlabel("Picks")
plt.ylabel("D/C")
plt.show()
