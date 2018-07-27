## Program to convert a binary tree to its mirror tree recursively


class Node(object):
	def __init__(self,key,parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None


def mirror_tree(root):

	if root is None:
		return 

	mirror_tree(root.left)
	mirror_tree(root.right)

	root.left, root.right = root.right, root.left


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





