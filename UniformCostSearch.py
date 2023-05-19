from queue import PriorityQueue
def uniform_CostS_fun(x, begin, y):
    q = PriorityQueue()
    q.put((0, begin))
    lst1 = set()
    lst2 = {}
    list_cst = {}
    lst2[begin] = None
    list_cst[begin] = 0
    while not q.empty():
        curr_cst, cur = q.get()
        if cur == y:            plist = []
            while cur is not None:
                plist.append(cur)
                cur = lst2[cur]
            return plist[::-1]
        lst1.add(cur)
        for a, e_cst in x[cur]:
            if a not in lst1:
                updated_cst = list_cst[cur] + e_cst
                if a not in list_cst or updated_cst < list_cst[a]:
                    list_cst[a] = updated_cst
                    lst2[a] = cur
                    q.put((updated_cst, a))
    return None