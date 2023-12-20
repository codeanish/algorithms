graph = {
  5: [3,7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

visited: list[int] = []
queue: list[int] = []

def bfs(visited: list[int], graph: dict[int,list[int]], node: int):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

if __name__ == "__main__":
    print("Breadth-First Search")
    bfs(visited, graph, 5)