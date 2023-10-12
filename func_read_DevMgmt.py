import wmi

def get_usb_device_info():  #List out all connected USB devices
    try:
        # Connect to the Windows Management Instrumentation (WMI) service
        w = wmi.WMI()

        # Query USB devices
        usb_devices = w.Win32_PnPEntity()
        
        for device in usb_devices:
            if "USB" in device.Description:
                print("Device Name:", device.Name)
                print("Device Description:", device.Description)
                print("Device Hardware ID:", device.PNPDeviceID)
                print("-----")

    except Exception as e:
        print("Error:", e)

def print_usb_controller_properties(): #Print all properties available for all USB devices
    try:
        # Connect to the Windows Management Instrumentation (WMI) service
        w = wmi.WMI()

        # Query USB controllers (Universal Serial Bus controllers)
        usb_controllers = w.Win32_USBHub()

        for controller in usb_controllers:
            if isinstance(controller, wmi._wmi_object):
                print("Controller Name:", controller.Name)
                
                # Get all properties of the USB controller
                for prop in controller.Properties_:
                    print(f"{prop.Name}: {prop.Value}")

                print("----------------------------------------")
            else:
                print("Found an unexpected object:", controller)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_usb_device_info()
    print_usb_controller_properties()

