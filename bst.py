class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,node,data):
        if node is None:
            return Node(data)
            
        if data< node.data:
            node.left=self.insert(node.left,data)
        elif data> node.data:
            node.right=self.insert(node.right,data)
        return node
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
tree=bst()
tree.root=tree.insert(tree.root,5)
tree.root=tree.insert(tree.root,3)
tree.root=tree.insert(tree.root,1)
tree.root=tree.insert(tree.root,2)
tree.inorder(tree.root)

    #100,101,112,222,226,257