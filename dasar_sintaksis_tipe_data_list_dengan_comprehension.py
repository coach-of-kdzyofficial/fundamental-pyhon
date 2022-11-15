print('\nPerintah Del')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
del daftar_anak_kos[0]
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

print('\nPerintah Del dengan list comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
del daftar_anak_kos[:] #START:END
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

print('\nPerintah Del dengan list comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
del daftar_anak_kos[0:2] #START:END
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

print('\nPerintah Del dengan list comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
del daftar_anak_kos[0:-2] #START:END
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

print('\nPerintah Del dengan list comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
del daftar_anak_kos[0::2] #START:END:STEP
for i in range (0,len(daftar_anak_kos)):
    print(daftar_anak_kos[i])

print('\nMembuat list baru')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep']
daftar_anak_kos_baru = daftar_anak_kos
for i in range (0,len(daftar_anak_kos_baru)):
    print(daftar_anak_kos_baru[i])

print('\nMembuat list baru')
del daftar_anak_kos_baru [:]
for i in range (0,len(daftar_anak_kos_baru)):
    print(daftar_anak_kos_baru[i])

print('\nMembuat list baru dengan comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep','Rizkinnyott']
daftar_anak_kos_baru = daftar_anak_kos [1::2]
for i in range (0,len(daftar_anak_kos_baru)):
    print(daftar_anak_kos_baru[i])

print('\nMembuat list baru dengan comprehension')
daftar_anak_kos = ['Mekkbok','Zulkenyott','Niepep','Rizkinnyott']
daftar_anak_kos_baru = daftar_anak_kos [0:-1]
for i in range (0,len(daftar_anak_kos_baru)):
    print(daftar_anak_kos_baru[i])
