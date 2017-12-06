"""Path counting solutions."""

def count_path_recursive(m, n):
    """Count number of paths with the recursive method."""
    pass


def count_path_dynamic(m, n):
    """Count number of paths with dynamic method."""
    # create 2d array to store values
    paths = [[0 for x in range(m)] for y in range(n)]

    # set num of paths on edges to one
    for i in range(m):
        paths[i][0] = 1
    for i in range(n):
        paths[0][i] = 1

    # calculate num paths
    for i in range(1, m):
        for j in range(n):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    return paths[m - 1][n - 1]
