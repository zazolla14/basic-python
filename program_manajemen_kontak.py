#Program manajemen kontak

#MENU
#1. Daftar Kontak
#2. Tambah Kontak
#3. Hapus Kontak
#4. Cari Kontak

#Daftar Kontak
# -Nama
# -Email
# -No Telepon

import program_man_kon_function

daftar_kontak=[]

daftar_kontak.append(
    {
        "nama":"Azola Zubizarreta",
        "email":"azola.zubizarreta",
        "no_telp":"087867870372"
    }
)
daftar_kontak.append(
    {
        "nama":"Dety Mei Dina Saputri",
        "email":"dety.dina@gmail.com",
        "no_telp":"089648461979"
    }
)


while True:
    print("=====================")
    print("Menu Manajemen Kontak")
    print("=====================")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari kontak")
    print("0. Keluar Program")
    print("---------------------")

    menu = input("Pilih menu : ") 

    if menu == "0":
        break

    elif menu == "1":
        print("=============")
        print("Daftar Kontak")
        print(len(daftar_kontak))
        print("=============")
        program_man_kon_function.display_kontak(daftar_kontak)

    elif menu == "2":
        print("================")
        print("Tambahkan Kontak")
        print("================")
        kontak = program_man_kon_function.new_kontak()
        daftar_kontak.append(kontak)
    
    elif menu == "3":
        print("============")
        print("Hapus Kontak")
        print("============")
        program_man_kon_function.hapus_kontak(daftar_kontak)
    else:
        print("==============")
        print("4. Cari kontak")
        print("==============")
        program_man_kon_function.cari_kontak(daftar_kontak)

print("Keluar Dari Program")
print("Terimnaksih :)")




#    elif menu == "4":
#        print("Cari Kontak")

#    elif menu == "5":
#        print("Keluar Dari Program")
#        print("Terimnaksih :)")

#    else:
#        print("Pilihan tidak tersedia!")