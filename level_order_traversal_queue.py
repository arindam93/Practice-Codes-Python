### Level order traversal of a Binary Tree (Breadth First traversal)

## Time complexity: O(N)

class Node(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

def level_order_traversal(root):
	if root is None:
		return

	queue = []
	queue.append(root)  ## push the root value into empty queue

	while len(queue) > 0:

		print queue[0].key         ## print the first value in queue
		curr_node = queue.pop(0)   ## dequeue the first value from queue, make it current node

		if curr_node.left is not None:
			queue.append(curr_node.left)
		if curr_node.right is not None:
			queue.append(curr_node.right)


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