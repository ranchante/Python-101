import getpass
import telnetlib

# indica aqui la ip del eqtuipo
HOST = '192.168.1.31'

# Credenciales del dispositivo
user = input("Ingrese su cuenta de usuario: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
# cambia "login : " por "Username: " 
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

# password para privilegiado
tn.write(b"enable\n")
tn.write(b"class\n")
# comandos a modificar
tn.write(b"configure terminal\n")

for n in range (2,11):
	#VlanNumber = "vlan "+str(n)
	#VlanName   = "name Vlan_"+str(n)
	#tn.write(VlanNumber.encode('ascii') + b"\n")
	#tn.write(VlanName.encode('ascii') + b"\n")
	tn.write(b"vlan "+str(n).encode('ascii')+b"\n")
	tn.write(b"name vlan "+str(n).encode('ascii')+b"\n")

# Cerrar sesion 
tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))
