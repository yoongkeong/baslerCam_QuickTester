import subprocess

# Run powercfg and capture the output
output = subprocess.check_output(["powercfg", "/query"], text=True)
output_winPowerSetting = subprocess.check_output(["powercfg", "-getactivescheme"])

# Process the output, e.g., split it into lines and filter relevant data
lines = output.split('\n')
for line in lines:
    if "Subgroup GUID" in line:
        print(line)
    elif "Power Setting GUID" in line:
        print(line)
    elif "Possible Setting Index" in line:
        print(line)
    elif "Possible Setting Friendly Name" in line:
        print(line)
    elif "Minimum Possible Setting" in line:
        print(line)
    elif "Maximum Possible Setting" in line:
        print(line)
    elif "Possible Settings increment" in line:
        print(line)
    elif "Possible Settings units" in line:
        print(line)
    elif "Current AC Power Setting Index" in line:
        print(line)
    elif "Current DC Power Setting Index" in line:
        print(line)
    elif "Current DC Power Setting Index" in line:
        print(line)
