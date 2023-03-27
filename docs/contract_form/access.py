@public
def get_welcome_message(): # public function, accessible to others and this contract
    return greet()

def greet(): # private function, only accessible to this contract
    return "Welcome to Marvinnet!"