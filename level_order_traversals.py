### Level order traversal of a Binary Tree (Breadth First traversal)

## Time complexity: O(N*N)

class Node(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None


def level_order_traversal(root):
	h = height(root)
	for d in range(h):
		print_current_level(root,d)

def print_current_level(root,level):
	if root is None:
		return
	if level == 0:
		print "%d" %(root.key)
	elif level > 0:
		print_current_level(root.left, level-1)
		print_current_level(root.right, level-1)

def height(node):
	if node is None:
		return 0       ## depth = 0 if there are no nodes
	else:
		left_height = height(node.left)
		right_height = height(node.right)

	return max(left_height,right_height) + 1


## Test code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "The level order traversal of the tree is:"
level_order_traversal(root)
