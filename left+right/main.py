import numpy as np 
from sympy import isprime
from graphviz import Digraph

maxlen = 0
maxint = 0


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
    return isprime(n) #holy fuck this is like hundreds of times than simple check_prime faster for large numbers

def add_prime_children(node):
    global maxlen,maxint
    for sd in range(1,10): 
        new_val1 = 10*node.value() + sd
        if check_prime(new_val1):
            new_child = Tree(str(new_val1))
            node.add_child(new_child)
            if len(str(new_child.value()))>maxlen:
                maxlen = len(str(new_child.value()))
                maxint = new_child.value()
                #print(maxlen)
            add_prime_children(new_child)
        new_val2 = sd*(10**len(str(node.value())))+node.value()
        if check_prime(new_val2):
            new_child = Tree(str(new_val2))
            node.add_child(new_child)
            if len(str(new_child.value()))>maxlen:
                maxlen = len(str(new_child.value()))
                maxint = new_child.value()
                #print(maxlen)
            add_prime_children(new_child)


#--------------------------

trees = [Tree(str(i)) for i in [2,3,5,7]]
for tree in trees:
    maxlen = 0
    maxint = 0
    add_prime_children(tree)
    print(f"done with tree {tree.value()}")
    print(maxlen)
    print(maxint)

# WAYYYY too fucking big to visualize
# Visualize each tree
#for i, tree in enumerate(trees):
#    dot = visualize_prime_tree(tree)
#    dot.render(f'prime_tree_{tree.name}', format='png', cleanup=True)
#    print(f"Tree for {tree.name} has been saved as 'prime_tree_{tree.name}.png'")