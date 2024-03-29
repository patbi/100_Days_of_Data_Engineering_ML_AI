"""
* DATA STRUCTURES:

	Why we need to use data structure ?

	- Data structures: to store in an efficient way
	
	Why to use data structures ?

	- We often have the intuition --> if we want to make an algorithm fast,
		we have to optimize it
	- Avoid nested for loops
	- Make every calculation as fast as possible
	- But algorithms can be boosted up by proper data structures
	- Data structures make sure the running time will be better
	- Dijkstra algorithm
	- Without a proper data structure (heap / priority queue ) the running
		time would be quadratic // O(N²) 
	- Priority queue approach makes sure the running time will be far
		better // O(N*logN)
"""



"""
* Difference between Data structures and Abstract Data Types (ADT)


- Abstract data types:

	- Basically this is the model(logical description) for a certain data structure
	- It is like a supertype in programming (so an interface in Java)
	- We just define what methods / functions the data structure will have,
		so we define the basic behavior
	- IMPORTANT: it is just the model, ADT does not specify the concrete implementation
		or programming language
	- "Basically what the user knows"
	- For example: stack --> push() pop() peek()

	abstract data types(1-Stack, 2-Queue, 3-Priority queue, 4-Dictionary / hashmap)
	data structures (1-array,linked list. 2-array,linked list. 3-heap. 4-array)

- Data structure:

	- The concrete implementation, the actual representation of the data
	- The aim is to be able to store and retrieve data in an efficient manner
	- What we want: to be able to insert / find items in O(1) time complexity and to be able to retrieve items in O(1) as well
	- For example: arrays, linked lists, banary trees ...

"""



"""
* How to install python

url: https://www.python.org/downloads/
"""


"""
1 - Arrays Getting Started: in python: data structures

A collection of elements / values
each identified by an array index or key.

	- index starts at zero
	- because of the indexes: random access is possible


* Multidimensional arrays: it can prove to be very important in mathematical related computations (matrixes)
	- numbers[][] two dimensional array
	- First parameter: row index, Second parameter: column index


* Arrays:

- Arrays are data structures in order to store items of the same type
- We use indices as keys 
- Arrays can have as many dimensions as we want: one or two dimensional arrays are quite popular
- For example:storing a matrix --> two dimensional array
- Dynamic array: when the size of the array is changing dynamically
- Applications: looking tables / hashtables, heaps


* Advantages:
- We can use random access because of the keys: getItem(int index)
		will return the value with the given key very fast // O(1)
- Very easy to implement and to use 
- Very fast data struxture
- We should use arrays in applications when we want to add items over and over again and we want to take items with given indexes~ it will be fast


* Disadvantages:
- We have to now the size of the array at compile-time: so it is not so dynamic data structure
- If it is full: we have to create a bigger array and have to copy the values one by one // reconstructing an array is 0(N) operation
- It is not able to store items with different types

"""


"""
* Arrays all operations in python

	- Arrays operation: add
		We can keep adding values to the array as far the array is not full
		So: when adding new values to the list, we just have to insert it with the next index --> very fast O(1) operation
	
	- Arrays operation: insert item
		We would like to insert a given value with a given index
		So: it is a bit more problematic, sometime we have to shift lots of values in order to be able to insert the new one ~ O(N) time complexity

		Add new item: O(1)
		Insert item to a given index: O(N)

	
	- Arrays operation: remove items
		removeLast(): We would like to remove the last item, it is very simple, just remove it // O(1) time complexity
		
		remove(1) - Arrays operation: remove items with given index we would like to remove a value with a given, it is not that simple, we may have to shift items // O(N) time complexity
		So: overall complexity will be linear O(N)
	

		removing last item: O(1)
		removing first item,middle item: O(N)
"""



"""
* Arrays in Python
"""

#numbers = [25.5,20,10,40,30,50,70];
#random indexing --> O(1) get items if we know the index

#print(numbers[5]);
#numbers[5] = 100;
#numbers[5] = 'Thenavigo';
#print(numbers[5]);

#for num in numbers:
#    print(num);

#for i in range(len(numbers)):
#    print(numbers[i]);

#print(numbers[0:2]);


#O(N) search running time
#maximum = numbers[0];
#for num in numbers:
#    if num > maximum:
#        maximum = num;

#print(maximum);



"""
2 - Linked list in python

- Linked lists are composed of nodes and references / pointers pointing from one node to the other.
The last reference is pointing to a NULL

	* A single node:
		- contains data --> integer, double or custom object 
		- contains a reference pointing to the next node in the linked list

	class Node {
		data
		Node nextNode


		...
	}


- Each node is composed of a data and a reference/link to the next node in the sequence
- Simple and very common data structure
- They can be used to implement several other common data types: stacks, queues
- Simple linked lists by themselves do not allow random access to the data // so we can not use indexes ..getItem(int index)
- Many basic operations such as obtaining the last node of the list or finding a node that
	contains a given data or locating the place where a new node should be inserted --require sequential scanning of most or all of the list elements


	* Advantages:
	
	- Linked lists are dynamic data structures (arrays are not)
	- It can allocate the needed memory in run-time
	- Very efficient if we want to manipulate the first elements
	- Easy implementation
	- Can store items with different sizes: an array assumes every element to be exactly the same
	- It's easier for a linked list to grow organically. An array's size needs to be known ahead of time, or re-created when it needs to grow



	* Disadvantages:
	- Waste memory because of the references
	Nodes in a linked list must be read in order from the beginning as linked lists have sequential access (array items can reached via indexes in O(1) time)
	- Difficulties arise in linked lists when it comes to reverse traversing.
	Singly linked lists are extremely difficult to naigate backwards.
	- Solution: doubly linked lists --> easier to read, but memory is wasted is allocating space for a back pointer
"""


"""
* Linked list operations: insertion

	- Inserting items at the beginning of the linked list: very simple, we just have to update the references --> O(1) time complexity

	linkedList.insertAtStart(10);
	linkedList.insertAtStart(4);
	linkedList.insertAtStart(-5);

	- Inserting items at the end of the linked list: not thatvery simple, we have to traverse the whole linked list to find the last node.
		How do we find the last node ? We know the last node is pointing to a NULL.

		Plus we have to update the references when we get there O(N) time complexity

			- Insert at the beginning O(1)
			- Inserting at the end O(N)

* Linked list operations: remove

	- Remove item at the beginning of the list is always very fast: we do not have to search the item, we just have to update the references accordingly O(1) time complexity

linkedList.removeStart()

	- Remove item at a given point of the list is not always very fast: we have to searLinked list operations: insertionh for the given item whiLinked list operations: insertionh may take lot of time
		if the item is at the end of the list O(N) time complexity
linkedList.remove(10)

		- Remove items at the beginning: O(1)
		- Remove items at given positions: O(N) in the main

"""


"""
* Doubly linked list in python

	- Problems with linked lists:
	
	Fo example: 12 --> 4 --> 123 --> (-7) --> 25 --> NULL

	We can get from 4 to 25 because we just have to hop to the next nodes BUT we can not go from 25 to 4 because the references are in the opposite directions

	- Solution: doubly linked list --> Node class has two references, one pointing to the next node, one pointing to the previous node.

	12 <-- 4 <-- 123 <-- (-7) <-- 25 
					  --> NULL
	12 --> 4 --> 123 -->  (-7) --> 25 	
"""



"""
* linked lists vs arrays

	1) Search:

	- Search operation yields the same result for both data structure
	- ArrayList search operation is pretty fast compared to the LinkedList search operation
	- We can use random access with arrays: getItem(int index) which is O(1) time complexity
	- LinkedList performance is O(N) time complexity
	- So the conclusion: ArrayList is better for this operation
	- Why ?
	- ArrayList maintains index based system for its elements as it uses array data structure implicity which makes it faster for searching an element in the list
	- On the other hand LinkedList requires the traversal through all the items for searching an element


	2) Deletion:

	- LinkedList remove operation takes O(1) time if we remove items from the beginning and usually this is the case
	- ArrayList: removing first element ( so at the beginning ) takes O(N) time, removing the last item takes O(1) times
	- But on average: we have to reconstruct the array when removing
	- So the conclusion: LinkedList is better for this operation
	- Why ?
	- LinkedList basically operates with pointers: removal only requires change in the pointer location which can be done very fast


	3) Memory management:

	- Arrays do not need any extra memory
	- LinkedLists on the other hand do need extra memory because of the references / pointers
	- So in this aspect: arrays are better, they are memory friendly 



			   LinkedList         Arrays
Search                      O(N)               O(1)
Insert at the start         O(1)               O(N)
Insert at the end           O(N)               O(1)
Waste space                 O(N)               0

"""


"""
* Linked list insertion implementation in python

"""

class Node(object):

	def __init__(self, data):
		self.data = data;
		self.nextNode = None;


class LinkedList(object):

	def __init__(self):
		self.head = None;
		self.size = 0;


	#O(1)
	def insertStart(self, data):
		self.size = self.size + 1;
		newNode = Node(data);

		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head;
			self.head = newNode;

	#Linked list implementation in python (remove)

	def remove(self, data):
		if self.head is None:
			return;

		self.size = self.size - 1;

		currentNode = self.head;
		previousNode = None;

		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;

		if previousNode is None:
			self.head = currentNode.nextNode;
		else:
			previousNode.nextNode = currentNode.nextNode;



	#O(1)
	def size1(self):
		return self.size;


	# O(N) not good
	def size2(self):
		actualNode = self.head;
		size = 0;


		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;

		return size;

	#Linked list implementation in python (travese)

	def insertEnd(self, data):

		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;

		actualNode.nextNode = newNode;


	def traverseList(self):
		actualNode = self.head;

		while actualNode is not None:
			print("%d " % actualNode.data);
			actualNode = actualNode.nextNode;


#Linked list implementation testing in python
linkedlist = LinkedList();

linkedlist.insertStart(12);
linkedlist.insertStart(125);
linkedlist.insertStart(4);
linkedlist.insertEnd(48);

