def are_equal(node1, node2):
    # print("Checking Eq ", node1, node2)
    if node1 is None:
        return node1 == node2
    elif node2 is None:
        return False

    if node1.id != node2.id:
        return False
    
    return are_equal(node1.left, node2.left) and are_equal(node1.right, node2.right)

def search(parent, child):
    if are_equal(parent, child):
        return True
    if parent == None:
        return False
    return search(parent.left, child) or search(parent.right, child)

class Node:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.id)

def main():
    p = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    n = Node(3, Node(6), Node(7))
    print(search(n, n))

if __name__ == '__main__':
    main()
    