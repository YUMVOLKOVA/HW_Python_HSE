import ast


# import networkx

def show_ast(path):
    with open(path, "r") as f:
        ast_tree = ast.parse(f.read())
    print(ast.dump(ast_tree))


if __name__ == "__main__":
    show_ast('easy.py')