linkedlist.traverseList();
print(linkedlist.size1());

linkedlist.remove(48);
linkedlist.remove(12);
linkedlist.remove(125);
linkedlist.remove(4);

print(linkedlist.size1());



"""
* Doubly linked list in python

Problems with linked lists:

	12 <-- 4 <-- 123 <-- (-7) <-- 25 
					  --> NULL
	12 --> 4 --> 123 -->  (-7) --> 25 



We can get from 4 to 25 because we just have to hop to the next node BUT we can
not go from 25 to 4 because the references are in the opposite directions.

Solution: doubly linked list --> Node class has two references, one pointing to the next node, one pointing to the previous node


Ok we can get from eveywhere to everywhere BUT it is not so memory friendly,
we have to store lots of references

BUT there is no need to track the previous node during traversal

"""





"""
* Stack in python

	- It is an abstract data type (interface)
	- Basic operations: pop(), push(), and peek()
	- LIFO structure: last in first out
	- In most high level languages, a stack can be easy implemented either with arrays or linked lists
	- A number of programming languages are stack-oriented, meaning they define most basic operations (adding two numbers, printing a character) as taking their arguments from the stack, and placing any return values back on the stack


-- Push operation: put the given item to the top of the stack very simple operation, can be done in O(1)
stack.push(10000);

-- Pop operation: we take the last item we have inserted to the top of the stack (LIFO) very simple operation, can be done in O(1)
stack.pop();

-- Peek operation: return the item from the top of the stack without removing it very simple operation, can be done in O(1)
stack.peek();


-- Applications:

	- In stack-oriented programming languages
	- Graph algorithms: depth-first search can be implemented with stacks (or with recursion)
	- Finding Euler-cycles in a graph
	- Finding strongly connected components in a graph
"""


"""
* Stack in memory

	- Most important application of stacks: stack memory
	- It is a special region of the memory (in the RAM)
	- A call stack is an abstract data type that stores information about the active subroutines / methods / functions of a computer program
	- The details are normally hidden and automatic in high-level programming
	- Why is it good ?
	- It keeps track of the point to which each active subroutine should return control when it finishes executing
	- Stores temporary variables created by each function
	- Every time a function declares a new variable it is pushed onto the stack
	- Every time a function exits all of the variables - pushed onto the stack by that function - are freed --> all of its variables are popped off of the stack // and lost forever
	- Local variables: they are on the stack, after function returns they are lost
	- Stack memory is limited.
	diff(limited in size, fast access, local variables, space is managed efficiently by CPU, variables cannot be resized)

* Heap memory:
	- The heap is a region of memory that is not managed automatically for you
	- This is a large region of memory // unlike stack memory
	- C: malloc() and calloc() function // with pointers
	- Java: reference types and objects are on the heap
	- We have to deallocate these memory chunks: because it is not managed automatically
	- If not: memory leak
	- Slower because of the pointers
	diff(no size limits, slow access, objects, memory may be fragmented, variables can be resized // realloc())
"""



"""
* Stack and recursion

	- There are several situations when recursive methods are quite handy
	- For example: DFS, traversing a binary search tree, looking for an item in a linked list ...
	- What's happening in the background ?
	- All the recursive algorithms can be transformed into a simple method with stacks
	- IMPORTANT: if we use recursion, the OS will use stacks anyways

-- Depth-first search:

#recursion

public void dfs(Vertex vertex) {
	vertex.setVisited(true);
	printf(vertex);
	for(Vertex v: vertex.neighbours()) {
		if(!v.isVisited()) {
			dfs(v);
		}
	}
}	


#iterative approach with stack

public void dfs(Vertex vertex) {
	Stack stack;
	stack.push(vertex);

	while(!stack.isEmpty()){
		actual = stack.pop();
		for(Vertex v: actual.neighbours()) {
			if(!v.isVisited()) {
				v.setVisited(true);
				stack.push(v);
			}
		}
	}
}


-- Factorial: with recursion

public void factorial(int n) {
	if(n==0)
		return 1;
	return n*factorial(n-1);
}

This is the factorial function with Recursive implementation
n! = n*(n-1)*...*2*1

For example: 4! = 4*3*2*1 = 24
"""


"""
* Stack implementation in python
	- It is an abstract data type (interface)
	- Basic operations: pop(), push() and peek()
	- LIFO structure: last in first out
	- In most high level languages, a stack can be easy implemented either with arrays or linked lists
	- A number of programming languages are stack-oriented, meaning they define most basic operations (adding two numbers, printing a character) as taking their arguments from the stack, and placing any return values back on the stack



"""


class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek:", stack.peek())
print(stack.sizeStack())



"""
* Queue in python
	- It is an abstract data type (interface)
	- Basic operations: enqueue() and dequeue(), peek()
	- FOFO structure: first in first out
	- It can be implemented with dynamic arrays as well as with linked lists
	- Important when implementing BFS algorithm for graphs

Enqueue operation: we just simply add the new item to the end of the queue

queue.enqueue(20);

Dequeue operation: we just simply remove the item starting at the beginning of the queue // FIFO structure	
queue.dequeue();


Applications:
	- When a resource is shared with several consumers (threads): we store them in a queue
	- For example: CPU scheduling
	- When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes
	- For example: IO buffers
	- Operationel research applications or stochastic models relies heavily on queues

"""

#queue implementation in python
class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)

queue = Queue()
queue.enqueue(150)
queue.enqueue(250)
queue.enqueue(350)
print(queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())

"""
* Binary search tree python

	- Binary search trees are data structures
	- Keeps the keys in sorted order: so that lookup and other operations can use the principle of binary search
	- Each comparison allows the operations to skip over half of the tree, so that each lookup/insertion/deletion takes time proportional to the algorithms of the number of items stored in the tree
	- This is much better than the linear time O(N) required to find items by key in an unsorted array, but slower than the corresponding operations on hash tables


Sorted arrays(Inserting a new item is quite slow // o(N), Searching is quite fast with binary search // O(logN), Removing an item is slow // O(N))
Inserting a new item is very fast // O(1), Searching is sequential //O(N), Removing an item is fast because of the references // O(1)	

Binary search trees are going to make all of these operations quite fest, with O(log N) time complexity

"""



"""
* Binary search tree-insert

Insertion: we start at the root node. If the data we want to insert is greater than the root node we go to the right, if it is smaller, we go to the left

	binarySearchTree.insert(10);

Search: we start at the root node. If the data we want to find is greater than the root node we go to the right, if it is smaller, we go to the left until we find.

	binarySearchTree.find(10);
"""



"""
* Binary search tree-delete

Delete: soft delete --> we do not remove the node from the BST we just mark that it has been removed ~ not so efficient solution

In the main three possible cases:
	1.) The node we want to get rid of is a leaf node
	2.) The node we want to get rid of has a single child
	3.) The node we want to get rid of has 2 children
"""



"""
* Binary search tree-traversal in python
	1.) In-order traversal: we visit the left subtree + the root node + the right subtree recursively
	2.) Pre-order traversal: we visit the root + left subtree + the right subtree recursively
	3.) POst-order traversal: we visit the left subtree + right subtree + the root recursively
"""


"""
* Binary search tree running time

	        Average case           Worst case
Space           O(n)                   O(n)
Insert          O(log n)               O(n)
Delete          O(log n)               O(n)
Search          O(log n)               O(n)
	

What about the worst case scenarios ?
	- if the tree becomes unbalanced: the operations running times can be reduced to O(N) in the worst case
	- that why it is important to keep a tree as balanced as possible
"""



"""
* Binary search tree in python (BST)
"""


#Binary search tree insertion in python (BST)
class Node(object):
	def __init__(self, data):
		self.data = data;
		self.leftChild = None;
		self.rightChild = None;


class BinarySearchTree(object):

	def __init__(self):
		self.root = None;

	def insert(self, data):
		if not self.root:
			self.root = Node(data);

		else:
			self.insertNode(data, self.root);

	# O(LogN)  if the tree is balanced!!! --> it can reduced to O(N) --> AVL are needed
	def insertNode(self, data, node):
		if data < node.data:
			if node.leftChild:
				self.insertNode(data, node.leftChild);
			else:
				node.leftChild = Node(data);
		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild);
			else:
				node.rightChild = Node(data);

	#Binary search tree travercing in python

	def getMinValue(self):
		if self.root:
			return self.getMin(self.root);

	def getMin(self, node):

		if node.leftChild:
			return self.getMin(node.leftChild);

		return node.data;

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root);

	def getMax(self, node):

		if node.rightChild:
			return self.getMax(node.rightChild);

		return node.data;

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);

	def traverseInOrder(self, node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild);

		print("%s " % node.data);

		if node.rightChild:
			self.traverseInOrder(node.rightChild);


#Binary search tree testing
bst = BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(6);
print(bst.getMaxValue());
bst.traverse();



"""
* AVL tree in data structure python
	- Linked lists: quite easy to implement
		Stores lots of pointers
			O(N) search operation time complexity
			
	- Binary search trees: we came to conclusion that O(N) search complexity
		can be reduced to O(logN) time complexity
			But if the tree is unbalanced: these operations will become
				slower and slower
	
	- Balanced binary trees: AVL trees or red-black trees they are guaranteed to be balanced 
		Why is it good ? O(logN) is guaranteed
		
Conclusion: if we construct a binary search tree from a sorted array, we end up with a linkedlist
	O(logN) reduced to O(N)
"""


"""
* AVL tree rotation case
	
	- Case 1: rightRotate

		BEGIN rotateRight(Node node)
			Node tempLeftNode = node.getLeftNode()
			Node t = tempLeftNode.getRightNode()

			tempLeftNode.setRightNode(node)
			node.setLeftNode(t)

			node.updateheight()
			tempLeftNode.updateHeight()
		END
	
	- Case II leftRotate:

		BEGIN rotateLeft(Node node)

			Node tempRightNode = nodes.getRightNode()
			Node t = tempRightNode.getLeftNode()

			tempRightNode.setLeftNode(node)
			node.setRightNode(t)

			node.updateheight()
			tempRightNode.updateheight()
		END

	Case III: 
		- We have to make a left rotation an the node B (D-->B-->C)
		- We have to make a left rotation on the root node D (D-->C-->B)


	Case IV:
		- We have to make a left rotation on the root node D (D-->E-->F)

"""


