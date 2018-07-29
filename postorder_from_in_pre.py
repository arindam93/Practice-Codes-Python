## Print Postorder traversal from given Inorder and Preorder traversals


def print_postorder(inorder, preorder, n):

	if preorder[0] in inorder:
		root = inorder.index(preorder[0])

	if root != 0: ## left subtree
		print_postorder(inorder[:root],preorder[1:root+1],len(inorder[:root]))

	if root != n-1: ## right subtree
		print_postorder(inorder[root+1:],preorder[root+1:],len(inorder[root+1:]))


	print preorder[0]


inorder = [4,2,5,1,3,6]
preorder = [1,2,4,5,3,6]

print_postorder(inorder,preorder,len(inorder))