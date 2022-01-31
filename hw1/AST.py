import ast
import astunparse


def show_ast(path):
    with open(path, "r") as f:
        ast_tree = ast.parse(f.read())
    printed_ast = astunparse.dump(ast_tree)
    with open('ast_tree.txt', 'w') as f:
        f.write(printed_ast)


if __name__ == "__main__":
    show_ast('easy.py')
