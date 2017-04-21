#!usr/bin/python3

def find_shortest_path(graph, start, end, path=[]):
    path=path+[start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    shortest_path = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                if newpath and (len(shortest_path) == 0 or len(newpath) < len(shortest_path)):
                    shortest_path = newpath
return shortest_path
if __name__ == "__main__":
    from ex02 import g as barbe_bleue
    print(find_shorest_path(barbe_bleue, "Georgia", "Charlotte"))
