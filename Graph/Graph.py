
class Node:

    def __init__(self , key , value , extra=None):
        self.key = key
        self.value = value if value is not None else key
        self.extra = extra if extra is not None else dict()

    def __getattr__(self , attr):
        return self.extra[attr]

    def __setattr__(self, name, value):
        self.extra[name] == value

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key==other.key
    
    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        return "K:{}|V:{}".format(self.key , self.value)


class UndirectedGraph:

    def __init__(self , adj_matrix : list = None , adj_list :dict =None , max_size=None , number_vertecies=None):

        if adj_list is not None:
            self.adj_list = adj_list
        else:
            self.adj_list = self.to_adjacent_list(adj_matrix = adj_matrix)

    def add_vertex(self , v:Node):
        if v not in self.adj_list:
            adj_list[v] = []
            self.adj_matrix = self.to_adjacent_matrix
        else:
            raise Exception("Vertex already exists")

    def add_edge(self , e:tuple):
        u,v = e
        if u not in self.adj_list or v not in self.adj_list:
            raise Exception("vertex not in graph")

        else:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def to_adjacent_matrix(self):
        """
            create adjacent matrix representation from adjacent list
        """
        pass

    def to_adjacent_list(self,*args ,**kwargs):
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