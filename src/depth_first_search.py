# Using a Python dictionary to act as an adjacency list
graph = {
  5 : [3,7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

visited: set[int] = set() # Set to keep track of visited nodes of graph.

def dfs(visited: set[int], graph: dict[int, list[int]], node: int):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == "__main__":
    print("Following is the Depth-First Search")
    dfs(visited, graph, 5)