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
    # comandos a modificar
    tn.write(b"configure terminal\n")
    
    for n in range (2,11):
	    tn.write(b"vlan "+str(n).encode('ascii')+b"\n")
	    tn.write(b"name vlan "+str(n).encode('ascii')+b"\n")
    
    # cerrar sesion 
    tn.write(b'end\n')
    tn.write(b'exit\n')
    print(tn.read_all().decode('ascii'))
    