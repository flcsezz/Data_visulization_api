from die import Die
import plotly.express as px

dice1 = Die()
dice2 = Die(10)
result = []

for i in range(50_000):
    result.append(dice1.roll_die() + dice2.roll_die())

max_sides= dice1.sides + dice2.sides
poss_result = range(2, max_sides+1)
frequencies = []

for i in poss_result:
    frequencies.append(result.count(i))

title = "Result of rolling Two D6 and D10 50_000 times"
lables = {'x' : 'Result', 'y' : 'Frequency of result'}
fig = px.bar(x=poss_result, y=frequencies, title=title, labels=lables)

fig.update_layout(xaxis_dtick=1)

fig.write_html('dices.xhtml')