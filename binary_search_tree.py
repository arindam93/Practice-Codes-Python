### A binary search tree 
### Ops: find, insert, min, max, successor, predecessor, delete

class BSTNode(object):
	def __init__(self,key):
		self.key = key 
		self.parent = None
		self.left = None
		self.right = None


## Search key k

def search_key(root,k):

	if root is None:
		return 0

	elif k == root.key:
		return root

	elif k < root.key:
		return search_key(root.left,k)

	elif k > root.key:
		return search_key(root.right,k)


## Insert node k

def insert_key(root,k):

	if root is None:
		root = k

	else:
		if k.key < root.key:
			if root.left is None:
				root.left = k
			else:
				insert_key(root.left, k)

		else:
			if root.right is None:
				root.right = k
			else:
				insert_key(root.right, k)


## Returns the max entry in BST

def find_max(root):

	while root.right is not None:
		root = root.right

	return root.key


## Returns the min entry in BST

def find_min(root):

	while root.left is not None:
		root = root.left

	return root.key


## Inorder Successor of a node (larger than the node but smaller than everything else)

def next_larger(root,k):

	curr = search_key(root,k)

	if curr.right is not None:
		return find_min(curr.right)

	p = curr.parent
	while p is not None:
		if curr == p.left:
			break
		curr = p
		p = curr.parent

	return p


## Inorder Predecessor of a node (smaller than the node but bigger than everything else)

def next_smaller(root,k):

	curr = search_key(root,k)

	if curr.left is not None:
		return find_max(curr.left)

	p = curr.parent

	while p is not None:
		if curr == p.right:
			break
		curr = p
		p = curr.parent

	return p


## Delete a node

def delete(root,k):

	if root is None:
		return root

	## here we find the node to be deleted
	if k < root.key:
		root.left = delete(root.left, k)

	elif (k > root.key):
		root.right = delete(root.right, k)

	## now we found the node to be deleted
	else:
		## node with one child or no child
		if root.left is None:
			tmp = root.right
			root = None
			return tmp

		elif root.right is None:
			tmp = root.left
			root = None
			return tmp

		## node with left and right subtrees (2 children)
		succ = find_min(root.right)
		root.key = succ
		root.right = delete(root.right, succ)

	return root



## to check if the node is correctly inserted or not
## if correct, returns a sorted array
def inorder(root): 
	if root:
		inorder(root.left)
		print (root.key)
		inorder(root.right)




## Design the binary search tree
root = BSTNode(15)
root.left = BSTNode(10)
root.right = BSTNode(28)
root.left.parent = root.right.parent = root

root.left.left = BSTNode(5)
root.left.right = BSTNode(12)
root.left.left.parent = root.left.right.parent = root.left

root.right.left = BSTNode(25)
root.right.right = BSTNode(32)
root.right.left.parent = root.right.right.parent = root.right

root.right.right.left = BSTNode(29)
root.right.right.right = BSTNode(38)
root.right.right.left.parent = root.right.right.right.parent = root.right.right





### Scripts to check the functions

# op = search_key(root,32)
# insert_key(root,BSTNode(42))
# insert_key(root,BSTNode(18))
# inorder(root)
print "Max in BST is:", find_max(root)
print "Min in BST is:", find_min(root)

nextlarge = next_larger(root,12)
nextsmall = next_smaller(root,25)
print "Inorder Successor of node %d is: %d" %(12,nextlarge.key)
print "Inorder Predecessor of node %d is: %d" %(25,nextsmall.key)

root1 = delete(root,25)
inorder(root1)


