class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    # DFS

    def preOrderTraversal(self,node):
        if node is None:
            return
        else:
            print(node.data,end=", ")
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def inOrderTraversal(self,node):
        if node is None:
            return
        else:
            self.inOrderTraversal(node.left)
            print(node.data,end=", ")
            self.inOrderTraversal(node.right)
    
    def postOrderTraversal(self,node):
        if node is None:
            return
        else:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.data,end=", ")




    # BFS 
    
    def findHeight(self,node):
        if node is None:
            return 0
        else:

            # Compute the height of each subtree
            lheight = self.findHeight(node.left)
            rheight = self.findHeight(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

    def levelTraversal(self,node):
        height = self.findHeight(node)
        for i in range(1,height+1):
            self.printCurrentLevel(node,i)

    def printCurrentLevel(self,node,level):
        if node is None:
            return
        elif level == 1:
            print(node.data,end=", ")
        else:
            self.printCurrentLevel(node.left,level-1)
            self.printCurrentLevel(node.right,level-1)
        



t = Tree()
t.root = Node(1)
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.right = Node(6)


print("\nPreorder:")
t.preOrderTraversal(t.root)
print("\nInorder:")
t.inOrderTraversal(t.root)
print("\nPostOrder:")
t.postOrderTraversal(t.root)
print("\nLevelTraversal:")
t.levelTraversal(t.root)