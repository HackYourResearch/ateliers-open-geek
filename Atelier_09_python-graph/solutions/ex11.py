#!usr/bin/python3

def depth_first_traverse(graph, start, path=[]):
    path=path+[start]
    for node in graph[start]:
        if node not in path:
            path = depth_first_traverse(graph,node,path)
    return path

if __name__ == "__main__":
    from ex02 import g as barbe_bleue
    print(depth_first_traverse(barbe_bleue, "Georgia", "Charlotte"))
