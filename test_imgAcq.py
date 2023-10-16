from pypylon import pylon

# Declare SensorWidth and SensorHeight outside the function
SensorWidth = 0  # Replace with the actual sensor width value
SensorHeight = 0  # Replace with the actual sensor height value

# Function to capture an image and check dimensions
def image_capture_test(expected_width, expected_height):
    try:
        # Create an instant camera object
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

        # Open the camera
        camera.Open()

        # Capture an image
        camera.StartGrabbing(pylon.GrabStrategy_LatestImages)
        img = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Get the image dimensions
        image_data = img.Array
        image_width, image_height = image_data.shape[1], image_data.shape[0]

        global SensorWidth, SensorHeight  # Declare these as global variables

        # Set the global SensorWidth and SensorHeight
        SensorWidth = camera.SensorWidth.GetValue()
        SensorHeight = camera.SensorHeight.GetValue()

        # Check image dimensions
        if image_width == expected_width and image_height == expected_height:
            print("Image dimensions matched.")
        else:
            print("Image dimensions do not match.")
            width_difference = abs(image_width - expected_width)
            height_difference = abs(image_height - expected_height)
            print(f"Width Difference: {width_difference}")
            print(f"Height Difference: {height_difference}")

        # Close the camera
        camera.Close()

        return True

    except pylon.GenericException as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    expected_width = SensorWidth  # Use the global SensorWidth
    expected_height = SensorHeight  # Use the global SensorHeight

    if image_capture_test(expected_width, expected_height):
        # Perform additional tests or analysis if needed
        pass