"""
* AVL tree illustration
	- Link: https://www.programiz.com/dsa/avl-tree

"""


#AVL tree height balance implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class AVL(object):
	
	def __init__(self):
		self.root = None;

	def insert(self, data):
		self.root = self.insertNode(data, self.root);

	def insertNode(self, data, node):

		if not node:
			return Node(data);

		if data < node.data:
			node.leftChild = self.insertNode(data, node.leftChild);
		else:
			node.rightChild = self.insertNode(data, node.rightChild);

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		return self.settleViolation(data, node);

	#AVL tree violance implementation in python
	def settleViolation(self, data, node):
		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy situation...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy situation...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Left right heavy situation...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rightChild(node);

		if balance < -1 and data < node.rightChild.data:
			print("Right left heavy situation...");
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

	def calcHeight(self, node):

		if not node:
			return -1;
		
		return node.height;

	# if it returns value > 1 it means it is a left heavy tree --> right rotation
	# ......
	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;


	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;

"""
* AVL tree introduction

	- The running time of BST operations depends on the height of the binary search
		tree: we should keep the tree balanced in order to get the best performance
	- Thats why AVL trees came to be
	- 1962: invented by two russian computer scientist
	- In an AVL tree, the heights of the two child subtrees of any node differ by at most one
	- Another solution to the problem is a red-black trees
	- AVL trees are faster than red-black trees because they are more rigidly balanced BUT needs more work
	- Operating systems relies heavily on these data structures!!!
	- Most of the operations are the same as we have seen for binary search trees
	- Every node can have at most 2 children: the leftChild is smaller, the rightChild is greater than the parent node
	- The insertion operation is the same BUT on every insertion we have to check whether the tree is unbalanced or not
	- Delete operation is the same
	- Maximum / Minimum finding operations are the same as well.

	balancedTree.find(40);
	findMin();

	* Binary search trees

			   Average case         Worst case
Space                       O(N)               	   O(n)
Insert                      O(log n)               O(n)
Delete                      O(log n)               O(n)
Search                      O(log n)               O(n)


	* Balanced trees

			   Average case         Worst case
Space                       O(N)               	   O(n)
Insert                      O(log n)               O(log n)
Delete                      O(log n)               O(log n)
Search                      O(log n)               O(log n)

"""




# AVL tree rotation implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class AVL(object):

	def __init__(self):
		self.root = None;

	def calcHeight(self, node):
		return -1;

		return node.height;

	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;


	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;





"""
* AVL tree application
	
	- We can use this data structure to sort items
	- We just have to insert the N items we want to sort
	- We have to make an in-order traversal -> it is going to yield the numerical or alphabetical ordering.

		* Insertion: O(N*logN)
		* In-order traversal: O(N)
		* Overall complexity: O(N*logN)

	--Applications:

		* Databases when deletions or insertions are not so frequent, but have to make a lot of look-ups
		* Look-up tables usually implemented with the help of hashtables BUT AVL tress support more operations in the main
		* We can sort with the help of AVL trees
		* Red-black trees are a bit more popular because for AVL trees we have to make several rotations ~ a bit slower

"""



"""
* AVL tree height introduction

	- AVL tree requires the heights of left and right child of every node to differ at most +1 or -1
	- | height(leftSubtree) - height(rightSubtree) | < = 1
	- We can maintain this property in O(logN) time which is quite fast
	- Insertion:

		1.) a simple BST insertion according to the keys
		2.) fix the AVL property on each insertion from insertion upward

	- There may be several violations of AVL property from the inserted node up to the root
	- We have to check them all   
"""


#AVL tree node implementation in python
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class  AVL(object):

	def __init__(self):
		self.root = None;

	#AVL tree remove implementation in python
	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root);

	#AVL tree insertion implementation in python
	def insert(self, data):
		self.root = self.insertNode(data, self.root);

	def insertNode(self, data, node):

		if not node:
			return Node(data);

		if data < node.data:
			node.leftChild = self.insertNode(data, node.leftChild):
		else:
			node.rightChild = self.insertNode(data, node.rightChild);

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		return self.settleViolation(data, node);

	def removeNode(self.data, node):

		if not node:
			return node;

		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild);
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild);
		else:

			if not node.leftChild and not node.rightChild:
				print("Removing a left node...");
				del node;
				return node;

			if not node.leftChild:
				print("Removing right child...");
				tempNode = node.rightChild;
				del node;
				return tempNode;
			elif not node.rightChild:
				print("Removing left child...");
				tempNode = node.leftChild;
				del node;
				return tempNode;

			print("Removing node with two children...");
			tempNode = self.getPredecessor(node.leftChild);
			node.data = tempNode.data;
			node.leftChild = self.removeNode(tempNode.data, node.leftChild);

		if not node:
			return node; # if the tree had just a single node

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

		balance = self.calcBalance(node);

		# doubly left heavy situation
		if balance > 1 and self.calcBalance(node.leftChild) >= 0:
			return self.rotateRight(node);

		# left right case
		if balance > 1 and self.calcBalance(node.leftChild) < 0:
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		# right right case
		if balance < -1 and self.calcBalance(node.rightChild) <=0:
			return self.rotateLeft(node);

		# right left case
		if balance < -1 and self.calcBalance(node.rightChild) > 0:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def getPredecessor(self, node):

		if node.rightChild:
			return self.getPredecessor(node.rightChild);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def getPredecessor(self, node):

		if node.rightChild:
			return self.getPredecessor(node.rightChild);

		return node;

	def settleViolation(self, data, node):

		balance = self.calcBalance(node);

		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy tree...");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy tree...");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Tree is left right heavy...");
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def calcHeight(self, node):

		if not node:
			return -1;

		return node.height;

	def calcBalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);

	def traverseInOrder(self, node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild);

		print("% " % node.data);

		if node.rightChild:
			self.traverseInOrder(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);

		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;
		return tempLeftChild;

	def rotateLeft(self, node):
		print("Rotating to the left on node ", node.data);

		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;
		return tempRightChild;


#AVL Testing

av1 = AVL();
av1.insert(20);
av1.insert(10);
av1.insert(5);
av1.insert(7);
av1.insert(9);

av1.remove(10);
av1.remove(7);

av1.traverse();


"""
* Priority queue in data structure

	- It is an abstract data type such as stack or queue
	- BUT every item has an additional property: a priority value
	- In a priority queue, an element with high priority is served before an element with lower priority
	- Priority queues are usually implemented with heaps, but it can be implemented with self balancing trees as well
	- Very similar to queues with some modification: when we would like to get the next item --> the highest priority element is retrieved first.
		- No FIFO structure here

	-- Abstract Data Types: (Specification Interfaces ) < --- >  Data Structures (Concrete implementation)

	-- Operations:

		* insertWithPriority(data, priority) // sometimes we do not specify the priority
			
			this method will insert new item into the priority queue. We have to specify the data we want to insert and the priority associated with the given data
		
		* getHighestPriorityElement()

			Returns the element with highest priority: we have to reconstruct the heap 
			Max heap: returns maximum element
			Min heap: returns minimum element

		peek()

			Returns the element with highest priority: the structure of the heap does not change.

	-- Sorting:

		- The concept of priority queues naturally suggest a sorting algorithm
		- Insert all the elements to be sorted into a priority queue
		- Sequentially remove them: it will be the sorted order.
		- Why is it working ?
			- We have been discussing that priority queues rely heavily on priorities
			- We take out itemms --> the one with highest priority will be returned
			- Result sequency of decreasing priorities
			- This is the sorted order
			- For example: tree sort, heapsort


"""


"""
* Heap in data structure
	
	- It is baiscally a binary tree
	- Two main binary heap types: min and max heap
	- In a max heap, the keys of parent nodes are always greater than or equal to those of the children --> the highest key is in the root node
	- In a min heap, the keys of parent nodes are less than or equal to those of the children --> the lowest key is in the root node
	- It is complete: it cannot be unbalanced, We insert every new item to the next available place
	- Applications: Dijstra's algorithm, Prims algorithm
	- The heap is one maximally efficient implementation of a priority queue abstract data type
	- It has nothing to do with the pool of memory from which dynamically allocated memory is allocated

--- Heap properties:
	1.) Complete --> we construct the heap from left to right across each
		row // of course the last row may not be completely full
				There is no mising node from left to right in a layer

	2.) In a binary heap every node can have 2 children, left child and right child

	3.) Min heap --> the parent is always smaller than the values of the children

		Max heap --> the parent is always greater

		So: the root node will be the smallest/greatest value in the heap 
				// O(1) access

"""



"""
* Hashtable in data structure

	Arrays are just like that: if we know the index, the insert / retrieve operations can be done in O(1) time

	So arrays are going to solve our problem: the operations running time can be reduced to O(1)

	PROBLEM: we must transform the keys into array indexes, 
		// this is why hashfunctions came to be

	- Balanced BST --> we can achieve O(logN) time complexity for several operations including search
	- Can we do better ?
	- Yes, maybe we can reach O(1)
		This is why hashtables came to be

	- Array: if we know the index, the insertion and retrieval operations are very fast O(1).. that is what we are after

	Here wa want to search for a given item with a given key We have key-value pairs

		KEY ----------------> slot in set of buckets

	index = h(key) where h() is the hashfunction, it maps keys to indexes in the array.

In general: we have n items to be stored + m buckets in which we can store items
Problem: keys are not always nonnegative integers. We have to do prehashing in order to map string keys to indexes of an array.


How can we map a certain key to a slot in our array ? h(x) hashfunction is needed
	Hashing: we can map a certain key of any type(!!!) to a random array index.

	- if we have integer keys we just have to use the modulo operator to transform the number into the range [0,m-1] ~ quite easy

	- if the keys are strings: we can have the ASCII values of the character and make some transformation in order to end up with an index to the array


Hash function:

- Distribute the keys uniformly into buckets
- n: number of keys
- m: number of buckets // size of array
- h(x) = n % m (modulo operator)
	
	-- We should use prime numbers both for the size of the array and in our hash function to make sure the distribution of the generated indexes will be uniform.
	-- String keys: we could calculate the ASCII value for each character, add them up --> make % modulo

"""



