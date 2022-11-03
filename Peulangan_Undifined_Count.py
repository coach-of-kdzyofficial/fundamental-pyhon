"""
Perulangan Undifinite dengan Pemberhetian
"""
book_count = 10
print('Ibu berkata "Baca bukumu anjeng"')

understood_count = 0
read_count = 0

print(f"Jumlah buku yang sudah dibaca dan dipahami sebanyak {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")

    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

print(f"Saya sudah baca dan memahami {understood_count} buku njenngg")
if understood_count == book_count:
    print('Budi berkata, "Njeng semua buku sudah saya baca dan saya pahami"')

else:
    print(f'Budi berkata, "Njeng tidak semua buku bisa saya baca dan saya pahami,'
          f' gw cuma bisa membaca dan memahami {understood_count} buku"')



