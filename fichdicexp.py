#!/usr/bin/python3

fich = open("/etc/passwd", "r")

users = fich.readlines()
users_dic = {}

for user in users:
    tokens = user.split(':')
    users_dic[tokens[0]] = tokens[-1][:-1]
fich.close()

try:
    print('root ', users_dic["root"])
    print('imaginario', users_dic["imaginario"])
except KeyError:
    print("No existe el usuario introducido")
