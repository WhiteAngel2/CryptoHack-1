# Remember to install the PyCryptodome library before running the script / Recuerda instalar la libreria PyCryptodome antes de correr el script.
base10_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

flag = base10_int.to_bytes(33, 'big')
''' In the fourth line the first argument represents the number of characters, the second the size of the block / En la cuarta linea el primer argumento representa la cantidad de 
caracteres, el segundo el tamaño del bloque. '''

print ("Toma tu flag, nene: ")
print (flag)
