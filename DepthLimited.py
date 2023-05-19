def depth_lmted_fun(g, st, end, lim):
    if st == end:
        return True
    if lim <= 0:
        return False
    for n in g[st]:
        if depth_lmted_fun(g, n, end, lim - 1):
            return True
    return False