#include<stdio.h>
#include<stdlib.h>

struct BSTnode
{
	int key;
	struct BSTnode* left;
	struct BSTnode* right;
};

struct BSTnode* newNode(int key)
{
	struct BSTnode* node = (struct BSTnode*)malloc(sizeof(struct BSTnode));
	node->key = key;
	node->left = NULL;
	node->right = NULL;

};

struct BSTnode* arr_bst(int arr[], int start, int stop)
{
	if (start>stop)
		return NULL;

	int mid = (start+stop)/2;
	struct BSTnode *root = newNode(arr[mid]);

	root->left = arr_bst(arr,start,mid-1);
	root->right = arr_bst(arr,mid+1,stop);

	return root;
};

void Preorder(struct BSTnode* node)
{
	if (node == NULL)
		return;
	printf("%d ",node->key);
	Preorder(node->left);
	Preorder(node->right);
};


int main()
{
	int arr[]= {1, 5, 6, 3, 4, 8, 9, 0, 7, 2};
	int n = sizeof(arr)/sizeof(arr[0]);

	struct BSTnode *root = arr_bst(arr, 0, n-1);
	printf("Preorder traversal of the balanced BST\n");
	Preorder(root);

	return 0;
}
