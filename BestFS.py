from queue import PriorityQueue
def Best_FS_fun(x, st, end):
    q = PriorityQueue()
    q.put((0, st))
    nde = set()
    while not q.empty():
        curr_hrstc, n = q.get()
        if n == end:
            return True
        nde.add(n)
        for nd1, ehrtc in x[n]:
            if nd1 not in nde:
                q.put((ehrtc, nd1))
    return False