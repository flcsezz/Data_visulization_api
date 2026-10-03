import matplotlib.pyplot as plt

squares = [1, 2, 3, 8, 10, 20, 9]

fig, ax = plt.subplots()

ax.plot(squares, linewidth=3)

ax.set_title("Random Bullshi", fontsize = 24)
ax.set_ylabel("Random", fontsize = 20)
ax.set_xlabel("Bullshi", fontsize = 20)
plt.show()
