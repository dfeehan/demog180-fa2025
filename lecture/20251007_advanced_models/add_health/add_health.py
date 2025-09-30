import os
import networkx as nx
from networkx.algorithms import bipartite
import pandas as pd

import zipfile
import requests
import io


data_path = "data/"

def read_add_health_edges(network_id, path=data_path):
    """
    network_id : integer from 1 to 84
    
    read in the Add Health network corresponding to the given id number and
    return it as an undirected networkx object
    """

    # this file was downloaded from
    # http://moreno.ss.uci.edu/data.html#adhealth
    edge_file = os.path.join(path, "comm" + str(network_id) + ".dat")
    with open(edge_file, 'r') as f:
        edge_lines = f.readlines()
        
    network = nx.parse_edgelist(edge_lines, nodetype=int, data=[('activity_level', float)])
    
    # note that we call the to_undirected method to ensure we get an undirected network
    return(network.to_undirected())

def read_add_health_attributes_oneperrow(network_id, net, path=data_path):
    """
    Read in an Add Health attributes file that has one attribute per row
    """
    att_file = os.path.join(path, "comm" + str(network_id) + "_att.dat")
    with open(att_file, 'r') as f:
        att_lines = f.readlines()
    
    # the first 8 lines are meta-info and not actual data
    att_lines = att_lines[8:]
    
    node_races = {}
    node_grades = {}
    node_sexes = {}

    for cur_id in net.nodes():
        
        print("starting node ", cur_id)
        
        # the attributes are stored one per line for each node in sequence (race / sex / grade)
        # so line 0 is node 1's race, line 2 is node 1's sex, line 3 is node 1's grade, line 4 is node 2's race, etc
        start_idx = (cur_id-1) * 3
        this_race = str.split(g_att[start_idx])[2]
        this_sex = str.split(g_att[start_idx+1])[2]
        this_grade = str.split(g_att[start_idx+2])[2]
    
        node_races[cur_id] = this_race
        node_grades[cur_id] = this_grade
        node_sexes[cur_id] = this_sex
    
    nx.set_node_attributes(net, 'race', node_races)
    nx.set_node_attributes(net, 'grade', node_grades)
    nx.set_node_attributes(net, 'sex', node_sexes)
    
    return(net)

def read_add_health_attributes(network_id, net, path=data_path):
    """
    Read in an Add Health attributes file that has one row per node
    """
    
    # open up the attributes datafile
    att_file = os.path.join(path, "comm" + str(network_id) + "_att.dat")
    with open(att_file, 'r') as f:
        att_lines = f.readlines()
        
    # the first several lines are meta-info and not actual data;
    # the data start once we see "DATA:\n"
    header_start = att_lines.index("COLUMN LABELS:\n") + 1
    header_end = att_lines.index("DATA:\n")
    data_start = header_end + 1
    
    # build up a list that maps column index to column name
    col_defs = []
    # build up a dict that has the data for each variable
    col_data = {}
    
    for colindex, lineidx in enumerate(range(header_start, header_end)):
        # strip off the newline and the starting/ending quotes of the column name
        this_name = (str.strip(att_lines[lineidx])[1:-1]).lower()
        col_defs.append(this_name)
        # initialize the data for this column to empty dict
        col_data[this_name] = {}  
    
    att_lines = att_lines[data_start:]
    
    # for each row (corresponding to one node's data)
    # split the columns up and stick them into the appropriate
    # dict, with node id as key and attribute value as value
    for cur_id in net.nodes():
        #print('starting node ', cur_id)
        these_data = str.split(att_lines[cur_id - 1])
        
        for colidx, dat in enumerate(these_data):
            col_data[col_defs[colidx]][cur_id] = dat

    # take the data and assign it to the nodes in the graph object
    for var in col_defs:
        nx.set_node_attributes(net,  col_data[var],var)
    
    return(net)

def read_add_health_network(network_id):
    
    this_net = read_add_health_edges(network_id)
    #this_net = read_add_health_attributes(network_id, this_net)
    this_net = read_add_health_attributes(network_id, this_net)
    
    return(this_net)
