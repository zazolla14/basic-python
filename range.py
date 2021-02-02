#RANGE  digunakan untuk memberi jarak data

#Contoh penulisan tanpa menggunakan range pada list indeks
nomor = [1,2,3,4,5,6,7,8,9,10]
#cara ini tidak efektif jika banyak data yang akan ditulis

#Solusi penulisan angka dengan menggunakn RANGE untuk 1 sampa 10
nomor2 = range(1, 11)   #KENAPA 1, 11 karena range didalam angka antara 1 - 11 yaitu 1-10

for no in nomor2:
    print(f"Hasil menggunakan range {no}")

#cara yang lebih mudah yaitu dengan memasukan RANGE kedalam for loop

for num in range(1, 11):
    print("-----------------------------")
    print(f"Hasil menggunakan range {num}")