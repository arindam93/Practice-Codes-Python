## Program to find lowest common ancestor in a Binary Tree using single tree traversal
## Here we don't need to calculate path to the values

## Complexity: O(n)

class Node(object):
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

def buildTree(i,values):
	if i < len(values):
		return Node(values[i], left=buildTree((i+1)*2-1,values), right=buildTree((i+1)*2,values))


def find_lca(root,value1,value2):

	if root is None:
		return root

	if root.key == value1 or root.key == value2:
		return root

	# Look for keys in left and right subtrees
	left_lca = find_lca(root.left, value1, value2)
	right_lca = find_lca(root.right, value1, value2)

	## if one value lies in left subtree and other one on right subtree, 
	## both the variables will return non NULL. Hence, LCA is the root
	if left_lca and right_lca:
		return root

	if left_lca is not None:
		return left_lca
	else:
		return right_lca



values = [1,2,3,4,5,6,7,8,9]
root = buildTree(0,values)
lca = find_lca(root,6,7)
print lca.key
