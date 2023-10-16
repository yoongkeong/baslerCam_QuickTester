from pypylon import pylon
from datetime import datetime
import time
import csv

# Function to detect and access the camera
def detect_and_access_camera(max_wait_time):
    try:
        # Record the start time
        start_time = datetime.now()

        tlf = pylon.TlFactory.GetInstance()
        tl = tlf.CreateTl("BaslerGigE")

        # Keep trying to detect the camera until the max waiting time is reached
        while (datetime.now() - start_time).total_seconds() < max_wait_time:
            try:
                # Create an instant camera object
                camera = pylon.InstantCamera()

                # instantiate the first device on the transport layer
                dev = tl.CreateFirstDevice()

                # attach the device to the InstantCamera class
                camera.attach(dev)
                
                # Open the camera
                camera.Open()

                # Get camera information
                model = camera.GetDeviceInfo().GetModelName()
                serial_number = camera.GetDeviceInfo().GetSerialNumber()

                # Record the time when the camera is successfully detected
                detection_time = datetime.now()

                print(f"Detected camera: {model}, Serial Number: {serial_number}")
                print(f"Start Time: {start_time.strftime('%H:%M:%S')}")
                print(f"Detection Time: {detection_time.strftime('%H:%M:%S')}")

                # Calculate the time difference
                detection_delay = detection_time - start_time
                print(f"Camera detection delay: {detection_delay}")

                # Save the results to a CSV file
                with open('\Test Result\camera_detection_results.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Detected camera", "Serial Number", "Start Time", "Detection Time", "Camera detection delay"])
                    writer.writerow([model, serial_number, start_time.strftime('%H:%M:%S'), detection_time.strftime('%H:%M:%S'), str(detection_delay)])

                # You can add additional actions here if needed
                # Close the camera
                camera.Close()

                # detach the the device from the InstantCamera and release the device with the returned device handle
                tl.DestroyDevice(camera.DetachDevice())

                # unload the transport layer
                tlf.ReleaseTl(tl)

                time.sleep(3)

                return True
            except pylon.GenericException as e:
                if (datetime.now() - start_time).total_seconds() < max_wait_time:
                    print(f"Waiting for camera detection...")
                else:
                    print(f"An error occurred: {e}")
                    return False
        # delete the now empty python objects to prevent further access from python side
        del camera
        del dev
        del tl
        # now all references to the transport layer hardware are released.
    except Exception as e:
        errorMessage = f"An error occurred: {e}"
        print(errorMessage)
        return False

# Main function for Test Mode 1: Power On test
def power_on_test():
    print("Test Mode 1: Power On test")
    
    # Define the maximum waiting time for camera detection (in seconds)
    max_wait_time = 30  # Adjust this value as needed

    # Detect and access the camera, and record the time
    if detect_and_access_camera(max_wait_time):
        print("Camera detected and accessed successfully")
        # Add your delay time recording and test result generation logic here

    else:
        print("Camera detection or access failed")

if __name__ == '__main__':
    power_on_test()
