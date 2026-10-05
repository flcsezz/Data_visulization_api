from die import Die
import plotly.express as px

diec1 = Die()
diec2= Die()
diec3 = Die()



results = [(diec1.roll_die() * diec2.roll_die() * diec3.roll_die()) for i in range(20000)]
    

max_sides = diec1.sides + diec2.sides + diec3.sides
poss_results = range(3, max_sides + 1)
frequency = [results.count(num) for num in poss_results]



fig = px.bar(x= poss_results, y = frequency)

fig.update_layout(xaxis_dtick = 1)

fig.show()