from crypto.wallet import *

# create key pair
sk_vk = create_pair() # {"sk": xxxxx, "vk": yyyyy}
# Let's sign a message
message = "Awesome tutorial!"
# To sign a message, you must first create a signing object
sk_obj = create_signing_object(sk=sk_vk["sk"])
# sign a message
signature = sign(sk=sk_obj, message=message)
# Validate_signer
msg = validate_signer(vk=sk_vk["vk"], signature=signature, message=message)

print(msg) # Voila!
