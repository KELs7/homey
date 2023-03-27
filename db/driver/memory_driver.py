from typing import Any
import marshal

storage = {}

def make_key(contract: str, storage: str) -> str:
    return f"{contract}.{storage}"

def set(key: str, value: Any):
    storage[key] = value

def get(key: str) -> Any:
    try:
        return storage[key]
    except:
        return {}

def set_contract(name: str, code: str, code_obj: Any, sender: str):
    code_bytes = marshal.dumps(code_obj)
    data = {"code_string": code, "compiled": code_bytes, "creator": sender}
    set(key=name, value=data)

def get_contract_code(contract: str):
    return get(key=contract)["code_string"]

def get_contract_compiled(contract: str):
    return get(key=contract)["compiled"]


mem_driver = {
    "make_key": make_key,
    "set": set,
    "get": get,
    "set_contract": set_contract,
    "get_contract_code": get_contract_code,
    "get_contract_compiled": get_contract_compiled
}