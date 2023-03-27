
import marshal
from typing import Any
from stdlib.env import env
from db.driver.memory_driver import mem_driver
from importlib.util import module_from_spec, spec_from_loader

DRIVER = mem_driver

def check_private_method(func):
    assert func.__name__ == "public", "This function is private and cannot be called from outside!"


def check_constructor(func):
    assert func.__name__ != "constructor", "This function is private and cannot be called from outside!"

def import_module(contract: str):
    code_bytes = DRIVER["get_contract_compiled"](contract=contract)
    code_obj = marshal.loads(code_bytes)
    spec = spec_from_loader(contract, loader=None)
    module = module_from_spec(spec)
    module.__dict__.update(env)
    exec(code_obj, module.__dict__)
    return module
    # sys.modules[name] = module
    # globals()[name] = module

def get_module_from_code_string(contract: str, code_obj: Any):
    # code_obj = compile(code, "", "exec")
    spec = spec_from_loader(contract, loader=None)
    module = module_from_spec(spec)
    module.__dict__.update(env)
    exec(code_obj, module.__dict__)
    return module
    

def execute(contract: str, method: str, kwargs: dict, sender: str) -> Any:
    module = import_module(contract=contract)
    func = getattr(module, method)
    check_constructor(func)
    check_private_method(func)
    return func(**kwargs)