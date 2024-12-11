# percabangan bersarang - Neisted IF

# kalkulator sederhana
print(20*"=")
print ("kalkulator sederhana")
print(20*"=")

angka_1 = float (input("Masukkan angka ke-1 ="))
operator = input("Operator (+,-) = ")
angka_2 = float(input("Masukkan angka ke-2 ="))

# percabangan
if operator == '+':
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '-' :
    hasil =  angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
else : 
    print("Tolong masukkan angka dan operator yang benar")