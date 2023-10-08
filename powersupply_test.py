import ea_psu_controller as psu

device = psu.PsuEA(comport='COM9')
print(device.get_status())