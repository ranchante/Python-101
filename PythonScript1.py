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
tn.write(b"int lo 0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
# Cerrar sesion 
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))