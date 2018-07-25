## Program to calculate diameter of a Binary Tree

## Simple Method
## Worst Time complexity: O(N*N) for skewed tree

class BSTNode(object):
	def __init__(self,key,parent=None):
		self.key = key 
		self.parent = parent
		self.left = None
		self.right = None


def height(root):
	if root is None:
		return 0
	else:
		lheight = height(root.left)
		rheight = height(root.right)

	return max(lheight, rheight) + 1

def diameter(root):
	if root is None:
		return 0

	else:
		left_height = height(root.left)
		right_height = height(root.right)

	ldiam = diameter(root.left)
	rdiam = diameter(root.right)

	## when the path passes through root
	# diam = left_height + right_height + 1
	return max(left_height + right_height + 1, max(ldiam,rdiam))




## Driver code

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

diam = diameter(root)
print "The diameter of the tree is: %d" %(diam)

