from queue import PriorityQueue
def calc_hrs(a, b):
    x1 = a
    y1 = a
    x2 =b
    y2 = b
    return abs(x1 - x2) + abs(y1 - y2)
def Astr_fun(x, strt, end):
    q = PriorityQueue()
    q.put((0, strt))  # Insert tuple of (total cost, node) into the priority queue
    n = set()
    c1 = {}
    c2 = {}
    c1[strt] = 0
    c2[strt] = calc_hrs(strt, end)
    while not q.empty():
        currcs, cnde = q.get()
        if cnde == end:
            return True
        n.add(cnde)
        for nnde, e_cst in x[cnde]:
            s = c1[cnde] + e_cst
            if nnde not in c1 or s < c1[nnde]:
                c1[nnde] = s
                c2[nnde] = s + calc_hrs(nnde, end)
                if nnde not in n:
                    q.put((c2[nnde], nnde))
    return False