def bidirec_srch_fun(p, bgin, end):
    lst1 = [bgin]
    lst2 = [end]
    lst3 = set([bgin])
    lst_vs = set([end])
    while lst1 and lst2:
        curr = lst1.pop(0)
        for x in p[curr]:
            if x not in lst3:
                lst1.append(x)
                lst3.add(x)
            if x in lst_vs:
                return True
        bck_cur = lst2.pop(0)
        for x in p[bck_cur]:
            if x not in lst_vs:
                lst2.append(x)
                lst_vs.add(x)
            if x in lst3:
                return True
    return False