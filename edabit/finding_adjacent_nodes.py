#https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def is_adjacent(matrix, node1, node2):
    if matrix[node1][node2]:
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
    matrix2 = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
    is_adjacent(matrix2, 3,2)


"""
Undirected graph has nodes (vertices) and edges.
Edges do not have any direction to them and therefore are unordered pairs. 
Unidrected graph can be represented as a VxV adjacency matrix, where each position is a node, and the value at that position indicates if there's an edge between those two nodes.

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

if matrix[i][j] is 0, there is no connection between those nodes.
if matrix[i][j] is 1, there is a connection between those nodes.

"""
