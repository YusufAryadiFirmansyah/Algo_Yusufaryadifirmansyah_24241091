# operasi komparasi/perbandingan

# perhatikan 
"""
   Hasil dari operasi komparasi
   selalu bertipe data boolean
   (True/False)
"""
# >,<,>=,<=,==,!=, is, dan is not

a = 4
b = 2

# lebih dari >
print("===Lebih dari (>)")
hasil = a > 3 # TRUE
print(hasil)
hasil = b > 3 # FALSE
print(hasil)
hasil = b > 2
print(hasil)

# kurang dari <
print("===Lebih dari (<)")
hasil = a < 3 # FALSE
print(hasil)
hasil = b < 3 # TRUE
print(hasil)
hasil = b < 2 # FALSE
print(hasil)

# lebih dari sama dengan
print("===Lebih dari (>=)")
hasil = a >= 3 # TRUE
print(hasil)
hasil = b >= 3 # FALSE
print(hasil)
hasil = b >= 2 # TRUE
print(hasil)

# kurang dari sama dengan
print("===Lebih dari (<=)")
hasil = a <= 3 # FALSE
print(hasil)
hasil = b <= 3 # TRUE
print(hasil)
hasil = b <= 2 # TRUE
print(hasil)

# sama dengan 
print("===Lebih dari (==)")
hasil = a == 3 # FALSE
print(hasil)
hasil = b == 3 # FALSE
print(hasil)
hasil = b == 2 # TRUE
print(hasil)

# tidak sama dengan
print("===Lebih dari (!=)")
hasil = a != 3 # TRUE
print(hasil)
hasil = b != 3 # TRUE
print(hasil)
hasil = b != 2 # FALSE
print(hasil)