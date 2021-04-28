
from netmiko import ConnectHandler

iosv_l2_S1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.31',
	'username': 'admin2',
	'password': 'cisco123!',
}

iosv_l2_S2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.32',
	'username': 'admin2',
	'password': 'cisco123!',
}

iosv_l2_S3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.33',
	'username': 'admin2',
	'password': 'cisco123!',
}

iosv_l2_S4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.34',
	'username': 'admin2',
	'password': 'cisco123!',
}


all_switchs = [iosv_l2_S1,iosv_l2_S1,iosv_l2_S2,iosv_l2_S3,iosv_l2_S4]

for switch in all_switchs:
	print('Configurando el dispositivo ')
	net_connect = ConnectHandler(**switch)
	print('Las vlan actualmente configuradas: ')
	output = net_connect.send_command('show vlan brief')
	print(output)

	print('Creando las vlan 2 al 10')
	for n in range (2,11):
		print('Creando VLAN '+str(n))
		config_commands = ['Vlan ' + str(n), 'name vlan_'+str(n)]
		output = net_connect.send_config_set(config_commands)
		print(output)

	print ('Verificando las vlans Creadas')
	output = net_connect.send_command('show vlan brief')
	print(output)
