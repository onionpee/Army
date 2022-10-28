import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv("army.csv", index_col=2)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

def scatter(label, color):
    data = table.loc[label]
    ax.scatter(data["weight"],data["height"], c=color, label=label)

scatter("1st","red")
scatter("2nd","orange")
scatter("3rd","yellow")
scatter("4th","green")
scatter("5th","blue")
scatter("6th","purple")

ax.legend()
plt.savefig("ic_rank.png")