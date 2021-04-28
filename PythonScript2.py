import getpass
import telnetlib

# indica aqui la ip del eqtuipo
HOST = "192.168.1.31"

# Credenciales del dispositivo
user = input("Ingrese su cuenta de usuario: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
# cambia "login : " por "Username: " 
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# password para privilegiado
tn.write(b"enable\n")
tn.write(b"class\n")
# comandos a modificar
tn.write(b"configure terminal\n")
tn.write(b"vlan 2\n")
tn.write(b"name vlan_02\n")
tn.write(b"vlan 3\n")
tn.write(b"name vlan_03\n")
tn.write(b"vlan 4\n")
tn.write(b"name vlan_04\n")
tn.write(b"vlan 5\n")
tn.write(b"name vlan_05\n")
tn.write(b"vlan 6\n")
tn.write(b"name vlan_06\n")
tn.write(b"vlan 7\n")
tn.write(b"name vlan_07\n")
tn.write(b"vlan 8\n")
tn.write(b"name vlan_08\n")
tn.write(b"vlan 9\n")
tn.write(b"name vlan_09\n")
tn.write(b"vlan 10\n")
tn.write(b"name vlan_10\n")

# Cerrar sesion 
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))