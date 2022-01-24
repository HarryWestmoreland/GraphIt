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

    Visited : bool
        weather the node has been visited by a traversal or not
    '''
    def __init__(self, name):
        self.name = name
        self.connected_nodes = []
        self.visited = False

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


def write_tgf_file(nodes, file_dir):
    '''
    writes a tgf file from the given nodes into the given file directory
    Parameters
    ----------
    nodes : [Node]
        set off nodes you want to write to a tgf file

    file_dire : str
        the name and directory of the tgf file you want to create
    '''
    raw_nodes = ""

    for node in nodes:
        raw_nodes += str(nodes.index(node)) + " " + node.name + "\n"

    raw_nodes += "#"

    for node in nodes:
        if len(node.connected_nodes) > 0:
            for connected_node in node.connected_nodes:
                raw_nodes += ("\n" + str(nodes.index(node)) + " " +
                str(nodes.index(connected_node[0])) + " " +
                str(connected_node[1]))

    file = open(file_dir, "x", encoding = "UTF-8")
    file.write(raw_nodes)

def depth_first_search(node, log = ""):
    '''
    performs a depth first search on the node

    Parameters
    ----------
    node : Node
        node to perform the depth first search on

    log : str
        the log of the traversal, leave blank on initial call
    '''
    if node.visited:
        return log

    node.visited = True
    if len(log) != 0:
        log += " "
    log += node.name
    for connected_node in node.connected_nodes:
        log = depth_first_search(connected_node[0],log)

    return log
