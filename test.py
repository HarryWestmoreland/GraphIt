'''This is a test Module for the Project'''
import os
from main import read_tgf_file, write_tgf_file, Node

def test_example_read():
    '''Tests read_tgf_file on an example file'''
    nodes = read_tgf_file("example.tgf")
    assert nodes[1].name == "Birmingham"
    assert nodes[1].connected_nodes[0][0].name == "Manchester"
    assert nodes[1].connected_nodes[0][1] == 8
    assert nodes[1].connected_nodes[1][0].name == "Liverpool"

def test_connect_node():
    '''tests node connection functionality'''
    node_a = Node("node_a")
    node_b = Node("node_b")

    node_a.connect_node(node_b,5)

    assert node_a.connected_nodes[0][0] == node_b
    assert node_a.connected_nodes[0][1] == 5

def test_example_write():
    '''tests write_tgf_file functionality'''
    nodes = read_tgf_file("example.tgf")
    write_tgf_file(nodes,"wroteFile.tgf")

    read_file = open("example.tgf","r",encoding = "UTF-8").read()
    wrote_file = open("wroteFile.tgf","r",encoding = "UTF-8").read()

    os.remove("wroteFile.tgf")
    assert read_file == wrote_file
