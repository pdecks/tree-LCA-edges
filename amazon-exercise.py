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
    # import pdb; pdb.set_trace()
    if not root:
        return None
    if n1 <= root.value and root.value <= n2:
        return root
    elif n1 < root.value and n2 < root.value:
        if root.left:
            return find_LCA(root.left, n1, n2)
        else:
            return None
    elif root.value < n1 and root.value < n2:
        if root.right:
            return find_LCA(root.right, n1, n2)
        else:
            return None

def count_edges(root, LCA, n1, n2):
    if not root:
        return None
    # traverse tree to find LCA
    level_LCA = traverse_tree(root, LCA.value)
    print "LCA:", LCA.value
    print "Level LCA", level_LCA
    # traverse from root to find node1
    level_n1 = traverse_tree(root, n1)
    print "Level n1", level_n1
    # traverse from root to find node2
    level_n2 = traverse_tree(root, n2)
    print "Level n2", level_n2
    # number of edges = level_n1 + level_n2 - 2(level_LCA)
    if LCA != root:
        num_edges = level_n1 + level_n2 - 2 * level_LCA
    else:
        num_edges = level_n1 + level_n2
    return num_edges


def traverse_tree(root, node):
    if not root:
        return None
    current = root
    level = 0
    while current:
        if current.value == node:
            return level
        elif current.value < node and current.right:
            level += 1
            current = current.right
        elif current.value > node and current.left:
            level += 1
            current = current.left
        else:
            return None
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
    node_values = [50, 25, 75, 10, 30, 60, 80, 5, 26, 32]
    # create tree
    root = BSTNode(node_values[0])
    for i in range(1,len(node_values)):
        root.insert(node_values[i])
    print "Looking for LCA of 5 and 32"
    LCA = find_LCA(root, 5, 32)
    print "Result:", LCA
    print "Result.value:", LCA.value
    print "Looking for LCA of 5 and 80"
    result = find_LCA(root, 5, 80)
    print "Result:", result
    print "Result.value:", result.value

    level_n1 = traverse_tree(root, 5)
    level_LCA = traverse_tree(root, LCA.value)
    num_edges = count_edges(root, LCA, 5, 32)
    print "num_edges between 5 and 32", num_edges
    num_edges = count_edges(root, LCA, 5, 60)
    print "num_edges between 5 and 60", num_edges

                