class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "Node(" + str(self.value) + ")"


def dfs1(tree):
    if tree is not None:
        print(tree)
        dfs1(tree.left)
        dfs1(tree.right)


def dfs2(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:  # Check if node is not None before printing
            print(node)
            stack.append(node.left)
            stack.append(node.right)

tree = Node('A', Node('B', Node('E')), Node('C', Node('F'), Node('G')))

print("DFS1:")
dfs1(tree)

print("\nDFS2:")
dfs2(tree, [])
