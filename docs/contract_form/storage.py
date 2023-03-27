owner = Storage() 
balance = Storage(default_value=0) # can set an initial value.
                                   # if not set, the default value is None

@initialise  # decorator ensures this function is called once on contract submission
def init():  
    balances["wallet_1234"] = 1_000_000 # can store multiple keys. Max is 8 
                                       # eg: balance["wallet_1234", "wallet_2345"] 
    owner.set("marvin")            

@public
def show_owner():
    return owner.get("marvin")

@public
def show_balance():
    return balances["wallet_1234"]  # returns 1000000

@public
def show_zero_balance():
    return balances["wallet_0000"]  # returns 0 because it was not initialised
                                   # the default value will be returned