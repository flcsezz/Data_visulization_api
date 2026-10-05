from random import choice
import matplotlib.pyplot as plt

class RandomWalk():

    def __init__(self, num_points=5000):

        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y= self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        #step = direction * distance
        step = choice([-1,1]) * choice([0, 1, 2, 3, 4, 5])

        return step



            


rw = RandomWalk()
rw.fill_walk()

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(15,9), dpi = 128)

point_nums = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values,c=point_nums, cmap=plt.cm.Blues, s=1)

ax.scatter(0,0, c = "green", edgecolors=None, s=80)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c ='red', edgecolors=None, s=80)
ax.set_aspect('equal')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()


        