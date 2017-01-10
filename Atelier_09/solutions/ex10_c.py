#!usr/bin/python3

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

def has_path(graph, nodeA, nodeB):
    '''peut-on se frayer un chemin?'''
    paths = find_all_paths(graph, nodeA, nodeB, path=[])
    return len(paths) > 0

if __name__ == "__main__":
    from ex02 import g as barbe_bleue
    print(has_path(barbe_bleue, "Georgia", "Charlotte"))
