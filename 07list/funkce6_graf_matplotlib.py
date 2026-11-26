import math
import matplotlib.pyplot as plt
xs = []
ys1 = []
ys2 = []

for i in range(-50, 51):
    x = i / 10
    xs.append(x)
    ys1.append(x * x)
    ys2.append(10 / (1 + math.exp(-x)))

plt.plot(xs, ys1, label="Parabola (x*x)")
plt.plot(xs, ys2, label="Sigmoid")
plt.title("Porovnání dvou křivek")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend() 
plt.show()