#!/usr/bin/env python3
# Don't forget to connect with "nc socket.cryptohack.org 11112" / No olvides conectarte con "nc socket.cryptohack.org 11112".

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "flag" # Replace "clothes" with "flag" / Se sustituye "clothes" por "flag".
}
json_send(request)

response = json_recv()

print(response)
