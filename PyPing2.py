import subprocess
import platform
 
def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

 
if __name__ == '__main__':
        
    File1 = open ('IP_SW.txt')
    for Linea in File1:
        HOST = Linea.strip()
        if ping_ip(HOST):
            print(f"{HOST} esta Activo")
        else:
            print(f"{HOST} no esta activo")
