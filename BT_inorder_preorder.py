### Program to construct a Binary Tree given inorder and preorder traversals

## Time Complexity: O(N^2). Worst case occurs when tree is left skewed, i.e. when
## the inorder and preorder traversals are just reverse of each other

class Node(object):
	def __init__(self,key,parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None



def BT_inorder_preorder(inorder, preorder, inStart, inEnd):

	global preorder_index

   	if (inStart > inEnd):
   		return None

   	root = Node(preorder[preorder_index])
 	preorder_index += 1

   	## if the node has no children then return the node
   	if inStart == inEnd:
   		return root

   	inIndex = search(inorder,root.key,inStart,inEnd)


	# Using index in Inorder Traversal, construct left 
    # and right subtrees
   	root.left = BT_inorder_preorder(inorder, preorder, inStart, inIndex-1)
   	root.right = BT_inorder_preorder(inorder, preorder, inIndex+1, inEnd)

   	return root


def search(arr,val,start,end):

	for i in range(start,end+1):
		if arr[i] == val:
			return i

def inorder_traversal(root):

	if root:
		inorder_traversal(root.left)
		print root.key
		inorder_traversal(root.right)




### Driver code

## initialise the preorder counter
preorder_index = 0
inorder_lst = [2,4,5,6,8,11]
preorder_lst = [5,4,2,8,6,11]

root = BT_inorder_preorder(inorder_lst, preorder_lst,0,len(inorder_lst)-1)

## check if returns the original inorder_lst
inorder_traversal(root)



