import base64

val_hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
val_byte = bytearray.fromhex(val_hex) # This line convert hex value to bytes / Esta linea convierte el valor hex a bytes.
val_b64 = base64.b64encode(val_byte) # This line encode the bytes in Base64 / Esta linea codifica los bytes en Base64.

print("Valor Hexadecimal: ", val_hex)
print("Valor en Byte: ", val_byte)
print("Toma tu flag en Base64, nene: ", val_b64)
