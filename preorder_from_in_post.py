## Print Preorder traversal from given Inorder and Postorder traversals without constructing tree




def print_preorder(inorder, postorder, n):

	if postorder[-1] in inorder:
		root = inorder.index(postorder[-1])

	print postorder[-1]

	if root != 0: ## left subtree
		print_preorder(inorder[:root],postorder[:root],len(inorder[:root]))

	if root != n-1: ## right subtree
		print_preorder(inorder[root+1:],postorder[root:-1],len(inorder[root+1:]))


	# print preorder[0]


inorder = [4,2,5,1,3,6]
postorder = [4,5,2,6,3,1]

print_preorder(inorder,postorder,len(inorder))