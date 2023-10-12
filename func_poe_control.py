import netmiko
import time

#SSH channel
device = {"host": "192.168.0.10","username": "cisco","password": "cisco","device_type":"cisco_s300"}

Connect = netmiko.ConnectHandler(**device)

print('Connected switch :' + Connect.find_prompt())

def poe_on(boolean):
    if boolean == True :
        print("Activating POE")
        Connect.enable()
        Connect.send_command("configure terminal", expect_string=r"#")
        Connect.send_command("interface gi5", expect_string=r"#")
        Connect.send_command("power inline auto",expect_string=r"#")
        Connect.send_command("commit",expect_string=r"#")
        Connect.send_command("end",expect_string=r"#")
        time.sleep(10)
        print('POE activated')
    else:
        print('Disabling POE')
        Connect.enable()
        Connect.send_command("configure terminal", expect_string=r"#")
        Connect.send_command("interface gi5", expect_string=r"#")
        Connect.send_command("power inline never",expect_string=r"#")
        Connect.send_command("commit",expect_string=r"#")
        Connect.send_command("end",expect_string=r"#")
        time.sleep(5)
        print("POE Disabled")

def check_poe():
    Connect.enable()
    check_status = Connect.send_command("show power inline")
    print(check_status)
    if 'Never' in check_status:
        status_poe = 'off'
        print("POE OFF!")
    else:
        print("POE ON!")
        status_poe = 'on'
    return status_poe

# poe_on(True)
# check_poe()
poe_on(False)
check_poe()

# poe_on(True)
# check_poe()

