'''This is a test Module for the Project'''
from main import read_tgf_file

def test_example_read():
    '''Tests read_tgf_file on an example file'''
    nodes = read_tgf_file("example.tgf")
    assert nodes[1].name == "Birmingham"
    assert nodes[1].connected_nodes[0][0].name == "Manchester"
    assert nodes[1].connected_nodes[0][1] == 8
    assert nodes[1].connected_nodes[1][0].name == "Liverpool"
    assert nodes[1].connected_nodes[1][1] == 9
