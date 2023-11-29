import matplotlib.pyplot as plt
import numpy as np

def plot_bar_chart():
    # Sample data from the provided bar chart image
    labels = ['saveInfo', 'deleteInfo', 'queryPK', 'queryDP', 'updateDP']
    four_nodes = [50, 120, 40, 30, 130]
    six_nodes = [60, 110, 50, 40, 120]
    eight_nodes = [70, 100, 60, 50, 110]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, four_nodes, width, label='4 edge nodes', hatch='/')
    rects2 = ax.bar(x, six_nodes, width, label='6 edge nodes', hatch='\\')
    rects3 = ax.bar(x + width, eight_nodes, width, label='8 edge nodes', hatch='|')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Operation time (ms)')
    ax.set_title('Smart contract APIs')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()

# To use this function, simply call it
plot_bar_chart()
