## Program to convert a binary tree to its mirror tree iteratively
## Complexity: O(n) where n is the number of nodes

class Node(object):
	def __init__(self,key,parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None


def mirror_tree(root):

	if root is None:
		return root

	queue = []
	queue.append(root)

	while len(queue) > 0:

		curr_node = queue.pop(0)

		curr_node.left, curr_node.right = curr_node.right, curr_node.left

		if curr_node.left is not None:
			queue.append(curr_node.left)

		if curr_node.right is not None:
			queue.append(curr_node.right)


def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print root.key
		inorder_traversal(root.right)


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(4)

print "The inorder traversal of the original tree is:"
inorder_traversal(root)

mirror_tree(root)

print "The inorder traversal of the mirrored tree is:"
inorder_traversal(root)





