class Node:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node
        self.keys = []  # List of keys in the node
        self.children = []  # List of child nodes
        self.is_root = False
        self.count = 0

    def max_keys(self):
        return 2 * self.t - 1
    
    def min_keys(self):
        return self.t - 1

    def max_children(self):
        return 2 * self.t
    
    def min_children(self):
        return self.t
    

def b_tree_search(x, k):
    i = 0
    while i <= x.count and k > x.keys[i]:
        i += 1
    if i <= x.count and k == x.keys[i]:
        return (x, i)
    if x.leaf:
        return None
    return b_tree_search(x.children[i], k)
    
