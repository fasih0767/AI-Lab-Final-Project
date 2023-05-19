def breadth_first_search_fun(nd):
    lst1 = [False] * (len(graph))
    lst2 = []
    lst1.append(nd)
    lst2.append(nd)
    while lst2:
        n = lst2.pop(0)
        print(n, " ")
        for x in graph[n]:
            if x not in lst1:
                lst1.append(x)
                lst2.append(x)