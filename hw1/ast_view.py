import ast
import networkx as nx
import astunparse


class AST(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.graph = nx.DiGraph()

    def generic_visit(self, node):
        name_node = str(node)
        name_node_splitted = name_node.split('.')[-1].split(' ')[0]
        if len(self.stack) > 0:
            parent = self.stack[-1]
            self.graph.add_edge(parent, name_node)

        self.stack.append(name_node)
        self.graph.add_node(name_node, label=name_node_splitted)
        super(self.__class__, self).generic_visit(node)
        self.stack.pop()


def show_ast(function_path, save_path):
    with open(function_path, "r") as f:
        ast_tree = ast.parse(f.read())
    printed_ast = astunparse.dump(ast_tree)
    with open('artifacts/ast_tree.txt', 'w') as f:
        f.write(printed_ast)
    visual = AST()
    visual.visit(ast_tree)
    nx.drawing.nx_pydot.to_pydot(visual.graph).write_png(save_path)


if __name__ == "__main__":
    show_ast('fibonacci.py', 'artifacts/ast.png')
