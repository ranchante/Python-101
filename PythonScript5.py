
from netmiko import ConnectHandler

iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.31',
	'username': 'admin2',
	'password': 'cisco123!',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show vlan brief')
print(output)


for n in range (2,11):
	print('Creando VLAN '+str(n))
	config_commands = ['Vlan ' + str(n), 'name vlan_'+str(n)]
	output = net_connect.send_config_set(config_commands)
	print(output)

output = net_connect.send_command('show vlan brief')
print(output)