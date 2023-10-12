import subprocess

def get_ipconfig_all():
    try:
        ipconfig_output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)
        return ipconfig_output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}\n{e.output}"
    except FileNotFoundError:
        return "Error: 'ipconfig' command not found. This script is for Windows only."

if __name__ == "__main__":
    ipconfig_info = get_ipconfig_all()
    print(ipconfig_info)
