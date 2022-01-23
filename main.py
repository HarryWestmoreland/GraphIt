'''This is the main module for the Project'''
class Node:
    '''
    This class models a Node within a Graph

    Parameters
    ----------
    name : str
        Name of the Node.

    connected_nodes : List[[Node, int]]
        List of Nodes that this Node is connected to and the length of the connection
    '''
    def __init__(self, name):
        self.name = name
        self.connected_nodes = []

    def connect_node(self, node, length = 1):
        '''
        adds node to connected_nodes with the connection length

        Parameters
        ----------
        node : Node
            the Node you want to connect to this Node

        length : int, Defaults to 1
            the length of the connection
        '''
        self.connected_nodes.append([node, length])


def read_tgf_file(file_dir):
    '''
    reads a tgf file and returns a set of Nodes

    Parameters
    ----------
    file_dir : str
        the name and directory of the file

    Returns
    -------
    nodes : [Node]
        a set off nodes described by the tgf file
    '''

    file = open(file_dir, "r",encoding = "UTF-8")
    file = file.read()
    file = file.split("#")

    raw_nodes = file[0].splitlines()
    raw_edges = file[1].splitlines()

    del raw_edges[0]

    nodes = []
    for node in raw_nodes:
        nodes.append(Node(node[2:]))

    for edge in raw_edges:
        edge_info = edge.split(" ")
        nodes[int(edge_info[0])].connect_node(nodes[int(edge_info[1])],int(edge_info[2]))

    return nodes
