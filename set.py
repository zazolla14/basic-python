#hampir sama dengan LIST dan TUPLE, digunakan unutk menyimpan data
#perbedaan dengan LIST dan TUPLE --> tidak dapat menambahkan data yang sama/duplikat (harus uniq)

#SINTAKS
#set     --> []
#tuple   --> ()
#set     --> {}

nama = {"zolla","azola","dety","dety","mei","mei"}      #data "dety", dan "mei" walau ada dua akan terbaca hanya satu

#tidak dapat pula mengubah data indeks
nama.add("Dina")    #hanya dapat menambah dan menhapus data
print(nama)                             #hasil print dari SET akan mengacak isi data
nama.remove("Dina") #hanya dapat menambah dan menhapus data
print(nama)                             #hasil print dari SET akan mengacak isi data
#print(nama[0])                         #sehingga tidak dapat mengakses INDEKS nya  

#untuk menakses data bisa dengan menggunakn FOR LOOP
for i in nama:
    print(i)