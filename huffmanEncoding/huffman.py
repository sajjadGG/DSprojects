"""
implement a module for huffman encoding and decoding
"""

class Stack():

    def __init__(self):
        self.data=[]
    
    def push(self, p):
        self.data.append(p)

    def pop(self):
        return self.data.pop()
    
    def peak(self):
        return self.data[-1]


class Node():
        
        def __init__(self,data,key=None,parent=None , left=None , right=None):
            self.data = data
            if key==None:
                key=data
            self.parent = parent
            self.left = left
            self.right = right

        def is_root(self):
            return self.parent==None

        def is_leaf(self):
            return self.left==None and self.right==None
        
        def __str__(self):
            return str(data)


class BinaryTree():
    
   
        
    def __init__(self,root,policy='max_heap'):
        self.root = root
        if isinstance(policy,str):
            #TODO : support for 'min_heap' , 'BST'
            if policy in ['max_heap']:
                self.prop_func = self._max_heap_prop

            self.policy = policy
        else:
            self.prop_func = policy
            self.policy='custom' 
    
    def traverse(self , how='in_order'):
        
        if how=='in_order':
            _in_order(self.root)
        elif how=='pre_order':
            _pre_order(self.root)
        elif how=='post_order':
            _pre_order(self.root)
        else:
            print("how specifed is not in_order , pre_order or post_order please specifie one of these")
        

    def add(self,data,key=None):
        
        n = Node(data,key=key,left=self.root)

        self.root.parent = n
        self.root=n
        

    def check_prop(self,root):
        self.prop_func(root)


    #private methods
    def _in_order(self,node):
        if node==None:
            return
        else:
            _in_order(node.left)
            print(node)
            _in_order(node.right)
    
    def _post_order(self,node):
        if node==None:
            return
        else:
            _in_order(node.left)
            _in_order(node.right)
            print(node)
    
    def _pre_order(self,node):
        if node==None:
            return
        else:
            print(node)
            _in_order(node.left)
            _in_order(node.right)
    
    def _max_heap_prop(self,n):
        return (n.key > (n.left.key if n.left!=None else n.key-1)) and (n.key > (n.right.key if n.right!=None else n.key-1) )

class HuffmanEndoder():
    """
    HuffmanEncoder for .txt file and decode .cmp files

    """
    def __init__(self):
        super().__init__()

    def _build_tree(self , char_freq):
        
        pass

    def encode(self,path):


        pass

    def decode(self,path):
        pass
