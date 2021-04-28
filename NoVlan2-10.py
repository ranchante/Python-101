import getpass
import telnetlib

# Credenciales de los dispositivos
user = input("Ingrese su cuenta de usuario: ")
password = getpass.getpass()


File1 = open ('IP_SW.txt')
for Linea in File1:
    HOST = Linea.strip()
    print ('Configurando el Switch con IP ' + (HOST))
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
    print ('Eliminando las Vlan del 2 al 10 del Switch ' + (HOST))
    tn.write(b"configure terminal\n")
    tn.write(b"no vlan 2-10\n")
    #tn.write(b"do wr\n")
    # cerrar sesion 
    tn.write(b'end\n')
    tn.write(b'exit\n')
    print(tn.read_all().decode('ascii'))
print ('Proceso Finalizado')

    