"""
* Hashtable collision

	- Collision resolution with chaining: we put multiple entries into the same slot with the help of a linked list
		- If there are many collisions: O(1) complexity gets worse
		- It has an additional memory cost due to the references
	- Collision resolution with open addressing: better solution
	- If collision occurs, we find an empty slot instead
		- Linear probing: if a collision occures, we try the next slot ...if there is a collision too we keep trying the next slot until we find an empty slot
		- Quadratic probing: we trying slots 1,2,4,8...units far away
		- Rehashing: we hash the result again in order to find an empty slot



			   Average case         Worst case
Space                       O(n)               	   O(n)
Search                      O(1)               	   O(n)
Insert                      O(1)               	   O(n)
Delete                      O(1)               	   O(n)

"""


"""
* Hashtable dynamic resizing

	--Load factor: number of entries divided by the number of slots / buckets

	n/m this is the load factor. It is 0 if the hashtable is empty, it is 1 if the hashtable is full.

		- if the load factor is approximately 1 --> it means it is nearly full: the performance will decrease, the operations will be slow
		- if the load factor is approximately 0 --> it means it is nearly empty: there will be a lot of memory wasted

			SO: dynamic resizing is needed something.

	--Dynamic resizing:
		- Performance depends on the load factor: what is the number of entries and number of buckets ratio
		- Space-time tradeoff is important: the solution is to resize table, when its load factor exceeds given threshold
		- Java: when the load factor is greater than 0.75, the hashmap will be resized automatically
		- Python: the threashold is 2/3 ~ 0.66

			1.) hash values depend on table's size so hashes of entries are changed when resizing and algorithm can't just copy data from old storage to new one
			2.) resizing takes O(n) time to complete, where n is a number of entries in the table This fact may make dynamic-sized hash tables inappropriate for real-time applications


	-- Applications:

		- Databases: sometimes search trees, sometimes hashing is better
		- Counting given word occurence in a particular document
		- Storing data + lookup tables (password checks...)
		- Lookup tables in huge networks (lookup for IP addresses)
		- The hashing technique can be used for substring search
			(Rabin-karp algorithm)
"""


"""
* Hashfunction linear probing python
	
	key:apple
		-- > we can define the hashfunction: what is important that it should return
			an integer (the index of the arrayslot)
		-- > we can have the ASCII values for the characters
		-- > sum them up + use modulo operator to transform the final index into a valid range

		(a/p/p/l/e 97/112/112/108/101)
		97 + 112 + 112 + 108 + 101 = 530

		// we have to normalize it with the size of the underlying array

"""

class HashTable(object):

	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size

	# Linear probing insert implementation in python

	def put(self, key, data):

		index = self.hashfunction(key)

		while self.keys[index] is not None:
			if self.keys[index] == key:
				self.values[index] = data #update
				return

			# rehash try to find another slot
			index = (index+1)%self.size

		# insert
		self.keys[index] = key
		self.values[index] = data


	def get(self, key):

		index = self.hashfunction(key)

		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]

			index = (index+1) %self.size
		# it means the key is not present in the associative array
		return None


	def hashfunction(self, key):
		sum = 0
		for pos in range(len(key)):
			sum = sum + ord(key[pos])

		return sum%self.size

# Linear probing retrieve implementation in python
if __name__ == "__main__":

	table = HashTable()

	table.put("apple", 10)
	table.put("car", 20)
	table.put("tomatoe", 30)
	table.put("table", 40)

	print(table.get("table"))





# Dictionary in python
dict = {'Joe':14, 'Patbi':25, 'Emily':23}

#print(dict['Joe']) #O(1)

dict['Joe'] = 18

# print (dict['Joe'])

# dict.clear()
# del dict

#print( dict.items() )
#print( dict.keys() )

print( dict.items() )



"""
* Tries-ternary search tree in data structure

	- With the help of tries we can search and sort strings very very efficiently
	- The problem is that tries consume a lot of memory, so we should use ternary search trees instead which stores less references and null objects
	- TST stores characters or strings in nodes 
	- Each node has 3 children: less (left child), equal (middle child) or greater (right child)
	- Can we balance TST-s with rotations? Yes, but it does not worth the trouble
	- It can be used instead of hashmap: it is as efficient as hashing
	- Hashing need to examine the entire string key ...TST does not

In general we have as many pointers / edges from every node as the number of characters in the alphabet

We have to define an alphabet in advance + ALPHABET_SIZE
	For example: in english alphabet there are 26 characters, so ALPHABET_SIZE = 26--> 26 pointers from every node


	- TST supports sort operation
	- So: TST is better than hashing --> especially for search misses + flexible than BST (usually there is no perfect hash function)

	--- Conclusion: TST is faster than hashmap and more flexible than binary search trees

"""



"""
* Insertion in tries in data structure-python

	- PUT: with this operation we would like to insert a new element into the ternary search tree with a given key
		
		-- if the character is smaller alphabetically: we go to the left
		-- if the character is equal: we go to the middle child
		-- if the character is greater alphabetically: go to the right
"""


"""
* Searching in tries in data structure-python
	
	get: with this operation we would like to get an item from the ternary search tree with a given key

	IMPORTANT:
		- hashmap: we generate an index from the key with the hashfunction.
			We use every single character of the key

		- TST: we may come to the conclusion that there is no value with a given key 
			without considering every character 
			For example: we may return after the second character

		Conclusion: for mismatch --> TST is faster !!!
				For exemple: in LZW data compression there are several mismatches

"""



"""
* Application in tries in data structure

	- We should combine tries with TST
	- At the root: it is a trie with many many children
	- At lower levels it becomes a TST with 3 children only
	- This combination is quite efficient

-- TST vs hashing
	
	-- Hashing

		- Need to examine the entire key (because that is the way the hash function works)
		- Search hits and misses cost the same
		- The running time and performance relies heavily on the hashfunction
		- Does not support as many operations as TST (sorting)	

	-- TST

		- Works only for strings
		- Only examines just enough key characters
		- Search miss may only involve a few character
		- Support more operations ( sorting )
		- Faster than hashing ( for misses especially ) and more flexible than BST

	-- How do hashfunctions work?
		this is the key

		We have to transform the key into an array index ~ we can use ASCII values for the characters: sum them up + use % modulo operator to avoid index out of bound error !!!

	We Have To Examine Every character In The Key !!!

	-- Applications:

		- It can be used to implement the auto-complete feature very very efficiently
		- Can be used for spell-checkers
		- Near-neighbor searching ( of which a spell-check is a special case)
		- For databases especially when indexing by several non-key fields is desirable
		- Very important in package routing on WWW --> the router direct the packages in the direction of the longest prfix. It can be found very quickly with the hepl of TST-s
		- Prefix matching ~ google search
			- we can use DFS instead as well
"""


"""
* Implementation of tries in python

	1 - https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
"""



"""
* Red black tree example in data structure

	https://www.askpython.com/python/examples/red-black-tree-in-python
"""




"""
* Red black tree vs AVL in data structure
	
	1 - https://www.baeldung.com/cs/red-black-tree-vs-avl-tree

	2 - https://www.formosa1544.com/2021/07/02/build-the-forest-in-python-series-avl-tree-vs-red-black-tree
"""



"""
* Graph in data structure
	
	- Graphs G(V,E) are mathematical structures to model pairwise relations between given objects
	- A graph is made up of vertices/nodes and edges
	- There are two types of graphs: directed and undirected graphs

We know what are graphs First of all how to model them in programming languages ?
	
	- adjacency matrixes
	- edge list representation

1.) adjacency matrixes
	
	We have an A matrix constructed out of the vertices of the graph:

		--> the A(i,j) value in the matrix is 1 if there is a connection between node i and node j
		--> otherwise A(i,j) is 0

2.) edge list representation
	
	We create a Vertex class

		- it stores the neighbors accordingly

			class Vertex 

				vertexName;
				visited;
				Vertex[]neighbors;

	Graphs Applications:

		- shortest path algorithm (GPS, high frequency trading ...)
		- graph traversing: web crawlers for Google
		- spanning trees
		- maximum flow problem: lots of problems can be reduced to maximum flow
		- because there are two representations for graphs: we can handle these problems with matrixes as well
			// thats why most Google's algorithms have something to do with matrix relatedoperations although they are graph algorithms

"""



"""
* Breadth-first search in data structure

	- What is it good for ?
	- We have a graph and we want to visit every node --> we can do it with BFS
	- We visit the neighbors then neighbors of these new vertices and so on
	- We visit every vertex exactly once
	- Running time complexity: O(V+E)
	- Memory complexity is not good: we have to store lots of references
	- Thats why DFS is usually preferred
	- BUT it constructs a shortest path: Dijkstra algorithm does a BFS if all the edge weights are equal to 1


we have an empty queue at the beginning and we keep checking whether we have visited the given node or not
	~ keep iterating until queue is not empty

bfs(vertex)

	Queue queue
	vertex set visited true
	queue.enqueue(vertex)

	while queue not empty
		actual = queue.dequeue()

		for v in actual neighbors
			if v is not visited
				v set visited true
				queue.enqueue(v)


		  ITERATION

--- Applications:

	- In artificial intelligence / machine learning it can prove to be very important: robots can discover the surrounding more easily with BFS than DFS
	- It is also very important in maximum flow: Edmonds-karp algorithm uses BFS for finding augmenting paths
	- Cheyen's algorithm in garbage collection --> it help to maintain active references on the heap memory
	- It uses BFS to detect all the references on the heap
	- Serialization / deserialization of a tree like structure (for example when order does matter) --> it allows the tree to be reconstructed in an efficient manner !!!

"""



