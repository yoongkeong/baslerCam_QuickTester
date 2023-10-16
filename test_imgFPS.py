from pypylon import pylon

# Function to configure and check maximum frame rate
def max_framerate_test():
    try:
        # Create an instant camera object
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

        # Open the camera
        camera.Open()

        # Set the camera to the maximum possible acquisition frame rate
        camera.AcquisitionFrameRateEnable = True
        camera.AcquisitionFrameRate = camera.ResultingFrameRate.GetValue()

        # Start grabbing continuously
        camera.StartGrabbing(pylon.GrabStrategy_LatestImages)

        # Create an output format string
        output_format = "Max Frame Rate Achieved: {} fps"

        # Continuously check and print the frame rate
        while True:
            img = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

            # Calculate the current frame rate
            current_frame_rate = camera.ResultingFrameRate.GetValue()

            # Check if the maximum frame rate is achieved
            if current_frame_rate == camera.ResultingFrameRate.GetMax():
                print(output_format.format(current_frame_rate))
                break

    except pylon.GenericException as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    max_framerate_test()
