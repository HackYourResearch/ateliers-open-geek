#!usr/bin/python3

def find_path(graph, start, end, path=[]):
    path=path+[start]
    if start == end:
        return path
    if not graph.has_node(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path=path+[start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
