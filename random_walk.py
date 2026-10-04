from random import choice

import matplotlib.pyplot as plt

class Random_Walk():

    def __init__(self, num_points=5000):

        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            #step = direction * distance
            x_step = choice([-1,1]) * choice([0, 1, 2, 3, 4])
            y_step = choice ([-1, 1]) * choice([0, 1, 2, 3, 4])

            if x_step==0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


rw = Random_Walk()
rw.fill_walk()

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=10)
ax.set_aspect('equal')

plt.show()


        