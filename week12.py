from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0], #0행 A
    [1, 0, 0, 1, 0, 0, 0, 0], #1행 B
    [1, 0, 0, 1, 0, 0, 0, 0], #2행 C
    [0, 1, 1, 0, 1, 1, 1, 0], #3행 D  i=3
    [0, 0, 0, 1, 0, 1, 0, 0], #4행 E
    [0, 0, 0, 1, 1, 0, 0, 0], #5행 F
    [0, 0, 0, 1, 0, 0, 0, 1], #6행 G
    [0, 0, 0, 0, 0, 0, 1, 0]  #7행 H  i=7
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]: # j -> 0~7
            dfs(g, j, visited)

def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = 1
    #while len(queue) != 0:
    while queue:
        i = queue.popleft() # q가 비어있을 때까지 반복 - popleft
        print(chr(ord('A') + i), end=' ')
        for j in range(len(graph)):     # 열을 반복시키기 위한 코드
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = 1


visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 7, visited_dfs)
print()
bfs(graph, 4, visited_bfs)

