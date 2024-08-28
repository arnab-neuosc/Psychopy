from psychopy import event
from psychopy.hardware import keyboard

def KbQueue_start_routine(cfgExp):
    """
    KbQueue_start_routine(cfgExp)
    Starts the keyboard routine to start listening.
    A call to kb.getKeys() is required for participant's response.
    """
    # Define key names
    cfgExp['quitKey'] = 'escape'  # quit key
    cfgExp['noKey'] = 'n'  # no key
    cfgExp['yesKey'] = 'y'  # yes response
    cfgExp['respKey'] = 'y'  # keyboard response

    cfgExp['activeKeys'] = [cfgExp['quitKey'], cfgExp['respKey'], cfgExp['yesKey'], cfgExp['noKey']]

    # Create a keyboard object and start listening
    cfgExp['kb'] = keyboard.Keyboard()
    cfgExp['kb'].start()

    # Flush any existing keyboard events
    cfgExp['kb'].clearEvents()

    return cfgExp


