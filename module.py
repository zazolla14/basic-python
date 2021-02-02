 #digunakan unutk memisah2 file pada python

import module_function                  #ini cara mengimpor semua method dalam satu file python
#from module_function import say_hello   #ini cara mengimport beberapa method saja
#from module_function import total

a = module_function.say_hello("Azola")
print(a)

#a = say_hello("Azola")  #jika hanya meng import beberapa mothod pada suatu file maka tidak perlu memanggil nama file
#print(a)

b = module_function.total(5,5,5,5,5)
print(b)