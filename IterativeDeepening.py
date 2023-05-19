import DepthLimited
#importing depht limited search file since its already defined and is required here.
def iteratve_deepng_fun(g, s, end, dep):
    for dlim in range(dep + 1):
        if DepthLimited.depth_lmted_fun(g, s, end, dlim):
            return True
    return False
