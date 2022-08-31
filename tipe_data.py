from ctypes import c_double, c_int16

# tipe data standart yang ada di python
# 1. integer / number
# 2. float
# 3. string (kumpulan karakter)
# 4. biner true / false (boolean)

# tipe data khusus yang ada di python
# 1. bilangan kompleks
# 2. tipe data dari bahasa C

var_integer = 100
print("variable var_integer bertipe: ", type(var_integer))

var_float = 3.14
print("variable var_float bertipe: ", type(var_float))

var_string = "ricky damar saputra"
print("variable var_string bertipe: ", type(var_string))

var_boolean = True
print("variable var_boolean bertipe: ", type(var_boolean))

var_complex = complex(5, 6)
print("variable var_complex bertipe: ", type(var_complex))

var_c_double = c_double(10.5)
print("variable var_c_double bertipe: ", type(var_c_double))

var_c_int16 = c_int16(5)
print("variable var_c_int16 bertipe: ", type(var_c_int16))
