graph = {
    "a" : ["b","d"],
    "b" : [],
    "c" : [],
    "e" : ["c"],
    "d" : ["e", "g"],
    "f" : [],
    "g" : ["f"]
    }





def dfs(graph, source):
    stack = []
    visited = []

    stack.append(source)
    visited.append(source)

    while stack:
        node = stack.pop(-1)
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                stack.append(neighbour)

dfs(graph, "a")
