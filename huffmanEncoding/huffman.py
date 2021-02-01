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
            return self.parent==None

        def is_leaf(self):
            return self.left==None and self.right==None
        
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

        def shallow_copy(self):
            return Node(self.data , self.key ,  self.parent , self.left , self.right)

        def deep_copy(self):
            pass

    
import sys 

class MaxHeap: 

	def __init__(self, maxsize=100 , min_key=-100): 
		
		self.maxsize = maxsize 
		self.size = 0
		self.Heap = [min_key] * (self.maxsize + 1) 
		self.Heap[0] = Node(sys.maxsize )
		self.FRONT = 1

	# Function to return the position of 
	# parent for the node currently 
	# at pos 
	def parent(self, pos): 
		
		return pos // 2

	# Function to return the position of 
	# the left child for the node currently 
	# at pos 
	def leftChild(self, pos): 
		
		return 2 * pos 

	# Function to return the position of 
	# the right child for the node currently 
	# at pos 
	def rightChild(self, pos): 
		
		return (2 * pos) + 1

	# Function that returns true if the passed 
	# node is a leaf node 
	def isLeaf(self, pos): 
		
		if pos >= (self.size//2) and pos <= self.size: 
			return True
		return False

	# Function to swap two nodes of the heap 
	def swap(self, fpos, spos): 
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], 
											self.Heap[fpos]) 

	# Function to heapify the node at pos 
	def maxHeapify(self, pos): 

		# If the node is a non-leaf node and smaller 
		# than any of its child 
		if not self.isLeaf(pos): 
			if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
				self.Heap[pos] < self.Heap[self.rightChild(pos)]): 

				# Swap with the left child and heapify 
				# the left child 
				if (self.Heap[self.leftChild(pos)] > 
					self.Heap[self.rightChild(pos)]): 
					self.swap(pos, self.leftChild(pos)) 
					self.maxHeapify(self.leftChild(pos)) 

				# Swap with the right child and heapify 
				# the right child 
				else: 
					self.swap(pos, self.rightChild(pos)) 
					self.maxHeapify(self.rightChild(pos)) 

	# Function to insert a node into the heap 
	def insert(self, element): 
		
		if self.size >= self.maxsize: 
			return
		self.size += 1
		self.Heap[self.size] = element 

		current = self.size 

		while (self.Heap[current] > 
			self.Heap[self.parent(current)]): 
			self.swap(current, self.parent(current)) 
			current = self.parent(current) 

	# Function to print the contents of the heap 
	def Print(self): 
		
		for i in range(1, (self.size // 2) + 1): 
			print(" PARENT : " + str(self.Heap[i]) +
				" LEFT CHILD : " + str(self.Heap[2 * i]) +
				" RIGHT CHILD : " + str(self.Heap[2 * i + 1])) 

	# Function to remove and return the maximum 
	# element from the heap 
	def extractMax(self): 

		popped = self.Heap[self.FRONT] 
		self.Heap[self.FRONT] = self.Heap[self.size] 
		self.size -= 1
		self.maxHeapify(self.FRONT) 
		
		return popped 

print('The maxHeap is ') 
      
maxHeap = MaxHeap(15) 
maxHeap.insert(Node(5)) 
maxHeap.insert(Node(3)) 
maxHeap.insert(Node(17)) 
maxHeap.insert(Node(10)) 
maxHeap.insert(Node(84)) 
maxHeap.insert(Node(19)) 
maxHeap.insert(Node(6)) 
maxHeap.insert(Node(22)) 
maxHeap.insert(Node(9)) 

maxHeap.Print() 



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
