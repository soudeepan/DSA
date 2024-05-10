class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None

# insert in a BST
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# search in a BST
def search(root,key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right,key)
    else:
        return search(root.left,key)
    
# Inorder traversal
def inOrderTraversal(node):
    if node is None:
        return
    else:
        inOrderTraversal(node.left)
        print(node.value,end=", ")
        inOrderTraversal(node.right)
    

# delete in a BST
def delete(root,key):
    if root is None:
        return root
    
    if root.value > key:
        root.left = delete(root.left,key)
    elif root.value < key:
        root.right = delete(root.right,key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        temp = root.right
        while temp.left is not None:
            temp = temp.left       

        root.value = temp.value
        root.right = delete(root.right, root.value)
    return root


root = None
root = insert(root,50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

inOrderTraversal(root)
print()

delete(root,40)

inOrderTraversal(root)
print()

key = 60
if search(root,key):
    print("Found")
else:
    print("Not Found")