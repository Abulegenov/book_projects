import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    fig, ax = plt.subplots(figsize=(15, 9))
    # ax.scatter(rw.x_values,rw.y_values, c = range(rw.num_points),
    #              cmap = plt.cm.Blues,edgecolors=None, s = 1)
    ax.plot(rw.x_values, rw.y_values)
    ax.set_aspect("equal")
    ax.scatter(0, 0, color="black", s=20)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color="white", s=20)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Continue plotting? y/n")
    if keep_running == "n":
        break
