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

def find_the_sum_of_branches(root):
	branch_sum = root.get_data()
	solutionArr = []
	stack = []
	stack.append(root)
	stack, branch_sum, solutionArr = sum_branch(stack, branch_sum, solutionArr)
	return solutionArr	

def sum_branch(stack, branch_sum, solutionArr):
	if len(stack) == 0:
			return [stack,branch_sum,solutionArr]

	if stack[-1].left == None and stack[-1].right == None:
		solutionArr.append(branch_sum)
		branch_sum -= stack[-1].get_data()
		stack.pop()
		return [stack,branch_sum,solutionArr]

	if stack[-1].left != None:
		branch_sum += (stack[-1].left).get_data()
		stack.append(stack[-1].left)
		stack, branch_sum, solutionArr = sum_branch(stack, branch_sum, solutionArr)
		
	if stack[-1].right != None:
		branch_sum += (stack[-1].right).get_data()
		stack.append(stack[-1].right)
		stack, branch_sum, solutionArr = sum_branch(stack, branch_sum, solutionArr)
	
	branch_sum -= stack[-1].get_data()
	stack.pop()
	return [stack , branch_sum, solutionArr]

root = None
for i in arr:
	root = insert_tree(root , i)

print(find_the_sum_of_branches(root))