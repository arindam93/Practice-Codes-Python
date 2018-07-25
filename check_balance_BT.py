### Program to check whether a Binary Tree is balanced or not
### A tree is balanced only if the difference in height among the left and right subtree is at most 1


## Simple method
## Worst complexity: O(N*N) in case of skewed tree

class Node(object):
	def __init__(self,key,parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None


def max_depth_recursion(root):
	if root is None:
		return 0
	else:
		left_depth = max_depth_recursion(root.left)
		right_depth = max_depth_recursion(root.right)

	return max(left_depth,right_depth) + 1



def check_balance(root):

	if root is None:
		return True

	l_height = max_depth_recursion(root.left)
	r_height = max_depth_recursion(root.right)

	diff = abs(l_height - r_height)

	if diff <= 1 and check_balance(root.left) is True and check_balance(root.right) is True:
		return True
	


## Driver code

root = Node(6)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(15)
root.right.right.left = Node(12)
root.right.right.left = Node(18)
root.right.right.left.left = Node(17)
root.right.right.left.left.left = Node(16)

if check_balance(root):
	print "Balanced"
else:
	print "Unbalanced"


