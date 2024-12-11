# Percabangan
# menggunakan statement IF

# struktur IF statement sederhana
"""
   1. if-nya
   2. Ada kondisi (bernilai TRUE/FALSE
   3. Ada aksi -> proses lanjutan 
"""

nama = input(" Masukan Nama Anda =  ")

# IF statement dalam bentuk inline (satu baris)
#if nama == "fadli": print(f"Selamat Datang{nama}")
#print("Terima Kasih")

# IF statement dalam bentuk indentasi
if nama == 'fadli':
     print(f'Selamat Datang {nama}')
print ("Terima Kasih")

# IF-ELSE statement
if nama == 'fadli':
     # aksi 1
     print(f'Selamat Datang {nama}')
else :
     #aksi 2
     print(f'Kamu{nama}, bukan fadli')
print('Terima Kasih')
