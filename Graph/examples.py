
def compute_out_degree(adj_list):
    out_degs = {}
    for v in adj_list:
        out_degs[v] = len(adj_list[v])
    return out_degs

def transpose_list(adj_list):
    pass