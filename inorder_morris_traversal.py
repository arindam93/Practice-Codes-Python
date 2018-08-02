## Program to print inorder traversal of a BST without recursion and without stack

## Morris Inorder Traversal

class Node(object):
	def __init__(self, key=None, parent=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

def buildTree(i,values):
	if i < len(values):
		return Node(values[i], left=buildTree((i+1)*2-1,values), right=buildTree((i+1)*2,values))


def morris_inorder_traversal(root):

	if root is None:
		return root

	curr = root

	while curr is not None:

		if curr.left is None:
			print curr.key
			curr = curr.right

		else:

			tmp = curr.left

			## finding the inorder predecessor
			while tmp.right is not None and tmp.right != curr:

				tmp = tmp.right

			# Make current as right child of its inorder predecessor
			if tmp.right is None:
				tmp.right = curr
				curr = curr.left

			# Revert the changes made in if part to restore the 
            # original tree i.e., fix the right child of predecssor
			else:
				tmp.right = None
				print curr.key
				curr = curr.right


values = [10,5,40,1,7,30,50]
root = buildTree(0,values)
morris_inorder_traversal(root) 