# Breadth-first search implementation in python

class Node(object):

	def __init__(self, name):
		self.name = name;
		self.adjacencyList = [];
		self.visited = False;
		self.predecessor = None;

class BreadthFirstSearch(object):

	def bfs(self, startNode):

		queue = [];
		queue.append(startNode);
		startNode.visited = True;

		while queue:

			actualNode = queue.pop(0);
			print("%s " % actualNode.data);

			for n in actualNode.adjacencyList:
				if not n.visited:
					n.visited = True;
					queue.append(n);

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");

node1.adjacencyList.append(node2);
node2.adjacencyList.append(node3);
node2.adjacencyList.append(node4);
node4.adjacencyList.append(node5);

bfs = BreadthFirstSearch();
bfs.bfs(node1);



"""
* Depth first search in data structure

	- Depth-first search is a widely used graph traversal algorithm besides breadth-first search
	- It was investigated as strategy for solving mazes by Trémaux in the 19th century
	- It explores as far possible along each branch before backtracking // BFS was a layer-by-layer algorithm
	- Time complexity of traversing a graph a graph with DFS: O(V+E)
	- Memory complexity: a bit better than that of BFS

RECURSION
-----------
dfs(vertex)

	vertex set visited true
	print vertex

	for v in vertex neighbors
		if v is not visited
			if v is not visited
			dfs(v)


ITERATION
-----------
dfs(vertex)
	
	Stack stack
	vertex set visited true
	stack.push(vertex)


	while stack not empty
		actual = stack.pop()

		for v in actual neighbors
			if v is not visited
				v set visited true
				stack.push(v)


----Applications

	- Topological ordering
	- Kosaraju algorithm for finding strongly connected components in a graph which can be proved to be very important in recommendation systems (Youtube)
	- Detecting cycles (checking whether a graph is a DAG or not )
	- Generating mazes OR finding way out of a maze

----Symmetry in DFS:

We can go to the opposite direction,
it is going to be a valid DFS as well !!!

"""




# Depth first search implementation in python
class Node(object):
	def __init__(self, name):
		self.name = name;
		self.adjacenciesList = [];
		self.visited = False;
		self.predecessor = None;

class DepthFirstSearch(object):

	def dfs(self, node):

		node.visited = True;
		print("%s " % node.name);

		for n in node.node.adjacenciesList:
			if not n.visited:
				self.dfs(n);

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");

node1.adjacenciesList.append(node2);
node1.adjacenciesList.append(node3);
node2.adjacenciesList.append(node4);
node4.adjacenciesList.append(node5);

dfs = DepthFirstSearch();
dfs.dfs(node1);



"""
* BFS vs DFS in data structure

	- Memory complexity: BFS vs DFS

		Breadth-first search: O(N)
		Depth-first search: O(logN)

	That's why depth-first search is preferred most of the times Ok, there may be some situations where BFS is better ~ artificial intelligence, robot movements ....

"""


"""
* Dijkstra algorithms in data structure

	- Shortest path problem: finding a path between two vertices in a graph such that the sum of the weights of its edges is minimized
	- Dijkstra algorithm
	- Bellman-Ford algorithm
	- A*search
	- Floyd-Warshall algorithm
	- It was constructed by computer scientist Edsger Dijkstra in 1956
	- Dijkstra can handle positive edge weights // Bellman-Ford algorithm can have negative weights as well
	- Several variants: it can find the shortest path from A to B, but it is able to construct a shortest path tree as well --> defines the shortest paths from a source to all the other nodes
	- This is asymtotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights
	- Dijkstra's algorithm time complexity: O(V*logV + E)
	- Dijkstra's algorithm is a greedy one: it tries to find the global optimum with the help of local minimum --> it turns out to be good
	- It is greedy --> on every iteration we want to find the minimum distance to the next vertex possible --> appropriate data structure
		heaps (binary or Fibonacci) or in general a priority queue

"""


"""
* Dijkstra algorithms logic in data structure

	-- Dijkstra algorithm: Pseudocode

class Node
	name
	min_distance
	Node predecessor


function DijkstraAlgorithm(Graph, source)
	
	distance[source] = 0
	create vertex queue Q

	for v in Graph
		distance[v] = inf
		predecessor[v] = undefined // previous node in the shortest path
		add v to Q

	while Q not empty
		u = vertex in Q with min distance // this is why to use heaps
		remove v from Q

		for each neighbor v of v
			tempDist = distance[u] + distBetween(u,v)
			if tempDist < distance[v]
				distance[v] = tempDist
				predecessor[v] = u

	return distance[] // contains the shortest distances from source to other nodes
"""


"""
* Dijkstra algorithms real time example
	
	Learn more here:

		https://builtin.com/software-engineering-perspectives/dijkstras-algorithm

"""


"""
* Bellman ford algorithms in data structure
	
	- Invented in 1958 by Bellman and Ford independently
	- Slower than Dijkstra but more robust: it can handle negative edge weights too
	- Dijkstra algorithm choose the edge greedely, with the lowest cost: Bellman-Ford relaxes all edges at the same time for V-1 iteration
	- Running time is O(V*E)
	- Does V-1 iteration + 1 to detect cycles: if cost decreases in the V-th iteration, than there is a negative cycle, because all the paths are traversen up to the V-1 iteration

--- 1970: Yen optimization:

	- Yen algorithm: it is the Bellman-Ford algorithm with some optimization.
	- We can terminate the algorithm if there is no change in the distances between two iterations.
	- We use the same technique in bubble sort

--- Applications:
	
	- Cycle detection can prove to be very important
	- Negative cycles as well --> we have to run the Bellman-Ford algorithm that can handle negative edge weights by default
	- On the FOREX market it can detect arbitrage situations

"""




# Bellman ford algorithms in python-1
import sys;

class Node(object):

	def __init__(self, name):
		self.name = name;
		self.visited = False;
		self.predecessor = None;
		self.adjacenciesList = [];
		self.minDistance = sys.maxsize;

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;

class BellmanFord(object):

# Bellman ford algorithms in python-2

	HAS_CYCLE = False;

	def calculateShortestPath(self, vertexList, edgeList, startVertex):
		startVertex.minDistance = 0;

	for i in range(0, len(vertexList)-1):
		for edge in edgeList:
			u = edge.startVertex;
			v = edge.targetVertex;

			newDistance = u.minDistance + edge.weight;

			if newDistance < v.minDistance:
				v.minDistance = newDistance;
				v.predecessor = u;

	for edge in edgeList:
		if self.hasCycle(edge):
			print("Nagative cycle detected...");
			BellmanFord.HAS_CYCLE = True;
			return;

def hasCycle(self, edge):
	if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
		return True;
	else:
		return False;

def getShortestPathTo(self, targetVertex):

	if not BellmanFord.HAS_CYCLE:
		print("Shortest  path exists with value: ", targetVertex.minDistance);

		node = targetVertex;

		while node is not None:
			node = node.predecessor;
	else:
		print("Negative cycle detected...");

# Bellman ford algorithms in python-3
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");
node7 = Node("G");
node8 = Node("H");

edge1 = Edge(5, node1,node2);
edge2 = Edge(6, node1,node6);
edge3 = Edge(9, node1,node5);
edge4 = Edge(15, node2,node4);
edge5 = Edge(12, node2,node3);
edge6 = Edge(4, node2,node8);
edge7 = Edge(7, node6,node3);
edge8 = Edge(6, node8,node6);
edge9 = Edge(5, node5,node8);
edge10 = Edge(4, node5,node6);
edge11 = Edge(20, node5,node7);
edge12 = Edge(1, node6,node3);
edge13 = Edge(13, node6,node7);
edge14 = Edge(3, node3,node4);
edge15 = Edge(11, node3,node7);
edge16 = Edge(9, node4,node7);


node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node1.adjacenciesList.append(edge3);
node2.adjacenciesList.append(edge4);
node2.adjacenciesList.append(edge5);
node2.adjacenciesList.append(edge6);
node8.adjacenciesList.append(edge7);
node8.adjacenciesList.append(edge8);
node5.adjacenciesList.append(edge9);
node5.adjacenciesList.append(edge10);
node5.adjacenciesList.append(edge11);
node6.adjacenciesList.append(edge12);
node6.adjacenciesList.append(edge13);
node3.adjacenciesList.append(edge14);
node3.adjacenciesList.append(edge15);
node4.adjacenciesList.append(edge16);


vertexList = (node1,node2,node3,node4,node5,node6,node7,node8);
edgeList = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16);

algorithm = BellmanFord();
algorithm.calculateShortestPath(vertexList, edgeList, node1);
algorithm.getShortestPathTo(node7);


"""
* Shortest path algorithms

	--- DAG shortest path

		- If the graph is a DAG, so there is no directed cycles, it is easier to find shortest path
		- We sort the vertices into topological order: we iterate throught the topological order relaxing all edges from the actual vertex
		- Topological sort algorithm computers shortest path tree in any edge weighted (can be negative) DAG in time O(E+V)
		- It is much faster than Bellman-Ford or Dijstra
		- Applications: solving knapsack-problem
		- GPS, vehecule routing and navigation
		- Detecting arbitrage situations in FX
		- RIP "Routing Information Protocol"
		- This is a distributed algorithm
			- Each node calculates the distances between itself and all other nodes and stores this information as a table
			- Each node sends its table to all adjacent nodes
			- When a node receives distance tables from its neighbors, it calculates the shortest routes to all other nodes and updates its own table to reflect any changes

	--- Avidan-Shamir method

		- When we want to shrink an image for example in the browser or on a smartphone without distortion
		- We want to make sure the image will not deform
		- We have to eliminate the least significant bit strings
		- We set up an "energy function": and remove the connected string of pixels containing the least energy
		- Photoshop, GIMP use it
		- We build a huge graph: vertices are the pixels and the edges are pointing from every vertex to its downward 3 neighbours
		- The energy function determines what the edge weights will be
		- It's acyclic: we can use topological order shortest path to find the string of pixels to be removed

	
	--- Longest path problem

		- Problem of finding a simple path of maximum length in a given graph
		- No polynomial time algorithm !!! NP-hard problem
		- It has a linear time solution for directed acyclic graphs (DAG) which has important applications in finding the critical path in scheduling problems
		- We just have to negate the edge weights and run shortest path algorithm
		- We have to use Bellman-Ford algorithm because negative edges can occur
		- Application: Parallel job scheduling problem
		- Given a set of jobs with durations and precedence constraints, schedule the jobs - by finding a start time to each - so as ta achive the minimum completion time, while respecting the constraints
	

	--- CPM: critical path method
		
		- The method was first used between 1940 and 1943 in the Manhattan project
		- Problem formulation: we want an algorithm for scheduling a set of project activities so that the total running time will be as minimal as possible
		- The algorithms needs
		- A list of all activities reuired to complete the project
		- The time (duration) that each activity will take to complete
		- The dependencies between the activities



"""



