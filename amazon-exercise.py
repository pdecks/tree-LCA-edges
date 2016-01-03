class BinaryTreeNode:

    def __init__(self, value, parent):
        self.value = value
        self.left  = None
        self.right = None
        self.parent = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


class BSTNode(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left  = None
        self.right = None
    
    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
                self.right.parent = self
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BSTNode(value)
                self.left.parent = self
            else:
                self.left.insert(value)

def traverse(node):
    """Visit all nodes in the tree starting at node, in depth order."""
    if not node:
        return
    traverse(node.left)
    traverse(node.right)


def find_LCA(root, n1, n2):
    if not root:
        return None
    if n1 <= root.value and root.value <= n2:
        return root
    elif n1 < root.value and n2 < root.value:
        if root.right:
            find_LCA(root.right)
        else:
            return None
    elif root.value < n1 and root.value < n2:
        if root.left:
            find_LCA(root.left, n1, n2)
        else:
            return None



# the first node, n, we encounter with a value between n1 and n2 (n1 < n < n2)
# will be the LCA

# if n > n1 and n > n2, LCA in left subtree
# if n < n1 and n < n2, LCA in right subtree
# else root is LCA

if __name__ == "__main__":


    # # grab input                
    # node_1 = input()
    # node_2 = input()
    # num_nodes = input()
    # node_values = [int(i) for i in raw_input().strip().split()]
    node_values = [50 25 75 10 30 60 80 5 26 32]
    # create tree
    root = BSTNode(node_values[0])
    for i in range(1:len(node_values)):
        root.insert(node_values[i])
    print "Looking for LCA of 5 and 32"
    result = find_LCA(root, 5, 32)
    print "Looking for LCA of 5 and 80"
    result = find_LCA(root, 5, 80)

                