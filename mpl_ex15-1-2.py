import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.plot(x_values,y_values, color = 'Red', linewidth = 3)

ax.set_xlim(0, 5100)
ax.set_ylim(bottom=0)
ax.set_title('Cubes', fontsize = 24)
ax.set_xlabel('Numbers', fontsize=10)
ax.set_ylabel('Cubes', fontsize = 10)

plt.show()