#METHOD/FUNCTION tempat menyimpan kode blpk, yang dapat dipanggil

#SINTAKS
    #def nama_variabel():
    #    kode_blok_nya

    #memanggil method
        #nama_variabel()

#Tanpa menggunakn METHOD
#nama = []

#nama.append ("Azola")
#print("------------")
#for i in nama:
#    print(i)

#nama.append("Zolla")
#print("------------")
#for i in nama:
#    print(i)

#nama.append("Dety")
#print("------------")
#for i in nama:
#    print(i)

#dengan menggunakan METHOD, dengan menggunakan def = define

nama=[]

def print_nama():
    print("-------------")
    for i in nama:
        print(i)

nama.append("Azola")
print_nama()

nama.append("Zolla")
print_nama()

nama.append("Dety")
print_nama()