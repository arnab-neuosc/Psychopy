from psychopy import core, parallel
#import pylink

def send_trigger(cfgTrigger, cfgExp, code, cfgEyelink, eyelinkMsg):
    # send_trigger(cfgTrigger, cfgExp, code, cfgEyelink, eyelinkMsg)
    # Sends trigger during MEG, code should indicate trigger code you want to send
    # eyelinkMsg includes the message you want to send to Eyelink as trigger

    if cfgExp['EEGLab'] == 1:
        # Send trigger code, e.g., 16 (pin 5)
        port = parallel.ParallelPort(address=cfgTrigger['address'])
        port.setData(code)
        core.wait(0.005)  # wait 5ms to turn triggers off
        port.setData(0)  # reset trigger port
    else:
        print('Error Occured during trigger')

    # Get the time point of interest
    timepoint = core.getTime()

    return timepoint


