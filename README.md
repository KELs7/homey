git clone this https://github.com/KELs7/homey.git

`sudo git clone repo url`

install astor if you don't have the package already installed

`pip3 install astor`

copy the code below and paste into testing.py and run (python3 testing.py)

```
from client import submit_contract, submit_tx

with open("test_contracts/marv_token.py") as f:
    code = f.read()

# submit your contract code
submit_contract(name="con_token", code=code, client="marvin") 
# submit_contract(name="con_token", code=code)    client default value is "sys"        

# create a dictionary with transaction info
tx_info = {
    "contract": "con_token", 
    "method": "transfer",
    "kwargs":{
        "amount": 1000,
        "to": "benji"
    }
}
# submit your transaction
submit_tx(tx_info=tx_info)

```
kindly open the docs folder to have an idea how contracts will look like.
