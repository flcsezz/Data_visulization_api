import matplotlib.pyplot as plt

input = [1, 2, 3, 4, 5, 6, 7]
squares = [1, 4, 9, 16, 25, 36, 49]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(input, squares, s=100)

#ax.plot(input, squares, linewidth=4)

ax.set_title("Random Bullshi", fontsize = 24)
ax.set_ylabel("Random", fontsize = 20)
ax.set_xlabel("Bullshi", fontsize = 20)

#set size of tick lables 
ax.tick_params(labelsize=14)
plt.show()
