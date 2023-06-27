import networkx as nx
from matplotlib import pyplot as plt


def plotgr(lst):
    # Initialize graph
    g1 = nx.Graph()
    # Add edges
    g1.add_edges_from(lst)
    # Plot in file
    plt.tight_layout(pad=2)
    nx.draw_networkx(g1, arrows=True)
    plt.savefig("g1.png", format="PNG")
    print("Plot done")
