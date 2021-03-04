
def min_multiplication_cost(dims=[]):
    """
        compute the minimum cost of chain matrix multiplication
    Args:
        dims (list, optional): dimensions of the matrices in format
        [(p1,p2) , (p3,p4) , ...]

    Returns:
        int: cost 
    """
    if len(dims)<2:
        return None
    elif len(dims)==2:
        return dims[0][0] * dims[0][1]*dims[1][1] , [(dims[0][0] , dims[1][1])]
    else:
        f1 = dims[0][0] * dims[0][1]*dims[1][1] + min_multiplication_cost([(dims[0][0] , dims[1][1])] + dims[2:])[0]
        cost , newdims=min_multiplication_cost(dims[1:])
        f2 = cost + dims[0][0] * dims[0][1] * newdims[0][1]
        return min(f1,f2)


print(min_multiplication_cost([(10,100),(100, 5),(5,50)]))