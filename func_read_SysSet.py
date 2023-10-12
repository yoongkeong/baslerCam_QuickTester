import psutil
import datetime
import os
import socket
import wmi
import platform

def get_network_cards():
    network_cards = []
    for interface, addrs in psutil.net_if_addrs().items():
        card_info = {"Interface Name": interface}
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4 addresses
                card_info["IPv4 Address"] = addr.address
                card_info["Netmask"] = addr.netmask
            elif addr.family == socket.AF_INET6:  # IPv6 addresses
                card_info["IPv6 Address"] = addr.address
                card_info["Netmask"] = addr.netmask
        network_cards.append(card_info)
    return network_cards

def time_zone():
    return datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()

def hotfixes():
    import winreg
    hotfixes = []
    try:
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages") as subkey:
                hotfixes = [winreg.EnumKey(subkey, i) for i in range(winreg.QueryInfoKey(subkey)[0])]
    except Exception:
        pass
    return hotfixes

def virtualization_requirements():
    w = wmi.WMI()
    requirements = {
        "VM Monitor Mode Extensions": "No",
        "Virtualization Enabled In Firmware": "No",
        "Second Level Address Translation": "No",
        "Data Execution Prevention Available": "No",
    }

    try:
        for prop in w.Win32_ComputerSystem():
            requirements["VM Monitor Mode Extensions"] = "Yes" if prop.VirtualizationFirmwareEnabled else "No"
            requirements["Virtualization Enabled In Firmware"] = "Yes" if prop.VirtualizationFirmwareEnabled else "No"
    except AttributeError:
        pass

    try:
        for prop in w.Win32_Processor():
            requirements["Second Level Address Translation"] = "Yes" if prop.SecondLevelAddressTranslationExtensions else "No"
    except AttributeError:
        pass

    return requirements


def get_system_information():
    system_info = {
        "Host Name": os.environ['COMPUTERNAME'],
        "OS Name": platform.system(),
        "OS Version": platform.platform(),
        "OS Manufacturer": "Microsoft Corporation",
        "OS Configuration": "Standalone Workstation",
        "OS Build Type": os.environ['PROCESSOR_ARCHITECTURE'],
        "Registered Owner": "CyberOptics",
        "Registered Organization": "",
        "Product ID": "",
        "Original Install Date": datetime.datetime.fromtimestamp(os.path.getctime("C:/")).strftime("%d/%m/%Y, %I:%M:%S %p"),
        "System Boot Time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%Y, %I:M:%S %p"),
        "System Manufacturer": "",
        "System Model": "",
        "System Type": os.environ['PROCESSOR_IDENTIFIER'],
        "Processor(s)": psutil.cpu_count(logical=False),
        "BIOS Version": "",
        "Windows Directory": os.environ['WINDIR'],
        "System Directory": os.environ['SYSTEMROOT'] + "\\System32",
        "Boot Device": "",
        "System Locale": "en-us;English (United States)",
        "Input Locale": "en-us;English (United States)",
        "Time Zone": time_zone(),
        "Total Physical Memory": psutil.virtual_memory().total,
        "Available Physical Memory": psutil.virtual_memory().available,
        "Virtual Memory: Max Size": psutil.swap_memory().total,
        "Virtual Memory: Available": psutil.swap_memory().free,
        "Virtual Memory: In Use": psutil.swap_memory().used,
        "Page File Location(s)": "",
        # "Domain": "",
        # "Logon Server": "",
        # "Hotfix(s)": hotfixes(),
        "Network Card(s)": get_network_cards(),
        "Hyper-V Requirements": virtualization_requirements(),
    }

    return system_info

def write_to_text_file(system_info, filename):
    with open(filename, 'w') as file:
        file.write("SYSTEM INFORMATION:\n\n")
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    system_info = get_system_information()
    output_file = "system_info.txt"
    write_to_text_file(system_info, output_file)
    print(f"System information has been written to {output_file}")