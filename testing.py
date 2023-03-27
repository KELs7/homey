# Paste/write your test code here

from client import submit_contract, submit_tx

with open("test_contracts/marv_token.py") as f:
    code = f.read()

# submit your contract code
submit_contract(name="con_token", code=code, client="marvin") 
# submit_contract(name="con_token", code=code)    client default value is "sys"        

# create a dictionary with transaction info
tx_info = {
    "contract": "con_token", 
    "sender": "marvin",
    "method": "transfer",
    "kwargs":{
        "amount": 1000,
        "to": "benji"
    }
}
# submit your transaction
submit_tx(tx_info=tx_info)