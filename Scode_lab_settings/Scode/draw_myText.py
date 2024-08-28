# from psychopy import visual, event, core
# import cleanup, send_trigger
# from psychopy import visual, event, core
# from psychopy.hardware import keyboard

# def draw_myText(cfgScreen, cfgExp, text, cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim):
#     # Initialize window
#     win = cfgScreen['window']

#     # Clear the window
#     win.flip()

#     # Draw the text
#     message = visual.TextStim(win, text=text, color=cfgScreen['white'], pos=(0, 0))
#     message.draw()

#     # Flip the window to show the text
#     win.flip()

#     notWaiting = False  # Only enable the experimenter to continue/start

#     while not notWaiting:
#         keys = event.waitKeys(keyList=[cfgExp['yesKey'], cfgExp['noKey'], cfgExp['quitKey']])
#         contPressed = keys[0]

#         if contPressed == cfgExp['yesKey']:
#             notWaiting = True
#         elif contPressed in [cfgExp['noKey'], cfgExp['quitKey']]:
#             # Clear the window
#             win.flip()

#             # Draw the quit text
#             quit_message = visual.TextStim(win, text=cfgTxt['quitTxt'], color=cfgScreen['white'], pos=(0, 0))
#             quit_message.draw()

#             # Flip the window to show the quit text
#             win.flip()

#             abort_keys = event.waitKeys(keyList=[cfgExp['yesKey']])
#             abrtPressed = abort_keys[0]

#             if abrtPressed == cfgExp['yesKey']:
#                 cfgOutput['abrtTmPoint'] = send_trigger(cfgTrigger, cfgExp, cfgTrigger['abort'], cfgEyelink, 'Experiment aborted by user')  # Send the quit trigger
#                 cfgOutput = cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim)
#                 print('Experiment aborted by user')
#                 break

#         event.clearEvents()
#         core.wait(0.5)

#     return cfgOutput

# #Example usage (assuming cfgScreen, cfgExp, etc. are defined):
# #cfgOutput = draw_myText(cfgScreen, cfgExp, "Sample Text", cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim)



from psychopy import visual, event, core
from cleanup import cleanup
from psychopy.hardware import keyboard

def draw_myText(cfgScreen, cfgExp, text, cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim):
    """
    Draws white text in the center of the screen and waits for the experimenter
    to press "y" to continue.
    """
    win=cfgScreen['window']
    
    # Clear the screen by flipping the window (this will show a blank screen)
    win.flip()

    # Draw the text in the center of the screen
    message = visual.TextStim(win, text=text, color=cfgScreen['white'], pos=(0, 0))
    message.draw()

    # Flip the screen to display the text
    win.flip()

    # Waiting for the experimenter's response
    notWaiting = False
    while not notWaiting:
        # Wait for a key press
        keys = event.waitKeys()

        # Check which key was pressed
        if cfgExp['yesKey'] in keys:
            notWaiting = True
        elif cfgExp['noKey'] in keys or cfgExp['quitKey'] in keys:
            # Clear the screen
            win.flip()

            # Draw the quit text
            quit_message = visual.TextStim(win, text=cfgTxt['quitTxt'], color=[1, 1, 1], colorSpace='rgb', pos=(0, 0))
            quit_message.draw()

            # Flip the screen to display the quit text
            win.flip()

            # Wait for the user's decision
            abrt_keys = event.waitKeys()

            if cfgExp['yesKey'] in abrt_keys:
                # Send the abort trigger (assuming send_trigger is a function you've defined)
                #cfgOutput['abrtTmPoint'] = send_trigger(cfgTrigger, cfgExp, cfgTrigger['abort'], cfgEyelink, 'Experiment aborted by user')

                # Call the cleanup function (assuming cleanup is a function you've defined)
                print('Experiment aborted by user')
                cfgOutput = cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim)

                # Log a warning message and break the loop
                
                break
        
        # Clear events and wait for a short period to prevent excessive CPU usage
        event.clearEvents()
        core.wait(0.5)

    return cfgOutput




