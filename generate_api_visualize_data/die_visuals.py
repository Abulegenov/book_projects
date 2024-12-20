import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = []
for i in range(50_000):
    results.append(die_1.roll() + die_2.roll())

# Count the results of dice rolling
frequencies = {}
for i in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequencies[i] = results.count(i)

title = "Results of rolling One D6 Die and One D10 Die 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=frequencies.keys(), y=frequencies.values(), title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.write_html("dice_visual_d6d10_50000.html")
# fig.show()
