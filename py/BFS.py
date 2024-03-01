class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "Node(" + str(self.value) + ")"


def bfs(node,que):
    que.append(node)
    while len(que)>0:
        node=que.pop(0)
        if node is not None:
            print(node)
            que.append(node.left)
            que.append(node.right)

tree = Node('A', Node('B', Node('E')), Node('C', Node('F'), Node('G')))

print("BFS:")
bfs(tree,[])
