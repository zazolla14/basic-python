menu_pilihan=input("Pilih menu a,b,c atau d : ")

if menu_pilihan == "a":                 #elif hanya akan mengeksekusi satu blok program sampai else
    print("Anda memilih menu a")
elif menu_pilihan == "b":
    print("Anda memilih menu b")
elif menu_pilihan == "c":
    print("Anda memilih menu c")
elif menu_pilihan == "d":
    print("Anda memilih menu d")
else:
    print("Pilihan tidak tersedia!")

if menu_pilihan == "x":                 #blok berbeda dari blok pertama karena sudah mulai if baru
    print("Anda keluar dari program")   