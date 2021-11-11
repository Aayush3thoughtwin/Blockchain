# libraries which is used for performing the task.

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature 

# Function for generating the keys
def generate_keys():
    private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
) 
    public  = private.public_key()  # Here the public key
    return private, public

# Function for signing the message
def sign (message, private):
    # message = b"A message I want to sign"
    sig = private.sign(message,padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Here is the signature which sign the msg
    return sig

# It is the verification function
def verify(message, sig, public):
    try:
        res = public.verify(
        sig,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print("Error Executing public.key verify")
        return False

if __name__=="__main__" :
    pr,pu = generate_keys()
    print(pr)
    print(pu)
    message = b"thus3is5be"  #THis is the msg for that we will generate the keys and signature. 
    sig = sign(message,pr)
    print(sig)
    correct = verify(message,sig,pu)
    print(correct)

    if correct:
        print("Success! good sig")
    else:
        print("Bad sig")
