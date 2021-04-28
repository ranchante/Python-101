
from netmiko import ConnectHandler

iosv_l2_S1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.31',
	'username': 'admin2',
	'password': 'cisco',
}

iosv_l2_S2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.32',
	'username': 'admin2',
	'password': 'cisco',
}

iosv_l2_S3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.33',
	'username': 'admin2',
	'password': 'cisco',
}

iosv_l2_S4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.34',
	'username': 'admin2',
	'password': 'cisco',
}


all_switchs = [iosv_l2_S1,iosv_l2_S1,iosv_l2_S2,iosv_l2_S3,iosv_l2_S4]

for switch in all_switchs:
    print('Configurando el dispositivo ')
    net_connect = ConnectHandler(**switch)
    Archivo = input('ingrese el archivo de configuracion:')
    for Linea in Archivo:
        Comando = Linea.strip()
        config_commands = Comando
        output = net_connect.send_config_set(config_commands)
        print(output)
    print ('Verificando la configuracion :')
    output = net_connect.send_command('show runn')
    print(output)
    
