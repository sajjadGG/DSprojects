
class Node:

    def __init__(self , key , value):
        self.key = key
        self.value = value

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key==other.key
    
    def __ne__(self, other):
        return not(self == other)

class Graph:

    def __init__(self , adj_matrix : list = None , adj_list :dict =None , max_size=None , number_vertecies=None):

        if adj_matrix is not None:
            self.adj_matrix = adj_matrix
        else:
            self.adj_matrix == self.to_adjacent_matrix

        if adj_list is not None:
            self.adj_list = adj_list
        else:
            self.adj_list = self.to_adjacent_list

    def add_vertex(self , v:Node):
        if v not in self.adj_list:
            adj_list[v] = []
            self.adj_matrix = self.to_adjacent_matrix
        else:
            raise Exception("Vertex already exists")

    def add_edge(self , e:tuple):
        pass 

    def to_adjacent_matrix(self):
        """
            create adjacent matrix representation from adjacent list
        """
        pass

    def to_adjacent_list(self):
        """
            create adjacent list representation from adjacent matrix
        """
        pass

    def search(self):
        pass

    def _dfs(self , root:Node , visited=set()): 
        visited.add(root)
        for neighbour in self.adj_list[root]:
            if neighbour not in visited:
                self._dfs(neighbour , visited)
        return visited

    def _bfs(self):
        pass


def find_connected_components(g:Graph):
    scc = []
    visited=set()
    for v in g.adj_list:
        if v not in visited:
            component = g._dfs(v)
            scc.append(component)
            visited.update(component)
    return scc