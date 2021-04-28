import getpass
import telnetlib

# indica aqui la ip del eqtuipo
HOST = "192.168.1.31"

# Credenciales del dispositivo
user = input("Enter your remote account: ")
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
tn.write(b"terminal length 0 \n")
tn.write(b"show runn \n")
tn.write(b"terminal length 23 \n")

# Cerrar sesion 
tn.write(b"exit\n")

readoutput = tn.read_all()
saveoutput = open('switch.txt', 'w') 
saveoutput.write(readoutput.decode('ascii'))
saveoutput.write("\n")
saveoutput.close
#print(tn.read_all().decode('ascii'))