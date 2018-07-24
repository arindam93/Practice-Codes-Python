### Program to find height of a tree without recursion

## Idea is to traverse the tree level by level (level order traversal)
## using Queue (FIFO)

## Complexity: O(N) where N is the number of nodes in binary tree

class Node(object):
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None


def max_height(root):

	if root is None:
		return 0

	queue = []
	height = 0
	queue.append(root)

	while len(queue) > 0:

		curr_node = queue.pop(0)

		if curr_node.left is not None:
			queue.append(curr_node.left)
		if curr_node.right is not None:
			queue.append(curr_node.right)

		if curr_node.left is not None or curr_node.right is not None:
			height = height + 1

	return height

## Test code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.left.right = Node(9)


height = max_height(root)
print "The maximum height of the tree is:", height