"""
* Union find data structure
	
	- Also known as union-find data structures
	- Data structure to keep track of a set of elements partitioned into a number of disjoint (non everlapping) subsets
	- Three main operations: union and find makeSet
	- Disjoint sets can be represented with the help of linked lists but usually we implemented as a tree like structure
	- In kruskal algorithm it will be useful: with disjoint sets we can decide in approximately O(1) time whether two vertexes are in the same set or not

--- makeSet

function makeSet(x)
	x.parent = x

So the make sets operation is uite easy to implement ~ we set the parent of the given node to be itself
	Basically we create a district set to all the items/nodes

--- find

function find(x)
	if x.parent == x
		return x
	else
		return find(x.parent)

Several items can belong to the same set --> we usually represent the set with one of its items "representative of the set"
	When we search for an item with find() then the operation is going to return with the representative

--- union

function union(x,y)
	xRoot = find(x)
	yRoot = find(y)

	xRoot.parent = yRoot

The union operation is merge two disjoint sets together by connecting them according to the representatives
	
	PROBLEM: this tree like structure can become unbalanced

		1. union by rank --> always attach the smaller tree to the root of larger one
			The tree will become more balanced: faster
		2. path compression --> flattening the structure of the tree 
			We set every visited node to be connected to the root directly

--- rank: basically the depth of the tree

	The rank of the set is eual to the rank of the representative // ~ the root node

	We attack the smaller tree to the larger one --> it means we attack the tree with smallest rank to the tree with highest rank

--- pathCompression

function find(x)
	if x.parent!=x
		x.parent = find(x.parent)
	return x.parent


--- Applications

	- It is used mostly in Kruskal-algorithm implementation
	- We have to check whether adding a given edge to the MST would form a cycle or not
	- For checking this --> union-find data structure is extremly hepful
	- We can check whether a cycle is present --> in asymtotically O(1) constant time complexity

"""



"""
* Spanning tree in data structure

	--- Spanning trees:

		- A spanning tree of an undirected G graph is a subgraph that includes all the vertices og G
		- In general, a tree may have several spanning trees
		- We can assign a weight to each edge
		- A minimum spanning tree is then a spanning tree with weight less than or equal to the weight of every other spanning tree
		- Has lots of applications: in big data analysis, clustering algorithms, finding minimum cost for a telecommunications company laying cable to a new neighborhood
		- Standard algorithms: Prim's-Jarmik, Kruskal --> greedy algorithms

	--- Kruskal-algorithm:

		- We start edges according to their edge weights
		- It can be done in O(N*logN) with mergesort or quicksort
		- Union find data structure: "disjoint set"

			- We start adding edges to the MST and we want to make sure there will be no cycles in the spanning tree. It can be done in O(logV) with the help of union find data structure
			- We Vould use a a heap instead sorting the edges in the beginning but the running time would be the same. So sometimes Kruskal's algorithm is implemented with priority queues
			- Worst case running time: O(E*logE), so we can use it for huge graphs too
			- If the edges are sorted: the algorithm will be quasi-linear
			- If we multiply the weights with a constant or add a constant to the edge weights: the result will be the same
				// in physics, an invariant is a property of the system that remains unchanged under some transformation

				In Kruskal algorithm, spanning trees are invariant under the transformation of these weights (addition, multiplication)
	
	--- 
"""




# Kruskal algorithms in python-1

class Vertex(object):

	def __init__(self, name):
		self.name = name;
		self.node = node;

class Node(object):

	def __init__(self, height, nodeId, parentNode):
		self.height = height;
		self.nodeId = nodeId;
		self.parentNode = parentNode;

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex);
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;

	def __cmp__(self, otherEdge):
		return self.cmp(self.weight, otherEdge.weight);

	def __lt__(self, other):
		selfPriority = self.weight;
		otherPriority = other.weight;
		return selfPriority < otherPriority;

# Kruskal algorithms in python-2
class DisjointSet(object):

	def __init__(self, vertexList):
		self.vertexList = vertexList;
		self.rootNodes = [];
		self.nodeCount = 0;
		self.setCount = 0;
		self.makeSets(vertexList);

	def find(self, node):

		currentNode = node;

		while currentNode.parentNode is not None:
			currentNode = currentNode.parentNode;

		root = currentNode;
		currentNode = node;

		while currentNode is not root:
			temp = currentNode.parentNode;
			currentNode.parentNode = root;
			currentNode = temp;

		return root.nodeId;

	def merge(self, node1, node2):

		index1 = self.find(node1);
		index2 = self.find(node2);	

		if index1 == index2:
			return; #they are in the same set

		root1 = self.rootNodes(index1);
		root2 = self.rootNodes(index2);

		if root1.height < root2.height:
			root1.parentNode = root2;
		elif root1.height > root2.height:
			root2.parentNode = root1;
		else:
			root2.parentNode = root1;
			root1.height = root1.height + 1;

	def makeSets(self, vertexList):
		for v in vertexList:
			self.makeSet(v);

	def makeSet(self, vertex):
		node = Node(0, len(self.rootNodes), None);
		vertex.parentNode = node;
		self.rootNodes.append(node);
		self.setCount = self.setCount + 1;
		self.nodeCount = self.nodeCount + 1;

# Kruskal algorithms in python-3
class KruskalAlgorithm(object):

	def spanningTree(self, vertexList, edgeList):

		disjointSet = DisjointSet(vertexList);
		spanningTree = [];

		edgeList.sort();

		for edge in edgeList:

			u = edge.startVertex;
			v = edge.targetVertex;

			if disjointSet.find(u.node) is not disjointSet.find(v.node):
				spanningTree.append(edge);
				disjointSet.merge(u.node, v.node);

		for edge in spanningTree:
			print(edge.startVertex.name," - ", edge.targetVertex.name);	

#Kruskal algorithms in python-4
vertex1 = Vertex("a");
vertex2 = Vertex("b");
vertex3 = Vertex("c");
vertex4 = Vertex("d");
vertex5 = Vertex("e");
vertex6 = Vertex("f");
vertex7 = Vertex("g");

edge1 = Edge(2, vertex1, vertex2);
edge2 = Edge(6, vertex1, vertex3);
edge3 = Edge(5, vertex1, vertex5);
edge4 = Edge(10, vertex1, vertex6);
edge5 = Edge(3, vertex2, vertex4);
edge6 = Edge(3, vertex2, vertex5);
edge7 = Edge(1, vertex3, vertex4);
edge8 = Edge(2, vertex3, vertex6);
edge9 = Edge(4, vertex4, vertex5);
edge10 = Edge(5, vertex4, vertex7);
edge11 = Edge(5, vertex6, vertex7);

vertexList = [];
vertexList.append(vertex1);
vertexList.append(vertex2);
vertexList.append(vertex3);
vertexList.append(vertex4);
vertexList.append(vertex5);
vertexList.append(vertex6);
vertexList.append(vertex7);

edgeList = [];
edgeList.append(edge1);
edgeList.append(edge2);
edgeList.append(edge3);
edgeList.append(edge4);
edgeList.append(edge5);
edgeList.append(edge6);
edgeList.append(edge7);
edgeList.append(edge8);
edgeList.append(edge9);
edgeList.append(edge10);
edgeList.append(edge11);

algorithm = KruskalAlgorithm();
algorithm.spanningTree(vertexList, edgeList)



# Prims algorithms in python-1

import heapq;

class Vertex(object):

	def __init__(self, name):
		self.name = name;
		self.visited = False;
		self.predecessor = None;
		self.adjacenciesList = [];

	def __str__(self):
		return self.name;

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;

	def __cmp__(self, otherEdge):
		return self.cmp(self.weight, otherEdge.weight);

	def __lt__(self, other):
		selfPriority = self.weight;
		otherPriority = other.weight;
		return selfPriority < otherPriority;

# Prims algorithms in python-2

class PrimsAlgo(object):
	def __init__(self, unvisitedList):
		self.unvisitedList = unvisitedList;
		self.spanningTree = [];
		self.edgeHeap = [];
		self.fullCost = 0;

	def calculateSpanningTree(self, vertex):

		self.unvisitedList.remove(vertex);

		while self.unvisitedList:

			for edge in vertex.adjacenciesList:
				if edge.targetVertex in self.unvisitedList:
					heapq.heappush(self.edgeHeap, edge);

			minEdge = heapq.heapop(self.edgeHeap);
			self.spanningTree.append(minEdge);
			print("Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name, minEdge.targetVertex.name));
			self.fullCost = self.fullCost + minEdge.weight;

			vertex = minEdge.vertex;
			self.unvisitedList.remove(vertex);


	def getSpanningTree(self):
		return self.spanningTree;		

# Prims algorithms in python-3

node1 = Vertex("A");
node2 = Vertex("B");
node3 = Vertex("C");

edge1 = Edge(100,node1,node2);
edge2 = Edge(100,node2,node1);
edge3 = Edge(1000,node1,node3);
edge4 = Edge(1000,node3,node1);
edge5 = Edge(0.01,node3,node2);
edge6 = Edge(0.01,node2,node3);


node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge3);
node2.adjacenciesList.append(edge2);
node2.adjacenciesList.append(edge6);
node3.adjacenciesList.append(edge4);
node3.adjacenciesList.append(edge5);


