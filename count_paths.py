"""Path counting solutions."""


def count_path_recursive(m, n):
    """Count number of paths with the recursive method."""
    def traverse(m, n, location=[1, 1]):
        # return 0 if past edge
        if location[0] > m or location[1] > n:
            return 0
        # return 1 if at end position
        if location == [m, n]:
            return 1
        return traverse(m, n, [location[0] + 1, location[1]]) + traverse(m, n, [location[0], location[1] + 1])

    return traverse(m, n)


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
