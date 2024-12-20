from calendar import c
import matplotlib.pyplot as plt
import random

squares = [1, 4, 9, 16, 25]
squares_2 = [(3 + i) ** 2 for i in range(5)]
input_values = [i + 1 for i in range(5)]
print(input_values)
# for i in range(5):
style = random.choice(plt.style.available)
# print(style)
# print(plt.style.available)
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# ax.plot(input_values, squares_2, linewidth = 3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared Value", fontsize=14)

ax.tick_params(labelsize=14)

ax.scatter(3, 5, s=200, color="black")
ax.scatter(input_values, squares_2, c=squares_2, s=200, cmap=plt.cm.Blues)
# ax.axis([0,10,0,100])
# plt.show()
plt.savefig("squares_plot.png", bbox_inches="tight")
