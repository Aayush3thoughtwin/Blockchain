# 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

digest = hashes.Hash(hashes.SHA256(),backend=default_backend())
# digest.update(b"abc")
digest.update(b"124")
hash = digest.finalize()
print("\n",hash)
# output hash : b'l\xa1=R\xcap\xc8\x83\xe0\xf0\xbb\x10\x1eBZ\x89\xe8bM\xe5\x1d\xb2\xd29%\x93\xafj\x84\x11\x80\x90'

print(f"\n*******This is two different hash*******\n")

# here we are watching that the two different msg generates two different hash
digest = hashes.Hash(hashes.SHA256(),backend=default_backend())
# digest.update(b"abc")
digest.update(b"125")
hash = digest.finalize()
print(hash)
#output hash : b'\xe1O\xd8f#\x99\x8f/D\xec\xd9Uh\xe8#\xba6\x9f\xf9x\x1ao\\\x18\x03\xb2fe\x199)\x98'