### Tree traversals in a Binary Tree

### Preorder / Inorder / Postorder traversal (Depth First traversal)

## Complexity: O(n) where n = number of nodes in the tree

class Node:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

def Inorder(root):   ### Left --> Root --> Right
	if root:
		Inorder(root.left)  ## recur on left child

		print (root.key)

		Inorder(root.right) ## recur on right child

def Preorder(root): ### Root --> Left --> Right

	if root:
		print (root.key)

		Preorder(root.left)
		Preorder(root.right)

def Postorder(root): ### Left --> Right --> Root

	if root:
		Postorder(root.left)
		Postorder(root.right)

		print (root.key)



## Test code

## Binary Tree

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

### Binary Search Tree (BST)

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(2)
# root.left.right = Node()
root.right.left = Node(6)
root.right.right = Node(11)


## returns a sorted array for BST
print "Inorder traversal of the binary tree is:"
Inorder(root)



print "Preorder traversal of the binary tree is:"
Preorder(root)


print "Postorder traversal of the binary tree is:"
Postorder(root)
