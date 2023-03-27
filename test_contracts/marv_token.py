balances = Storage(default_value=0)

@initialise
def let_see():
    balances["marvin"] = 5000

@public
def transfer(amount: str, to: float):
    assert amount > 0, "Amount cannot be negative!"
    assert balances["marvin"] > amount, "Do not have enough balance!"
    balances["marvin"] -= amount
    balances[to] += amount

    
    
    print(f'marvin: {balances["marvin"]}')
    print(f'{to}: {balances[to]}')