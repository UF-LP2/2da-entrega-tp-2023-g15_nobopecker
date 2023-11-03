from binarytree import Node

class Nodo(Node):
    def __init__(self,value,name, left=None, right=None):
        super().__init__(value, left, right)
        self.name=name
