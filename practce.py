import sys
class TreeNode:
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data


def insert_tree(root, data):
	if root == None:
		newNode = TreeNode()
		newNode.set_data(data)
		root = newNode
		return root
	
	if data < root.get_data():
		if root.left == None:
			root.left = insert_tree(root.left , data)
		else:
			insert_tree(root.left , data)
		return root

	if data >= root.get_data():
		if root.right == None:
			root.right = insert_tree(root.right , data)
		else:
			insert_tree(root.right , data)
		return root


def print_tree(root):
	if root == None:
		return None
	queue = []
	queue.append(root)
	while len(queue) != 0:
		if queue[0].left != None:
			queue.append(queue[0].left)

		if queue[0].right != None:
			queue.append(queue[0].right)

		print(queue[0].get_data())
		queue.pop(0)

arr = list(map(int , input().strip().split(" ")))
closest = int(input())

def find_closest(root, closest, min_diff = sys.maxsize , value = None):
	if root == None:
		return value

	if root.get_data() == closest:
		min_diff = 0
		return closest


	temp = root	
	if temp.data > closest:
		if min_diff > (abs(temp.data - closest)):
			min_diff = (abs(temp.data - closest))
			value = temp.data
		return find_closest(temp.left , closest , min_diff, value)

	if temp.data < closest:
		if min_diff > (abs(temp.data - closest)):
			min_diff = (abs(temp.data - closest))
			value = temp.data
		return find_closest(temp.right , closest , min_diff , value)
root = None
for i in arr:
	root = insert_tree(root , i)

print(find_closest(root , closest))