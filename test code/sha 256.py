import hashlib

m = hashlib.sha256()
m.update(b'testsha256')

print(m.digest())