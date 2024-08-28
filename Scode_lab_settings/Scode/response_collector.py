# from psychopy import core, visual
# from psychopy.hardware import keyboard
# #from send_trigger import send_trigger
# from send_opm_trigger import send_ttl_trigger
# from cleanup import cleanup

# def response_collector(cfgExp, cfgOutput, cfgTrigger, nstim, cfgTxt, cfgScreen, cfgFile, cfgEyelink, cfgStim):
#     # Initialize the keyboard
#     kb = keyboard.Keyboard()
#     win=cfgScreen['window']
#     # Set a flag to keep the loop running until a response is collected
#     noResp = True

#     # Start the keyboard for timing
#     kb.clock.reset()
#     # Ensure both are lists and then concatenate
#     keyList = (cfgExp['respKey'] if isinstance(cfgExp['respKey'], list) else [cfgExp['respKey']]) + (cfgExp['quitKey'] if isinstance(cfgExp['quitKey'], list) else [cfgExp['quitKey']])

#     while noResp:
#         # Check for key presses
#         keys = kb.getKeys(keyList=keyList, waitRelease=False)

#         if keys:
#             # Take the first key press (if multiple keys are pressed simultaneously)
#             key = keys[0].name
#             timestamp = keys[0].rt

#             if key in cfgExp['respKey']:  # If the key pressed is one of the response keys
#                 cfgOutput['respTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['resp'], cfgEyelink, 'button press onset')
#                 core.wait(0.002)  # Wait to make sure the response trigger is reset
#                 cfgOutput['respTmKbQueue'][nstim] = timestamp  # Exact time of button press#
                
#                 cfgOutput['keyName'][nstim] = 256  # Which key was pressed
                
#                 cfgOutput['presd'][nstim] = 2  # Collect all responses for hit rate and correct rejection analysis
                
#                 cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmKbQueue'][nstim] - cfgOutput['respStartTime'][nstim]  # Calculate RT using the timing info

#                 if cfgExp['corrResp'][nstim]:
#                     cfgOutput['RT_trig'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['dotOnTmPnt'][nstim]  # Calculate RT using triggers

#                 noResp = False  # Exit the loop since a response has been registered
#                 break
            

#             elif key == cfgExp['quitKey']:  # If the quit key is pressed
#                 cfgScreen['window'].flip()
#                 quit_text = visual.TextStim(win, text=cfgTxt['quitTxt'], color=[1, 1, 1], colorSpace='rgb', pos=(0, 0))
#                 quit_text.draw()
#                 cfgScreen['window'].flip()

#                 # Wait for the user to confirm quitting
#                 keys = kb.waitKeys(keyList=[cfgExp['yesKey'], cfgExp['noKey']])
#                 if cfgExp['yesKey'] in [key.name for key in keys]:
#                     cfgOutput['abrtTmPoint'] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['abort'], cfgEyelink, 'experiment aborted by user')
#                     print('Experiment aborted by user')
#                     cfgOutput = cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim)
#                     break
#         else:
#             cfgOutput['presd'][nstim] = 0
#                 #prsd=0

#         # Check if response time exceeded the timeout
#         if (core.getTime() - cfgOutput['respStartTime'][nstim]) > cfgExp['respTimOut']:
#         #if (core.getTime() - cfgOutput['respStartTime']) > cfgExp['respTimOut']:
#             noResp=False
#             cfgOutput['keyName'][nstim] = 0
#             break
         
#         noResp = False
            
#         cfgOutput['keyName'][nstim] = 0
#         break
#     return cfgOutput



from psychopy import core, visual, event
from psychopy.hardware import keyboard
from send_opm_trigger import send_ttl_trigger
from cleanup import cleanup
#from psychopy.iohub import launchHubServer
#from psychopy.core import getTime

def response_collector(cfgExp, cfgOutput, cfgTrigger, nstim, cfgTxt, cfgScreen, cfgFile, cfgEyelink, cfgStim):
    # Initialize the keyboard
    #io = launchHubServer()
    #kb = io.devices.keyboard
    kb = keyboard.Keyboard()
    win = cfgScreen['window']
    noResp = True

    # Start the keyboard clock
    kb.clock.reset()
    kb.clearEvents()

    # Concatenate response keys and quit key into a single list
    keyList = (cfgExp['respKey'] if isinstance(cfgExp['respKey'], list) else [cfgExp['respKey']]) + \
              (cfgExp['quitKey'] if isinstance(cfgExp['quitKey'], list) else [cfgExp['quitKey']])

    while noResp:
        # Check the elapsed time since the start of response collection
        elapsed_time = core.getTime() - cfgOutput['respStartTime'][nstim]

        # Check for key presses
        event.clearEvents('keyboard')
        keys = kb.waitKeys(waitRelease=False,maxWait=2)
        #keys=keyboard.waitForPresses(keyList=keyList, waitRelease=False,maxWait=5.0)
        #keys = kb.waitForPresses(maxWait=5.0)


        if keys:
            key = keys[0].name
            timestamp = keys[0].rt

            if elapsed_time <= cfgExp['respTimOut']:  # Check if response is within the timeout period
                if key in cfgExp['respKey']:
                    print('Response Received')
                    cfgOutput['respTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['resp'], cfgEyelink, 'button press onset')
                    core.wait(0.002)  # Ensure response trigger is reset
                    cfgOutput['respTmKbQueue'][nstim] = timestamp
                    cfgOutput['keyName'][nstim] = 256
                    cfgOutput['presd'][nstim] = 2
                    cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmKbQueue'][nstim] - cfgOutput['respStartTime'][nstim]

                    if cfgExp['corrResp'][nstim]:
                        cfgOutput['RT_trig'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['dotOnTmPnt'][nstim]

                    noResp = False  # Exit the loop
                    break

                elif key == cfgExp['quitKey']:
                    cfgScreen['window'].flip()
                    quit_text = visual.TextStim(win, text=cfgTxt['quitTxt'], color=[1, 1, 1], colorSpace='rgb', pos=(0, 0))
                    quit_text.draw()
                    cfgScreen['window'].flip()

                    # Wait for the user to confirm quitting
                    keys = kb.waitKeys(keyList=[cfgExp['yesKey'], cfgExp['noKey']])
                    if cfgExp['yesKey'] in [key.name for key in keys]:
                        cfgOutput['abrtTmPoint'] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['abort'], cfgEyelink, 'experiment aborted by user')
                        print('Experiment aborted by user')
                        cfgOutput = cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim)
                        break
            else:  # If the elapsed time exceeds the timeout, assign keyName to zero
                print('No Response')
                cfgOutput['keyName'][nstim] = 0
                cfgOutput['presd'][nstim] = 0
                noResp = False
                break

        else:
            # If no key is pressed, check if response time exceeded the timeout
            cfgOutput['keyName'][nstim] = 0
            cfgOutput['presd'][nstim] = 0
            noResp = False
            break

    return cfgOutput




