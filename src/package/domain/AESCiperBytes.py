from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad


from src.package.utils.constants import SALT


# # Later on ... (assume we no longer have the key)
# file_in = open(key_location, "rb") # Read bytes
# key_from_file = file_in.read() # This key should be the same
# file_in.close()

class AESCipher(object):
    KEY_SIZE_16 = 16
    KEY_SIZE_24 = 24
    KEY_SIZE_32 = 32

    # path should be a directory location
    def __init__(self, password=None, path='aes_key.key', key_size=KEY_SIZE_16, mode=AES.MODE_CBC):
        self.mode = mode
        if password == None:
            self.key = Random.get_random_bytes(key_size)
            # Save the key to a file
            file_out = open(path+'/aes_key.key', "wb")  # wb = write bytes
            file_out.write(self.key)
            file_out.close()
        else:
            self.key = PBKDF2(password, SALT, dkLen=key_size)

    def set_mode(self, mode):
        self.mode = mode

    def encrypt(self, data):
        # if iv is not given , it will generate random one , auto
        if self.mode == AES.MODE_CBC:
            cipher = AES.new(self.key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))
            iv = b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            # not complete . complete this if needed ( according to official docs)
            pass
        elif self.mode == AES.MODE_CFB:
            pass
        elif self.mode == AES.MODE_EAX:
            pass

        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(
            encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - \
            len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
