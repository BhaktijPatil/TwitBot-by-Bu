import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def set_default_style():
    sns.set_style("darkgrid")
    sns.set(rc={'axes.facecolor': 'lightsteelblue', 'figure.facecolor': 'lightsteelblue'})


def create_basic_bar_graph(df, axes_labels, axes, title):
    graph = sns.catplot(data=df, kind="bar", x=axes[0], y=axes[1], palette=sns.color_palette("Paired", 9))
    graph.set_axis_labels(axes_labels[0], axes_labels[1])
    graph.set(title=title)
    return graph


def save_fig(save_loc):
    plt.savefig(save_loc)


def show_plt():
    plt.show()


def create_ukraine_war_trend_bar_graph(ukraine_df, axes_labels, axes, title, save_loc):
    set_default_style()
    graph = create_basic_bar_graph(ukraine_df, axes_labels, axes, title)
    # Donot show scientific notation for y-axis
    plt.ticklabel_format(style='plain', axis='y')
    # Prevent cropping of graph
    plt.tight_layout()
    # Set axes rotation
    graph.set_yticklabels(rotation=30)
    graph.set_xticklabels(rotation=30)
    # Set Upper & Lower bounds for y-axis
    axes = graph.axes
    axes[0, 0].set_ylim(600000, 1600000)
    save_fig(save_loc)
    # show_plt()
