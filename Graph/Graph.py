
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

    def __init__(self):
        super().__init__()

    def to_adjacent_matrix(self):
        pass

    def to_adjacent_list(self):
        pass

    def search(self):
        pass

    def _dfs(self):
        pass

    def _bfs(self):
        pass

    
