### Program to calculate the maximum depth of a tree


## Method 1: Recursive (easy) method
## Time complexity: O(n) where n = no. of nodes in the tree

class Node(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

def max_depth_recursion(root):
	if root is None:
		return 0
	else:
		left_depth = max_depth_recursion(root.left)
		right_depth = max_depth_recursion(root.right)

	return max(left_depth,right_depth) + 1


def max_depth_iterative(root)

root = Node(6)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(15)
root.right.right.left = Node(12)
root.right.right.left = Node(18)

print "The maximum depth of the tree using recursion is:", max_depth_recursion(root)
