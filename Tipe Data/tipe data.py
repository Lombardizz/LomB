#tipe data: Angka satuan yang 
# tidak ada koma int(integer)


data_integer = 1 
print("data : ", data_integer)
print("-tipe : ", type(data_integer))

#tipe data : angka dengan koma (float)
data_float = 2.0
print("data : ", data_float)
print("-tipe : ", type(data_float))

#tipe data : kumpulan karakter (string)
data_string = "ikbar"
print("data : ", data_string)
print("-tipe : ", type(data_string))


#tipe data : biner trus/false (boolean)
data_bool = True
print("data : ", data_bool)
print("-tipe : ", type(data_bool))

## Tipe data Khusus
#bilangan Khusus
data_complex = complex(7,8)
print("data : ", data_complex)
print("-tipe : ", type(data_complex))

#tipe data dari bhs C

from ctypes import c_double

data_c_double = c_double(10,5)
print("data : ", data_c_double)
print("-tipe : ", type(data_c_double))