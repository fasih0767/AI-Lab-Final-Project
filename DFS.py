def depth_FS_Func(g, st, x):
    x.add(st)
    print(st,' ')  # Process the node, you can modify this as per your requirement
    for i in g[st]:
        if i not in x:
            depth_FS_Func(g, i, x)
