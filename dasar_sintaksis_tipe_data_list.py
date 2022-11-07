daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
print(daftar_anak_kos)

for kos in daftar_anak_kos:
    print(kos)

print('\nTampilkan daftar anak kos cabul')
print(daftar_anak_kos[0])
print(daftar_anak_kos[1])

print('\nTampilkan para PK kampus')
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
print('\nNjeng tambahin satu buku lagi')
daftar_anak_kos.append('ZXZX')
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])
