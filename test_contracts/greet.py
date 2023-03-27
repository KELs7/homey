@public
def greet(name: str):
    return say_hello(name=name)

def say_hello(name: str):
    return f"Hello {name}"