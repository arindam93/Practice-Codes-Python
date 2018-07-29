## Program to find the path to node in a Binary Tree

## Complexity: O(n) where n is number of nodes
## Space: O(n)


class Node(object):
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

def buildTree(i,values):
	if i < len(values):
		return Node(values[i], left=buildTree((i+1)*2-1,values), right=buildTree((i+1)*2,values))



def path_find(root,value,path):

	if root is None:
		return root

	path.append(root.key)
	# print path

	# stopping criteria
	if root.key == value:
		return path

	if root.left != None and path_find(root.left, value, path):
		return path
	if root.right != None and path_find(root.right, value, path):
		return path

	# If not present in subtree rooted with root, remove
    # root from path (most important)
	path.pop()


## Driver code

values = [1,2,3,4,5,6,7,8]
root = buildTree(0,values)
path = []

## print all the nodes along the path leading to the value
lst = path_find(root,7,path)

print lst






