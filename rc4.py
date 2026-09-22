def ksa(key: bytes) -> list:
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S: list, n_bytes: int) -> bytes:
    S = S.copy()
    i = 0
    j = 0
    keystream = bytearray()
    for _ in range(n_bytes):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return bytes(keystream)

def rc4_process(data: bytes, key: bytes) -> bytes:
    S = ksa(key)
    keystream = prga(S, len(data))
    return bytes([b ^ k for b, k in zip(data, keystream)])

if __name__ == "__main__":
    kunci = b"KunciRahsiaUPTM"
    mesej_asal = b"Hello, ini ujian pertama stream cipher RC4!"

    print("1. Teks Asal       :", mesej_asal.decode())

    teks_sulit = rc4_process(mesej_asal, kunci)
    print("2. Teks Disulitkan :", teks_sulit)

    teks_dinyahsulit = rc4_process(teks_sulit, kunci)
    print("3. Teks Dinyahsulit:", teks_dinyahsulit.decode())