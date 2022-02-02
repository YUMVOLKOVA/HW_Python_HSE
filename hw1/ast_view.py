import ast
import networkx as nx
import matplotlib.pyplot as plt

class AST(ast.NodeVisitor):
    def __init__(self):
        
