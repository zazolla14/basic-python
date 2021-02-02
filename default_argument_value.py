#Default Argumen value atau DAULT VALUE pada python --> Argumen yang set di PARAMTER secara defaul pada METHOD
#jika pada METHOD biasa nya kita sudah menset isi pada argumen, maka dengan menggunakan DEFAULT METHOD kita hanya perlu men set agar VALUE tersebut sudah disi


#def say_hello(first_name, last_name):                #pada METHOD ini dengan variabel say_hello sudah terdapat parameter first_name dan last_name
#    print(f"Hello {first_name} {last_name}, Selamat Datang!")

#say_hello("Azola", "Zubzarreta")                    #maka untuk dapat memunculkan isi parameter tersebut kita perlu mengisikan ini paramter sebut yaitu Azola dan Zubiozarreta agar sesuai dengan parameter pada method. Jika ttdak disi maka program tidak akan berjalan

def say_hello(first_name="Zolla", last_name="Zubi"):       #Contoh default value dengan parameter Zolla dan Zubi
    print(f"Selamat datang {first_name} - {last_name} ")

say_hello()                                                 #ketika memanggil method walu pun tidak diisi parameter nya maka program akan tetap berjalan, karena sudah menggunakn default value

#jika ingin Zubizarreta menjadi last_name dan Azola menjadi first_name yaitu dengan cara sbg berukut
say_hello(last_name="Zubizarreta", first_name="Azola")                          