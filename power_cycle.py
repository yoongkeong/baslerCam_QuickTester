from pypylon import pylon
from pypylon import genicam
from datetime import datetime
import pandas as pd
import poe_control as poe

#User interface

def main():
    # test_mode = input('Choose test mode: A - Power Cycle, B- Long run, C- Power long run')
    test_mode = 'A'
    # print(test_mode)
    start_test_time,start_test_timeSTR = get_time_string()
    if test_mode == 'A':
        print('Begin Power Cycle test' + "  Current Timestamp:  "+ start_test_timeSTR)
        power_cycle()
        end_test_time,end_test_timeSTR = get_time_string()
        print('Test ended at :  '+ end_test_timeSTR)
        time_taken = end_test_time - start_test_time
        print("Total test time:  " + str(time_taken) + " <---(H:MM:SS.xxx)")
    else:
        print('Other test not available, pls restart')

def get_time_string():
    current_time = datetime.now()
    currentdatetimeSTR = current_time.strftime("%d/%m/%Y_%H:%M:%S")
    return current_time, currentdatetimeSTR
#Talk to PoE switch
#Camera accessibility
def power_cycle():
    # numberOfImagesToGrab = int(input('Insert number of image grabbed each test'))
    numberOfImagesToGrab = 50
    test_iteration = 0
    user_input_test_iteration = 2
    iteration_list = []
    result_list = []
    while test_iteration < user_input_test_iteration :
        try:
            poe.poe_on(False)
            poe.check_poe()
            poe.poe_on(True)
            poe.check_poe()
            camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            camera.Open()
            modelDUT= camera.GetDeviceInfo().GetModelName()
            SNDUT = camera.GetDeviceInfo().GetSerialNumber()
            print("Connected device: ", modelDUT)
            print("Serial Number: ",SNDUT)
            camera.StartGrabbingMax(numberOfImagesToGrab)
            while camera.IsGrabbing():
                grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

            if grabResult.GrabSucceeded():
            # Access the image data.
                print("SizeX: ", grabResult.Width)
                print("SizeY: ", grabResult.Height)
                img = grabResult.Array
                print("Gray value of first pixel: ", img[0, 0])
                print("Grab success!  " + "Number of images grabbed: " + str(numberOfImagesToGrab))

            success = grabResult.GrabSucceeded()
            grabResult.Release()
            camera.Close()

            if success == False:
                final_result = "FAILED"
                print('Power Cycle failed, camera did not grab successfully')
            else:
                final_result = "PASSED"
                pass
            test_iteration += 1
            iteration_list.append(test_iteration)
            result_list.append(final_result)
        except genicam.GenericException as e:
            #Error handling.
            print("An exception occurred.")
            print(e.GetDescription())
            exitCode = 1
    power_cycle_result = pd.DataFrame(
        {'No. of iteration' : iteration_list,
        'Test result': final_result}
    )
    print(power_cycle_result)

if __name__ == '__main__':
    main()