t,e=map(int,input().split())
graph={}
for i in range(e):
    a,b=map(int,input().split())
    graph.setdefault(a,[]).append(b)
print(graph)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
print(find_all_paths(graph,1,2))
