import os
import time
import matplotlib.pyplot as plt
from rc4 import rc4_process
from aes_cipher import aes_encrypt, aes_decrypt

sizes = {
    "1 KB": 1024,
    "100 KB": 100 * 1024,
    "1 MB": 1024 * 1024
}

key_rc4 = b"SecretKey16Bytes"
key_aes = b"SecretKey16Bytes"

results = {
    "RC4_Enc": [], "RC4_Dec": [],
    "AES_Enc": [], "AES_Dec": []
}

print(f"{'Size':<10} | {'RC4 Enc (s)':<12} | {'RC4 Dec (s)':<12} | {'AES Enc (s)':<12} | {'AES Dec (s)':<12}")
print("-" * 65)

for label, size in sizes.items():
    test_data = os.urandom(size)

    # Ujian RC4
    t0 = time.perf_counter()
    rc4_cipher = rc4_process(test_data, key_rc4)
    t_rc4_enc = time.perf_counter() - t0

    t0 = time.perf_counter()
    rc4_process(rc4_cipher, key_rc4)
    t_rc4_dec = time.perf_counter() - t0

    # Ujian AES
    t0 = time.perf_counter()
    iv, aes_cipher = aes_encrypt(test_data, key_aes)
    t_aes_enc = time.perf_counter() - t0

    t0 = time.perf_counter()
    aes_decrypt(iv, aes_cipher, key_aes)
    t_aes_dec = time.perf_counter() - t0

    results["RC4_Enc"].append(t_rc4_enc)
    results["RC4_Dec"].append(t_rc4_dec)
    results["AES_Enc"].append(t_aes_enc)
    results["AES_Dec"].append(t_aes_dec)

    print(f"{label:<10} | {t_rc4_enc:<12.6f} | {t_rc4_dec:<12.6f} | {t_aes_enc:<12.6f} | {t_aes_dec:<12.6f}")

# Hasilkan Graf Perbandingan
labels = list(sizes.keys())
x = range(len(labels))
width = 0.2

plt.figure(figsize=(10, 6))
plt.bar([p - 1.5*width for p in x], results["RC4_Enc"], width=width, label="RC4 Encryption")
plt.bar([p - 0.5*width for p in x], results["RC4_Dec"], width=width, label="RC4 Decryption")
plt.bar([p + 0.5*width for p in x], results["AES_Enc"], width=width, label="AES Encryption")
plt.bar([p + 1.5*width for p in x], results["AES_Dec"], width=width, label="AES Decryption")

plt.xlabel("File Size")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison: RC4 vs AES")
plt.xticks(x, labels)
plt.legend()
plt.tight_layout()
plt.savefig("benchmark_results.png")
print("\nGrafik berjaya disimpan sebagai 'benchmark_results.png'")