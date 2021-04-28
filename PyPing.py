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
    current_ip_address = ['192.168.1.21','192.168.1.31','192.168.1.32', '192.168.1.33', '192.168.1.34', '192.168.1.1']
    for each in current_ip_address:
        if ping_ip(each):
            print(f"{each} esta Activo")
        else:
            print(f"{each} no esta activo")
