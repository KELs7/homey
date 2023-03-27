import  ast
import astor
from db.driver.memory_driver import mem_driver
from execution.execution import execute, get_module_from_code_string
from compilation.compile import fill_storage_args, change_init_function_name

DRIVER = mem_driver

def submit_contract(name: str, code: str, client="sys", init_args={}):
    # TODO: lint code before anything else
    tree = ast.parse(code)
    tree_1 = fill_storage_args(tree=tree, contract=name)
    tree_2 = change_init_function_name(tree=tree_1)
    code = astor.to_source(tree_2)
    code_obj = compile(code, "", "exec")
    module = get_module_from_code_string(contract=name, code_obj=code_obj) # return compiled as well?
    func = getattr(module, "init") 
    func(**init_args)
    DRIVER["set_contract"](name=name, code=code, code_obj=code_obj, sender=client)


def submit_tx(tx_info: dict):
    contract = tx_info["contract"]
    sender = tx_info["sender"]
    method = tx_info["method"]
    try:
        kwargs = tx_info["kwargs"]
    except:
        kwargs = {} 
    return execute(contract=contract, method=method, kwargs=kwargs, sender=sender)