from die import Die

dice = Die()

result = []

for i in range(1000):
    result.append(dice.roll_die())

poss_result = range(1, dice.sides+1)

for i in poss_result:
    frequencies = result.count(i)
    print(f"{i} appeared {frequencies} Time")