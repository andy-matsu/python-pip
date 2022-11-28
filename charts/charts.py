import matplotlib.pyplot as plt
def generate_pie_chart():
    label = ["A", "B", "C"]
    values = [250, 50, 170]

    fig, ax = plt.subplots()
    ax.pie(values, labels=label)
    plt.savefig("pie.png")
    plt.close()