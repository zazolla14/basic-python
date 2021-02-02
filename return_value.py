#RETURN VALUE digunakan untuk mengembalikan hasil dari suatu method

#disini kita akan mengambil value dari list_angka dan total
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka

    #print(f"Hasil penjumlahan {list_angka} = {total}")

    return list_angka, total                            #pengambilan parameter tidak boleh terbalik, karena akan mempengaruhi hasil pengambilan RETURN

list_angka, total = jumlahkan(10, 10, 10, 10, 10)       #value yang diambil atau yang di RETURN harus di definisikan atau ditulikan sebelum penulisan METHOD

#Hasil pengambilan dari method jumlahkan
print(f"Hasil penjumlahan {list_angka} = {total}")  