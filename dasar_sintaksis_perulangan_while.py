"""
Program perulangan membaca buku dengan while
"""
jumlah_buku = 69
print('Ibu berkata, "Baca semua buku mu anjeng"')

jumlah_buku_yang_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f"Buku ke {jumlah_buku_yang_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")
