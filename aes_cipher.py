from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(data: bytes, key: bytes) -> tuple:
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv, ciphertext

def aes_decrypt(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data

if __name__ == "__main__":
    kunci = b"16ByteSecretKey!"
    mesej_asal = b"Hello, ini ujian block cipher AES!"

    print("1. Teks Asal       :", mesej_asal.decode())

    iv, teks_sulit = aes_encrypt(mesej_asal, kunci)
    print("2. Teks Disulitkan :", teks_sulit)

    teks_dinyahsulit = aes_decrypt(iv, teks_sulit, kunci)
    print("3. Teks Dinyahsulit:", teks_dinyahsulit.decode())