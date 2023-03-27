import  ast
import astor
import copy


def fill_storage_args(tree: ast.AST, contract: str) -> ast.AST:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            try:
                if node.value.func.id == "Storage":
                    old_node = copy.deepcopy(node) # ok to use deep copy?
                    node.value.keywords.append(ast.keyword('contract', ast.Str(contract)))
                    node.value.keywords.append(ast.keyword('storage', ast.Str(node.targets[0].id)))
                    ast.copy_location(node, old_node)
                    ast.fix_missing_locations(node)
            except:
                pass
    return tree

def change_init_function_name(tree: ast.AST):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.decorator_list:
                decorator = node.decorator_list[-1]
                try:
                    if decorator.id == "initialise":
                        old_node = copy.deepcopy(node) # ok to use deep copy?
                        node.name = 'init'
                        ast.copy_location(node, old_node)
                        ast.fix_missing_locations(node)
                except:
                    pass
    return tree        