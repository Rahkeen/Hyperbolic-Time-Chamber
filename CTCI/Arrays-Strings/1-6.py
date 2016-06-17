from pprint import pprint

def rotate_90(matrix):
    N = len(matrix)
    layers = N/2
    for layer in xrange(layers):
        for i in xrange(layer, N-layer-1):
            # Swap the 4 values
            temp = matrix[i][layer] # top
            matrix[i][layer] = matrix[layer][N-i-1] # top = left
            matrix[layer][N-i-1] = matrix[N-i-1][N-layer-1] # left = bottom
            matrix[N-i-1][N-layer-1] = matrix[N-layer-1][i] # bottom = right
            matrix[N-layer-1][i] = temp

# matrix = [[1,4,7],[2,5,8],[3,6,9]]
matrix = [[1,3],[2,4]]
pprint(matrix)
rotate_90(matrix)
pprint(matrix)
