"""
implement a module for huffman encoding and decoding
"""

class Stack():
    """
    Stack implementation using list
    """

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
                self.key=data
            else:
                self.key = key
            self.parent = parent
            self.left = left
            self.right = right

        def get_data(self):
            return self.data

        def get_key(self):
            return self.key

        def set_data(self , data):
            self.data = data
        
        def set_key(self , key):
            self.key = self.key

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def is_root(self):
            return self.parent is None

        def is_leaf(self):
            return self.left is None and self.right is None
        
        def __str__(self):
            return str(self.data)

        def __gt__(self , other):
            return self.key > other.key

        def __lt__(self , other):
            return self.key < other.key

        def __eq__(self , other):
            return self.key == other.key

        def __le__(self , other):
            return self.key <= other.key

        def __ge__(self , other):
            return self.key >= other.key
        
        def print_down(self):
            if self is None:
                return
            if self.is_leaf():
                print(self)
            else:
                if self.left is not None:
                    self.left.print_down()
                print(self)
                if self.right is not None:
                    self.right.print_down()


        def shallow_copy(self):
            return Node(self.data , self.key ,  self.parent , self.left , self.right)

        def deep_copy(self):
            pass



from heapq import *
class HuffmanEndoder():
    """
    HuffmanEncoder for .txt file and decode .cmp files

    """
    def __init__(self):
        pass

    def _freq(self , path):
        #TODO : exception handling
        freqs = {}
        with open(path , 'r') as f:
            for c in f.read():
                
                if c in freqs:
                    freqs[c]+=1
                else:
                    freqs[c]=1
        return freqs

    def _build_tree(self , char_freq):
        pad = 10
        self.heap = []
        for k in char_freq:
            heappush(self.heap , (char_freq[k] , Node(k , char_freq[k])))
        
    
    def _extract_codes(self , root):
        path=""
        codes = {}
        def _extract(node , path):
            if node is None:
                return
            if node.is_leaf():
                codes[node.data] = path
            else:
                _extract(node.left , path+'0')
                _extract(node.right , path+'1')
        _extract(root , "1")
        return codes


    def _write_file(self,read_path,write_path):

        with open(read_path , 'r') as rf , open(write_path , 'w') as wf:
            for c in rf.read():
                wf.write(self.codes[c])
        
        


    #Based on CLR
    def encode(self,path, write_path='enc.cmp'):
        
        freqs=self._freq(path)
        n = len(freqs)
        self._build_tree(freqs)
        for i in range(1,n):
            #TODO : exception heap out of range
            print('hi')
            left = heappop(self.heap)[1]
            right = heappop(self.heap)[1]
            z = Node(left.data + right.data , left.key + right.key , left=left , right=right)
            print(z)
            heappush(self.heap,(z.key , z))

        self.codes = self._extract_codes(heappop(self.heap)[1])
        print(self.codes)
        self._write_file(path , write_path)

        
    def _decode_dic(self):
        assert self.codes is not None
        decodes = {}
        for k in self.codes:
            decodes[self.codes[k]] = k
        return decodes

    def decode(self,path ,decodes=None, write_path='decode.txt'):
        if decodes is None:
            decodes = self._decode_dic()

        with open(path , 'r') as rf , open(write_path , 'w') as wf:
            l = rf.read()
            res=""
            curr=0
            while curr<len(l):
                if res in decodes:
                    wf.write(decodes[res])
                    res=""
                else:
                    res+=l[curr]
                    curr+=1
            wf.write(decodes[res])
        
        

h =HuffmanEndoder()
root = h.encode('test.txt')
h.decode('enc.cmp')
# root.print_down() 