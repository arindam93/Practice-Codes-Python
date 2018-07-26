### Program to construct a Binary Tree given inorder and postorder traversals

class Node(object):
	def __init__(self,key,parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None



def BT_inorder_postorder(inorder, postorder, inStart, inEnd):

	global postorder_index

	if inStart > inEnd:
		return None

	root = Node(postorder[postorder_index])
	postorder_index -= 1

	## means there are no left or right child of the node
	if inStart == inEnd:
		return root


	inIndex = search(inorder, root.key, inStart, inEnd)

	root.right = BT_inorder_postorder(inorder,postorder,inIndex+1,inEnd)
	root.left = BT_inorder_postorder(inorder,postorder,inStart,inIndex-1)

	return root


def search(arr,val,start,end):

	for i in range(start,end+1):
		if arr[i] == val:
			return i

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print (root.key)
		inorder_traversal(root.right)



## Driver code

inorder_lst = [4, 8, 2, 5, 1, 6, 3, 7]
postorder_lst = [8, 4, 5, 2, 6, 7, 3, 1]

postorder_index = len(postorder_lst)-1

root = BT_inorder_postorder(inorder_lst,postorder_lst,0,len(inorder_lst)-1)

## check if the output is same as the given inorder list
inorder_traversal(root)



