import matplotlib.pyplot as plt

y_values = range(1,1001)
x_values = [x**2 for x in y_values]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(y_values, x_values, c= y_values, cmap=plt.cm.Reds, s=10)

ax.axis([0, 1100, 0, 1_100_000])

#ax.plot(input, squares, linewidth=4)

ax.set_title("Random Bullshi", fontsize = 24)
ax.set_ylabel("Random", fontsize = 20)
ax.set_xlabel("Bullshi", fontsize = 20)

#set size of tick lables 
ax.tick_params(labelsize=14)

plt.savefig('Random_bs.png')
plt.show()