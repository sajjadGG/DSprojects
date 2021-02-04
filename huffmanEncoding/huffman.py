"""
implement a module for huffman encoding and decoding
endcode into cmp file first write the decode dictionary needed for decoding 
then write the data
for instance if the input is "h" and code is h : 0 encoded file will be
h:0

0
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
        """[summary]
            extract character frequencies fromfile
        Args:
            path (str): [description]. file to be decoded

        Returns:
            (dict): [description]. char :  frequency
        """
        #TODO : exception handling
        freqs = {}
        with open(path , 'r') as f:
            for c in f.read():
                
                if c in freqs:
                    freqs[c]+=1
                else:
                    freqs[c]=1
        return freqs

    def _build_heap(self , char_freq):
        """[summary]
            build heap using character frequencies
        Args:
            char_freq (dict): [description]. char : freq
        """
        self.heap = []
        for k in char_freq:
            heappush(self.heap , (char_freq[k] , Node(k , char_freq[k])))
        
    
    def _extract_codes(self , root):
        """[summary]
            extract encoding codes from huffman tree
        Args:
            root (Node): [description]. root of huffman tree

        Returns:
            (dict): [description]. char : huffmancode
        """
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
        """[summary]
            write encoded file
        Args:
            read_path (str): [description]. file to be encoded
            write_path (str): [description]. path to write encoded file
        """
        decodes = self._decode_dic()
        n = len(decodes)
        with open(read_path , 'r') as rf , open(write_path , 'w') as wf:
            i = 0
            for k in decodes:
                wf.write("{}:{}".format(k,decodes[k]))
                i+=1
                if i<n:
                    wf.write(',')
                else:
                    wf.write('\n')

            for c in rf.read():
                wf.write(self.codes[c])
        
        


    #Based on CLR
    def encode(self,path, write_path='enc.cmp'):
        """[summary]
            public interface for encoding the file
        Args:
            path (str): [description] path to file which is requested to be encoded 
            write_path (str, optional): [description]. Defaults to 'enc.cmp'.
        """
        freqs=self._freq(path)
        n = len(freqs)
        self._build_heap(freqs)
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
        """[summary]
        extract revese dictionary for decoding
        Returns:
            (dict): [description]. huffmancode  : char
        """
        assert self.codes is not None
        decodes = {}
        for k in self.codes:
            decodes[self.codes[k]] = k
        return decodes

    def _extract_decode(self , c):
        """[summary]
        extract decode dictionary from file meta data in files header
        Args:
            c (str): header of the file consist of information needed to 
            construct decode dictionary

        Returns:
            (dict) : [description]. huffmancode : char
        """
        l =  c.split(',')
        de = {}
        for e in l:
            k,v = e.split(':')
            de[k] = v
        return de


    def decode(self,path , write_path='decode.txt'):
        """[summary]
            decode a file in format specified by the this module
        Args:
            path (str): [description]. path of file to be decoded
            write_path (str, optional): [description]. Defaults to 'decode.txt'.
        """
        
        is_data=False
        with open(path , 'r') as rf , open(write_path , 'w') as wf:
            
            l = rf.read()
            decodes = self._extract_decode(l.split('\n')[0])

            res=""
            curr=0
            l = l.split('\n')[1]
            while curr<len(l):
                if res in decodes:
                    wf.write(decodes[res])
                    res=""
                else:
                    res+=l[curr]
                    curr+=1
            wf.write(decodes[res])
        
        

if __name__ =='__main__':

    h =HuffmanEndoder()
    print("please enter your file path")
    l = input()
    inp_path , extension = "".join(l.split('.')[:-1]) , l.split('.')[-1]

    if extension=='txt':
        h.encode(l , inp_path+'.cmp')
        print("done")

    elif extension=='cmp':
        h.decode(inp_path , inp_path+'decoded.txt')
        

# root = h.encode('test.txt')
# h.decode('enc.cmp')
# root.print_down() 