unvisitedList = [];
unvisitedList.append(node1);
unvisitedList.append(node2);
unvisitedList.append(node3);


algorithm = PrimsAlgo(unvisitedList);
algorithm.calculateSpanningTree(node1);



"""
* Application of spanning tree
	
--- 1) Optimizing road / cable/pipe length

	- We have N cities
	- We have to make sure that every city can be reached of roads
	- So the naive approach is to connect every city with every other city
	- Not the optimal solution
	- We have to find the minimum spanning tree: in order to connect all of the cities with the lowest cost possible (so the minimum length of roads)
	- Same problems --> want to lead in internet to a region or electicity or building motorways

--- 2) K-means clustering:
	
	- We want to classify similar items
	- For example dots in the 2 dimensional plane
	- The dots that are closer to reach other than to any other dots --> will be in the same cluster
	- We construct a minimum spanning tree --> and remove the N-1 most expensive edges if we want to make N clusters
	(kruskal algorithms: sort the edges in ascending order)

--- 3) Routing in LAN:

	- The spanning tree protocol (STP) ensures a loop-free topology for any bridged Ethernet local area network
	- Each switch would infinitely duplicate the first broadcast --> because there's nothing to prevent loops
	- The idea behind a spanning tree topology is that bridges can discover a subset of the topology that is loop-free: that's the tree
	- STP also makes sure there is enough connectivity to reach every portion of the network by spanning the entire LAN

"""



"""
* Sorting algorithms in data structure
	
	- A sorting algorithm is an algorithm that puts elements of an array in a certain order
	- Numbers --> numerical ordering
	- Strings, characters --> alphabetical ordering
	- Comparison based algorithms
		~ bubble sort, insertion sort, selection sort, merge sort, quicksort
	- Non-Comparison based sorting
		~ radix sort, bucket sort
	- Time complexity: O(N*N) or O(N log N) or O(N)
	- In place: strictly an in-place sort needs only O(1) memory beyond the items being sorted
		So an in place algorithm does not need any extra memory
	- Recursive: some sorting algorithms are implemented in a recursive manner --> the divide and conquer ones especially
			// merge sort and quicksort
	- Stable: stable sorting algorithms maintain the relative order of records with equal values


4|12|-3|32|16
-------------
An in place algorithm will not allocate any extra memory,
	for example a temporary array in order to make the sorting
	For merge sort --> we need some extra memory


4|12|-3|32|16 --------------> -3|4|12|16|32 (IN-Place: For example: quicksort)


Sometimes we have extra space when storing the numbers we want to sort --> not going to be in place

Why is it good to have algorithm that are in-place ?
	MEMORY EFFICIENT!!!


before sorting
--------------
4|12|-3|12|16
--------------
after sorting
--------------
-3|4|12|12|16

So the relative order of equal items remain the same The red 12 is after the yellow 12 even after sorting!!!
	Merge sort: stable
	Quick sort: unstable

For sorting N items --> we have to make log N! comparisons With Stringling-formula it can be reduced to N logN
	- so the Ω(N logN) time complexity is the lower bound for comparison based sorting algorithms
	- ok but we can achieve O(N) running time as far as sorting is concernded, such as bucket sort or radix sort 
		THESE ARE NOT COMPARISON BASED ALGORITHMS.

"""




"""
* Adaptive sorting algorithms
	
	- An adaptive algorithm is an algorithm that changes its behavior based on information available at runtime
	- Adaptive sort --> it takes advantage of existing order in its input
	- It benefits from local orders --> sometimes an unsorted array contains sequences that are sorted by default --> the algorithms will sort faster
	- Most of the times: we just have to modify existing sorting algorithms in order to end up with an adaptive one
	- Comparison based algorithms have optimal O(N logN) running time complexity
	- Adaptive sort takes advantage of the existing order of the input to try to achieve better times:maybe O(N) could be reached
	- The more presorted the input is, the faster it should be sorted 
	- IMPORTANT: nearly sorted sequences are common in practice
	- Heapsort,merge sort: not adaptive algorithms, do not take advantage of presorted sequences
	- Shell sort: adaptive algorithm so performs better if the input is partially sorted
"""




"""
* Bubble sort in data structure
	
	- Repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order
	- It is too slow and impratical for most problems even when compared to insertion sort
	- Bubble sort has worst-case and average complexity both O(N*N)
	- Bubble sort is not a pratical sorting algorithm
	- It will not be efficient in the case of a reverse-ordered collection
	- Stable sorting algorithm
	- In place algorithm --> does not need any additional memory
	- In computer graphics it is popular for its capability to detect a ery small error (like swap of just two elements) in almost-sorted arrays and fix it with just linear complexity O(N)
	- For example, it is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinates at a specific scan line (a line parallel to x axis) and with incrementing y their order change(two elements are swapped) only at intersections of two lines


bubbleSort(array)

	for i in range array.length-1
		for j in range array.length-1-i
			if array[j] > array[j+1]
				swap(array,j,j+1)

end

------------
-3|4|88|1|3
-----------
We keep considering fewer and fewer items, because on every iteration we consider one more item to be sorted

On every iteration we bubble up the largest item
-----------
-3|1|3|4|88


"""



"""
* Bubble sort in python
	
def bubble_sort(nums):

	for i in range(len(nums)-1):
		for j in range(0,len(nums)-1-i,1):
			if nums[j] > nums[j+1]:
				swap(nums,j,j+1)

	return nums

def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__== "__main__":

	a = [1,5,3,2,4,8,7]
	print(bubble_sort(a))

"""



"""
* Selection sort in data structure
	
	- Another O(N*N) running time sorting algorithm
	- Selection sort is noted for its simplicity and it has performance advantages over more complicated algorithms
	- Particularly useful where auxiliary memory is limited 
	- The algorithm divides the input list into two parts:
		- the subarray of items already sorted
		- and the subarray of items remaining to be sorted that occupy the rest of the array

	- The algorithm proceeds by finding the smallest element in the unsorted subarray
	- Exchange / swap it with the leftmost unsorted element --> putting it in sorted order
	- Moving the subarray boundaries one element to be right
	- It is an in place algorithm --> no need for extra memory
	- Selection sort almost always outperforms bubble sort
	- Not a stable sort --> does not preserve the order of keys with equal values
	- Quite counter-intuitive: selection sort insertion sort are both typically faster for small arrays // arrays with 10-20 items
	- Usual optimization method --> recursive algorithms switch to insertion sort or selection sort for small subarrays
	- Makes less writes than insertion sort --> this can be important if writes are significantly more expensive than reads,
	- For example with EEPROM or flash memory where every write lessens the lifespan of the memory


selectionSort(array)

	for i in range array.length-1
		index = i
		
		for j from i+1 to array.length
			if array[j] < array[index]
				index = j

		if index not i
			swap(array,index,i)

end



-3|4|1|88|3
------------
We find the minimum: for this we have to iterate through the whole array with Q(N) time complexity ~ linear search
------------
-3|1|3|4|88

"""



"""
* Selection sort in python

def selection_sort(nums):

	for i in range(len(nums)-1):

		index = i

		for j in range(i+1,len(nums),1):
			if nums[j] < nums[idex]:
			index = j

		if index != i:
			swap(nums,index,i)
	
	return nums

def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__ == "__main__":

	nums = [5,2,1,7,6,8,8,0]

	print(selection_sort(nums))

"""



"""
* Quicksort introduction-I
	
	- It is an efficient sorting algorithm
	- It was developed by Tony Hoare in 1959 // the same person who invented quickselect algorithm
	- A well implemented quicksort can outperforms heapsort and mergesort --> the main competitors
	- A comparison based algorithm --> not able to be faster than linearithmic time complexity
	- The efficient implementation of quicksort is NOT stable --> does not keep the relative order of items with equal value
	- It is in-place --> does not need any additional memory
	- On average case it has O(N logN) running time
	- But the worst case running time is quadratic O(N*N)
	- It is widely used in programming languages 
			- Primitive types --> usually quicksort is used
			- Reference types / objects --> usually mergesort is used

	It is a divide and conquer algorithm

	- pick an element from the array: this is the pivot item
	- partition phase: rearrange the array so that all elements with values less than the pivot come after it // equal values can go either way 
	- recursively apply these steps on the subarrays

		BASE CASE FOR RECURSION: arrays of size zero or one never need to be sorted

	Choosing the pivot item
		It is very important --> if we keep choosing bad pivots, the running time will be quadratic

		1.) we can choose a pivot at random // usually it is working fine
		2.) choose the middle index of the array as the pivot


Pseudocode:

quicksort(array,low,high)
	
	if low >= high return

	pivot = partition(array,low,high)
	quicksort(array,low,pivot-1)
	quicksort(array,pivot+1,high)

end


partition(array,low,high)
	
	pivotIndex = (low+high) / 2
	swap(pivotIndex,high)

	i = low

	for j = low to high
		if array[j] <= array[high]
			swap(i,j)
			i++

	swap(i,high)

	return i

end


"""



"""
* Insertion sort in python

def insertion_sort(nums):

	for i in range(len(nums)):

		j = i

		while j > 0 and nums[j-1] > nums[j]:
			swap(nums,j,j-1)
			j = j- 1

	return nums

def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__ = "__main__":

	nums = [1,5,3,8,10,100,4]
	print(insertion_sort(nums))

"""


