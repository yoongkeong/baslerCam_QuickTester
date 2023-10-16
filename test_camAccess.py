from pypylon import pylon

# Function to extract camera information
def extract_camera_information():
    # Create an instant camera object
    camera = pylon.InstantCamera()
    camera.Open()

    # Device Information
    device_model_name = camera.DeviceModelName.GetValue()
    device_version = camera.DeviceVersion.GetValue()
    device_firmware_version = camera.DeviceFirmwareVersion.GetValue()
    device_id = camera.DeviceID.GetValue()

    # Transport Layer
    gev_current_ip_configuration = camera.GevCurrentIPConfiguration.GetValue()
    gev_mac_address = camera.GevMACAddress.GetValue()
    gev_current_ip_address = camera.GevCurrentIPAddress.GetValue()
    gev_current_subnet_mask = camera.GevCurrentSubnetMask.GetValue()
    gev_link_speed = camera.GevLinkSpeed.GetValue()
    gev_scdct = camera.GevSCDCT.GetValue()
    gev_scps_packet_size = camera.GevSCPSPacketSize.GetValue()
    gev_scpd = camera.GevSCPD.GetValue()
    gev_scftd = camera.GevSCFTD.GetValue()
    payload_size = camera.PayloadSize.GetValue()

    # Configuration Sets
    user_set_selector = camera.UserSetSelector.GetValue()
    user_set_default_selector = camera.UserSetDefaultSelector.GetValue()
    default_set_selector = camera.DefaultSetSelector.GetValue()

    camera.Close()

    # Replace empty values with 'N/A'
    def replace_empty_with_na(value):
        return value if value else 'N/A'

    return {
        "Device Information": {
            "Device Model Name": replace_empty_with_na(device_model_name),
            "Device Version": replace_empty_with_na(device_version),
            "Device Firmware Version": replace_empty_with_na(device_firmware_version),
            "Device ID": replace_empty_with_na(device_id)
        },
        "Transport Layer": {
            "Gev Current IP Configuration": replace_empty_with_na(gev_current_ip_configuration),
            "Gev MAC Address": replace_empty_with_na(gev_mac_address),
            "Gev Current IP Address": replace_empty_with_na(gev_current_ip_address),
            "Gev Current Subnet Mask": replace_empty_with_na(gev_current_subnet_mask),
            "Gev Link Speed": replace_empty_with_na(gev_link_speed),
            "Gev SCDCT": replace_empty_with_na(gev_scdct),
            "Gev SCPSPacketSize": replace_empty_with_na(gev_scps_packet_size),
            "Gev SCPD": replace_empty_with_na(gev_scpd),
            "Gev SCFTD": replace_empty_with_na(gev_scftd),
            "Payload Size": replace_empty_with_na(payload_size)
        },
        "Configuration Sets": {
            "User Set Selector": replace_empty_with_na(user_set_selector),
            "User Set Default Selector": replace_empty_with_na(user_set_default_selector),
            "Default Set Selector": replace_empty_with_na(default_set_selector)
        }
    }

if __name__ == '__main__':
    camera_data = extract_camera_information()
    # You can save this data to a JSON file or use it in the report generation script.
