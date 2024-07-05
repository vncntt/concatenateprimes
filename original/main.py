import numpy as np 
from graphviz import Digraph

class Tree(object):
    def __init__(self, name=1, children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        if not self.children:
            return self.name
        else:
            return f"{self.name}({', '.join(repr(child) for child in self.children)})"
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def value(self):
        return int(self.name)


def check_prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(np.sqrt(n))+1):
            if n%i==0:
                return False
        return True

def add_prime_children(node):
    for sd in single_digits:
        new_val = 10*node.value() + sd
        if check_prime(new_val):
            new_child = Tree(str(new_val))
            node.add_child(new_child)
            add_prime_children(new_child)

def add_to_graph(graph, node, parent=None):
    graph.node(node.name, node.name)
    if parent:
        graph.edge(parent.name, node.name)
    for child in node.children:
        add_to_graph(graph, child, node)

def visualize_prime_tree(root):
    dot = Digraph(comment='Prime Number Tree')
    dot.attr(rankdir='TB', size='8,8')
    add_to_graph(dot, root)
    return dot
#--------------------------

single_digits = [1,3,7,9]

trees = [Tree(str(i)) for i in [2,3,5,7]]

for tree in trees:
    add_prime_children(tree)

# Visualize each tree
for i, tree in enumerate(trees):
    dot = visualize_prime_tree(tree)
    dot.render(f'prime_tree_{tree.name}', format='png', cleanup=True)
    print(f"Tree for {tree.name} has been saved as 'prime_tree_{tree.name}.png'")