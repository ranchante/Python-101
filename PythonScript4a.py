import getpass
import telnetlib


File1 = open ('IP_SW.txt')
for Linea in File1:
    HOST = Linea.strip()
    print ('Configurando el Switch con IP ' + (HOST))
    # Credenciales del dispositivo
    user = input("Ingrese su cuenta de usuario: ")
    password = getpass.getpass()
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    # password para privilegiado
    tn.write(b'enable \n')
    tn.write(b'class\n')
    tn.write(b'terminal length 0 \n')
    tn.write(b'show runn \n')
    tn.write(b'terminal length 23 \n')
    # Credenciales para cerrar sesion 
    tn.write(b'exit\n')
    readoutput = tn.read_all()
    saveoutput = open('switch_'+ (HOST)+'.txt', 'w') 
    print ('Guardando configuracion en Switch_'+ (HOST))
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
    