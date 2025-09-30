import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import pyplot, patches
plt.style.use('fivethirtyeight')

import numpy as np


import os
import networkx as nx
from networkx.algorithms import bipartite
from networkx.utils import groups
import pandas as pd
from collections import defaultdict



def get_block_stats(g, attribute = 'block'):
    # assume the nodes in g have an attribute that is an int, starting at 0
    
    num_blocks = np.max(list(nx.get_node_attributes(g, attribute).values()))

    ####### edge counts
    
    # print out number of nodes in each group
    edge_counts = defaultdict(lambda: defaultdict(int))
    
    for u, v in g.edges():
        u_att = g.nodes[u][attribute]
        v_att = g.nodes[v][attribute]
        edge_counts[u_att][v_att] += 1
        if u_att != v_att:
            edge_counts[v_att][u_att] += 1
            
    df = pd.DataFrame(edge_counts).fillna(0).astype(int)
    
    # Reorder the DataFrame columns and rows to ensure all possible attribute values are present
    all_attrs = sorted(set(g.nodes[n][attribute] for n in g.nodes))
    df = df.reindex(index=all_attrs, columns=all_attrs, fill_value=0)
    # print out number of edges
    print("Edge table:")
    print(df)
    


# from https://sociograph.blogspot.com/2012/11/visualizing-adjacency-matrices-in-python.html
def draw_adjacency_matrix(G, node_order=None, partitions=[], colors=[]):
    """
    - G is a netorkx graph
    - node_order (optional) is a list of nodes, where each node in G
          appears exactly once
    - partitions is a list of node lists, where each node in G appears
          in exactly one node list
    - colors is a list of strings indicating what color each
          partition should be
    If partitions is specified, the same number of colors needs to be
    specified.
    """
    adjacency_matrix = nx.to_numpy_matrix(G, dtype=bool, nodelist=node_order)

    #Plot adjacency matrix in toned-down black and white
    fig = pyplot.figure(figsize=(5, 5)) # in inches
    pyplot.imshow(adjacency_matrix,
                  cmap="Greys",
                  interpolation="none")
    
    # The rest is just if you have sorted nodes by a partition and want to
    # highlight the module boundaries
    assert len(partitions) == len(colors)
    ax = pyplot.gca()
    for partition, color in zip(partitions, colors):
        current_idx = 0
        for module in partition:
            ax.add_patch(patches.Rectangle((current_idx, current_idx),
                                          len(module), # Width
                                          len(module), # Height
                                          facecolor="none",
                                          edgecolor=color,
                                          linewidth="1"))
            current_idx += len(module)



# function to create node colour list, given a set of blocks
def create_block_node_colors(graph, blocks):
    number_of_colors = len(blocks)    
    #colors = ["#D4FCB1", "#CDC5FC", "#FFC2C4", "#F2D140", "#BCC6C8"][:number_of_colors]
    # colormap ref:
    # https://matplotlib.org/stable/gallery/color/colormap_reference.html
    cur_cm = plt.cm.get_cmap('tab10', number_of_colors)
    colors = [matplotlib.colors.rgb2hex(cur_cm(i)) for i in range(cur_cm.N)]
    node_colors = []
    for node in graph:
        current_block_index = 0
        for block in blocks:
            if node in block:
                node_colors.append(colors[current_block_index])
                break
            current_block_index += 1
    return node_colors


# function to plot network with node colouring based on blocks
def visualize_blocks(graph, edge_alpha = 1, node_size=100):
    # assume the nodes have an attribute called 'block'
    # this next line makes a list whose entries are lists of nodes in each block
    blocks = groups(nx.get_node_attributes(graph, 'block')).values()
    node_colors = create_block_node_colors(graph, blocks)

    pos = nx.spring_layout(graph, k=0.3, iterations=50, seed=2)
    plt.subplot(3, 1, 1)

    nx.draw_networkx_nodes(
        graph,
        pos=pos,
        node_size=node_size,
        node_color=node_colors,
    )
    nx.draw_networkx_edges(
        graph,
        pos=pos,
        alpha = edge_alpha,
    )

