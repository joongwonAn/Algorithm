#DFS, Depth-First Search, 깊이 우선 탐색
#그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘


def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

visited = [False] * 9
dfs(graph, 1, visited)
