# ARGUMENT LIS --> membuat suatu Argumen pada parameter menjadi list agar, parameter tersebut dapat menimpan banyak data sekaligus

# CARA MELAKUKAN PENJUMLAHKAN SEDERHANA TANPA MENGGUNAKAN ARGUMENT LIST
# def jumlahkan (satu, dua, tiga):
#    total = satu + dua + tiga
#    print(f"Hasil dari {satu} + {dua} + {tiga}= {total}")

#jumlahkan(10, 10, 10)

# cara dengan menggunakan ARGUMENT LIST
# ARGUMENT LIST ditandai dengan tanda * jika ingin menambah default argumwen harus di taruh di depan argument list
def jumlahkan(x, *list_jumlahkan):
    total = 0
    for angka in list_jumlahkan:
        total = total + angka
    print(f"Hasil dari {list_jumlahkan} = {total}")


# dengan menggunakn ARGUMENT LIST kita bebas memasukan berapa banyak input nya
jumlahkan(0, 10, 10, 10, 10, 10)  # x = 0
