import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [ [] for i in range(n+1) ] 
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
  x, y, z = map(int, input().split()) #a노드에서 b노드로 가는 비용이 c
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, c))
  distance[c] = 0
  while q: # 큐가 비어있지 않다면 
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들 확인 
    for i in graph[now]:
      cost = dist + i[1] 
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)

#도달할 수 있는 노드의 개수
count = 0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
  #도달할 수 있는 노드인 경우
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

print(count-1, max_distance)