"""
* Insertion sort in data structure

	- It is a simple sorting algorithm that builds the final sorted array one item at a time
	- It has quadratic running time O(N*N)
	- On large datasets it is very inefficient but on arrays with 10-20 items it is quite good
	- Simple implementation
	- It is more efficient than other quadratic running time sorting procedures such as bubble sort or selection sort
	- Adaptive algorithm --> speeds up when array is already substantially sorted
	- Stable sort --> preserve the order of the items with equal keys
	- In-place algorithm --> does not need any additional memory
	- It is an online algorithm --> it can sort an array as it receives it for example downloading data from web
	- Hybrid algorithms uses insertion sort if the subarray is small enough Insertion sort is faster for small subarrays than quicksort
	- Variant of insertion sort is shell sort
	- Sometimes selection sort is better: thay are very similar algorithms
	- Insertion sort requires more writes because the inner loop can require shifting large sections of the sorted portion of the array
	- In general, insertion sort will write to the array O(n*n) times while selection sort will write only O(n) times
	- For this reason selection sort may be preferable in cases where writing to memory is significantly more expensive than reading --> for example flash memory


insertionSort(array)
	
	for i=1 to length(array)
		j = i

		while j > 0 and array[j-1] > array[j]
			swap(array,j,j-1)
			j = j-1
		end
	end
end


---------
While the previous item is greater than the given one,
we keep swapping them

~ that why there are so many shifts in insertion sort

55|-2|34|10|0|2|-5|12
----------------------
-5|-2|0|2|10|12|34|55

---------

"""



"""
* Quicksort introduction-II
	
quicksort(array,low,high)

	if low >= high return

	pivot = partition(array,low,high)
	quicksort(array,low,pivot-1)
	quicksort(array,pivot+1,high)

end


partition(array,low,high)
	
	pivotIndex = (low+high) / 2
	swap(pivotIndex,high)

	i = low

	for j=low to high
		if array[j] <= array[high]
			swap(i,j)
			i++

	swap(i,high)

	return i

end


23|6|6|-1|0|12|8|3|1
--------------------
Sort right subarray recursively
--------------------
-1|0|1|3|4|6|8|12|23


"""



"""
* Quicksort in python

de quick_sort(nums,low,high):

	if low >= high:
		return

	pivot_index = partition(nums,low,high)
	quick_sort(nums,low,pivot_index-1)
	quick_sort(nums,pivot_index+1,high)

def partition(nums,low,high):

	pivot_index = (low+high) // 2
	swap(nums,pivot_index,high)

	i = low

	for j in range(low,high,1):
		if nums[j] <= nums[high]:
			swap(nums,i,j)
			i = i + 1

	swap(nums,i,high)

	return i

def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__ == "__name__":

	nums = [-2,-1,0,1,0,-1,-2]
	quick_sort(nums,0,len(nums)-1)
	print(nums)

"""




"""
* Merge sort importance in data structure

	- Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945
	- Comparison based algorithm with running time complexity O(N logN)
	- It is a stable sorting algorithm
	- Not an in-place algorithm
	- Although heapsort has the same time bounds as merge sort --> heapsort requires only O(1) auxiliary space instead of merge sort's O(N)
	- Efficient quicksort implementations generally outperforms mergesort
	- Mergesort is often the best choice for sorting a linked list: in this situation it is relatively easy to implement a merge sort in such a way that it requires only O(1) extra space



			   Quicksort              Mergesort
In place                    Yes                      No
Stable                      No                       Yes
Time complexity             Quadratic sometimes      O(N logN)




	1- divide the array into two subarrays recursively
	2- sort these subarrays recursively with mergesort again
	3- if the is only a single item left in the subarray --> we consider it to be sorted by definition
	4- merge the subarrays to get the final sorted array



"""



"""
* Merge sort in data structure
	
	3-5-6-10   1-4-8

	So after the split operations: we have several distinct arrays that are already sorted: we have to merge these arrays into a single one

	-- We start at the beginning of the subarrays: we keep comparing them, we insert the smaller into the result array
	
	result array: 1-3-4-5-6-8-10

	Very important: we have to iterate through the left and right array if there are some more items left --> in this case the 10 in the left subarray


	Pseudocode:

	mergeSort(low,high)

		if(low >= high) return
		middle = (low + high) / 2

		mergeSort(low, middle)
		mergeSort(middle + 1, high)
		mergeSort(low, middle, high)
	end

"""





# Merge sort in python

def merge_sort(nums):

	if len(nums) == 1;
		return

	middle_index = len(nums) // 2

	left_half = nums[:middle_index]
	right_half = nums[middle_index:]

	merge_sort(left_half)
	merge_sort(right_half)

	i = 0
	j = 0
	k = 0

	while i<len(left_half) and j<len(right_half):
		if left_half[i] < right_half[i]
			nums[k] = left_half[i]
			i = i + 1
		else:
			nums[k] = right_half[j]
			j = j +1

		k = k + 1


	while i <len(left_half):
		nums[k] = left_half[i]
		k = k + 1
		i = i + 1

	while j < len(right_half):
		nums[k] = right_half[j]
		k = k + 1
		j = j + 1

if __name__ == "__main__":

	nums = [1,2,3,4,-5]
	merge_sort(nums)
	print(nums)	




"""
* Hybrid sorting algorithms

	- It combines more algorithms to solve a given problem
	- It choses one algorithm depending on the data or switching between them over the course of the algorithm
	- This is generally done to combine desired features of each, so that the overall algorithm is better than the individual components
	- Important: hybrid algorithm does not refer to simply combining multiple algorithms to solve a different problem but only to combining algorithms
		that solve the same problem --> but differ in other characteristics // such as performance
	- The technique can be used when sorting
	- Heapsort --> it has an advantage of a guaranteed running time O(N logN)
	- Quicksort --> optimal implementations are outperform both mergesort and heapsort
	- BUT quicksort can have quadratic running time when we keep choosing, bad" pivots
	- Solution: let's combine the two algorithms
	- Insertion sort: very efficient on small data(5-10 elements)
	- Mergesort / quicksort: asymptotically optimal on large dataset, but the overhead becomes significant if applying them to small datasets
	- Solution: let's combine the two algorithms
	- Highly optimized hybrid algorithm: timsort

		TIMSORT = INSERTION SORT + MERGESORT


-- Introsort:
	
	- Also known as introspective sort 
	- It is a hybrid sorting algorithm that provides both fast average performance and optimal worst-case performance
	- It begins with quicksort and switches to heapsort when quicksort becomes too slow
		INTROSORT = QUICkSORT + HEAPSORT 

-- Timsort:

	- Combines mergesort and insertion sort
	- It is a stable sorting algorithm
	- It was implemented by Tim Peters in 2002 for use in the Python programming language
	- Best case running time: O(N)
	- Worst case running time: O(N logN)
	- Worst case space complexity: O(N)

"""



"""
* Non comparison sorting

	-- Comparison based sorting:

		- What does comparison based sorting mean ?

		if nums[i] > nums[j]

				swap(i,j)

		We keep comparing items ( strings, characters, double ...)

			~ keep making decisions according to these comparisons

		Result: we have to make at least lg n ! comparisons to sort an array
	
		stirling formula yields: Ω(N log N)
			So this is a lower bound, we are not able to do any better !!!

	Can we do better ? Yes, the solution is not to use comparisons

		There are simpler algorithms that can sort a list using partial information about the kays
			For example: radix sort, bucket sort
"""




"""
* Counting sort in data structure

	- It operates by counting the number of objects that have each distinct key value
	- Integer sorting algorithm: we assume the values to be integers
	- And using arithmetic on those counts to determine the positions of each key value in the output sequence
	- It is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items
	- It can be used as a subroutine in redix sort
	- Because counting sort uses key values as indexes into an array --> it is not a comparison based sorting algorithm, so linearithmic running time can be reduced
	- Running time: O(N+K)
	- N --> number of items we want to sort
	- K --> difference between the maximum and minimum key values,
	basically the number of possible keys
	- Conclusion: it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items

	1 4 1 7 1 7 10 3  Initial array we want to sort

	Content value: 3
	Index: 1
	-----------
	Meaning: we have 3 items with key 1 in out original array

	Numerical ordering: 1,1,1,3,4,7,7,10

	Overall running time: O(k) + O(N) = O(N+K)

	Problem: k can be very very large, and the counting sort algorithm will be slow

	Allocate memory --> for an array size k, we want to track and count that how many occurances are there in the the original array for the given key

	1) Iterate through the original array O(N)
	2) The value in the array will be the index of the temporary array: we increment the counter there
	3) Traverse the array of counters ( array size k ) and print out the values O(k)
	4) It is going to yield the numerical ordering




Pseudocode:

countingSort(array, max, min)

	countArray = new array with size [max-min+1]

	for i in array
		increment countArray[i-min]
	end
	z = 0

	for i in array
		while countArray[i-min] > 0
			array[z] = 1
			z = z + 1
			countArray[i-min] = countArray[i-min] - 1
		end
	end
end

Counting sort is not in place, we do need some additional memory

max-min+1 going to determine the size of the array

Thats why counting sort can get slow if this countArray is huge

"""


"""
* Radix sort in data structure

-- Radix sort:

		- Can be very efficient, because there are no comparisons
		- So O(N) running time can be reached
		- Running time: O(K*N) where K is the number of digits in the input number
		- We sort the elements according to individual characters
		- It is a stable sorting algorithm

	-- LSD string sorting:

		- Least-significant-digit-first string sorting
		- Consider characters from right to left
		- We can use it to fixed length strings or fixed length numbers for example integers
		- Sort the characters at the last column...then keep going left and sort the columns independently
		- Typical interview question: how to sort one million 32-bit integers

	-- MSD string sort:

		- Most-significant-digit-first string sorting
		- Consider characters from left to right
		- It is sensitive to ASCII and Unicode representations
		- It has several advantages
			- MSD examines just enough characters to sort the key
			- CAN BE SUBLINEAR IN INPUT SIZE !!!
		- MSD access memory randomly ... not so efficient
		- Solution: we should combine it with quicksort ... this is the 3-way radix quicksort


"""


"""
* Associated array in python
	
	- Associative arrays / maps / dictionaries are abstract data types !!!
	- Composed of a collection of key-value pairs where each key appears only once in the collection
	- Most of the times we implement associative arrays with hashtables but binary search trees can be used as well
	- The aim is to reach O(1) time complexity for most of the operations

		Supported operations:
			- Adding key-value pairs to the collection
			- Removing key-value pairs from the collection 
			- Update existing key-value pairs
			- Lookup of value associated with a given key
"""