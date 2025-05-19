graph = [
    [0, 1, 1, 0, 0, 0, 0, 0], #0행
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0], #3행 i=3
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]  #7행 i=7
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]: # j -> 0~7
            dfs(g, j, visited)

def bfs(g, i, visited):
    pass

visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 7, visited_dfs)
print()
bfs(graph, 4, visited_bfs)

# 깊이 유선 탐색 dfs
# 너비 유선 탐색 bfs