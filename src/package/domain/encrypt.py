from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

##########################GENERATE CERTIFICATE PAIR########################

# new_key = RSA.generate(2048)

# private_key = new_key.exportKey("PEM")
# public_key = new_key.publickey().exportKey("PEM")

# fd = open("private_key.pem", "wb")
# fd.write(private_key)
# fd.close()

# fd = open("public_key.pem", "wb")
# fd.write(public_key)
# fd.close()

################ENCRYPT/DECRYPT DATA WITH CERTIFICATE#######################

# message = b'CODE EVERYDAY TO GET BETTER'

# key = RSA.import_key(open('public_key.pem').read())
# cipher = PKCS1_OAEP.new(key)
# ciphertext = cipher.encrypt(message)
