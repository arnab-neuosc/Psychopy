from psychopy import visual, event, core

def show_instructions(cfgScreen, cfgTxt, cfgExp, presentingStr, cfgStim):
    # Initialization and first screen flip
    win=cfgScreen['window']
    win.flip()  # Clear the screen
    fixDotColor = cfgScreen['fixDotColor']
    fixDotFlashColor = cfgScreen['fixDotFlashColor']
    fixDotRect = cfgScreen['fixDotRect']
    cueRndIdx = cfgStim['cueRndIdx'][1]
    rectRL = cfgStim['rectRL'][cueRndIdx-1]
    

    # Display Instruction Text 1
    instrTxt1 = cfgTxt['instrTxt'][0]
    textStim1 = visual.TextStim(win, text=instrTxt1, color=cfgScreen['white'], pos=(0, 0))
    textStim1.draw()
    win.flip()

    # Wait for Key Press to Continue
    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys(keyList=[cfgExp['yesKey']])
        if keys and keys[0] == cfgExp['yesKey']:
            notWaiting = True
        event.clearEvents()
        core.wait(1)

    # Display Instruction Text 2
    instrTxt2 = cfgTxt['instrTxt'][1]
    textStim2 = visual.TextStim(cfgScreen['window'], text=instrTxt2, color=cfgScreen['white'], pos=(0, 0))
    textStim2.draw()
    win.flip()

    # Wait for Key Press to Continue
    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys(keyList=[cfgExp['yesKey']])
        if keys and keys[0] == cfgExp['yesKey']:
            notWaiting = True
        event.clearEvents()
        core.wait(1)

    # Display Instruction Text 3
    instrTxt3 = cfgTxt['instrTxt'][2]
    textStim3 = visual.TextStim(cfgScreen['window'], text=instrTxt3, color=cfgScreen['white'], pos=(0, 0))
    textStim3.draw()
    win.flip()

    # Wait for Key Press to Continue
    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys(keyList=[cfgExp['yesKey']])
        if keys and keys[0] == cfgExp['yesKey']:
            notWaiting = True
        event.clearEvents()
        core.wait(1)

    # Display Instruction Text 4
    instrTxt4 = cfgTxt['instrTxt'][3]
    textStim4 = visual.TextStim(cfgScreen['window'], text=instrTxt4, color=cfgScreen['white'], pos=(0, 0))
    textStim4.draw()
    win.flip(cfgScreen['vbl'] + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])

    # Wait for Key Press to Continue
    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys(keyList=[cfgExp['yesKey']])
        if keys and keys[0] == cfgExp['yesKey']:
            notWaiting = True
        event.clearEvents()
        core.wait(1)
    # Draw textures








# Initialize the PsychoPy window (assuming window size and other properties)
#win = visual.Window([800, 600], fullscr=False, units='pix')

# Example configuration (these should be set according to your experimental setup)
    # cfgScreen = {
    #     'window': win,
    #     'fixDotColor': [[1,1,1],[0,0,0]],  # Color of the fixation dot
    #     'fixDotFlashColor': [1,0,0],  # Color of the cue dot
    #     'fixDotRadius': 5,  # Radius of the fixation dot
    #     #'fixDotPos': [0, 0],  # Position of the fixation dot
    #     #'fixDotRect': [0, 0],  # Placeholder for the fixation dot position
    #     'vbl': 0,  # Placeholder for vertical blank time
    #     'waitFrm': 1,  # Placeholder for frame wait time
    #     'ifi': 1 / 60.0  # Inverse frame interval (assuming 60 Hz refresh rate)
    #     }

    # cfgStim = {
    #     'destVisStimR': [1039, 408, 1407, 776],  # Position for the right visual stimulus
    #     'destVisStimL': [513, 408,881,776],  # Position for the left visual stimulus
    #     'rectRL': [[1213, 582,1233,602], [687,582, 707,602]],  # Placeholder for cue rectangle positions
    #     'cueRndIdx': [0, 1]  # Index for cue (0 for left, 1 for right)
    #     }

    # cfgExp = {
    #     'yesKey': 'space',  # Key to continue/start the experiment
    #     'deviceNum': None  # Device number (not needed in PsychoPy)
    #     }

#Initialize stimuli (assuming images are properly stored and paths are valid)
    image1=presentingStr['visStimR'][0][1]
    image2=presentingStr['visStimL'][1][1]


# # # Set positions for the textures
#     image1.pos = (-256,0)
#     image2.pos = (+256,0)
    destvecRL=[cfgStim['destVisStimR'],cfgStim['destVisStimL']]
    
# #     # size_x = presentingStr['visStimR'][0][1].size[0]
# #     # size_y = presentingStr['visStimR'][0][1].size[1]
    
# #     # size_x1 = presentingStr['visStimL'][0][1].size[0]
# #     # size_y1 = presentingStr['visStimL'][0][1].size[1]

# #     presentingStr['visStimR'][0][1].size = [100,100]
# #     presentingStr['visStimL'][0][1].size = [100,100]

# # Draw the textures at their respective positions
#     #image1.draw()
#     #win.flip()
#     #event.waitKeys()
#     #image2.draw()
#     #win.flip()
#     #event.waitKeys()

# # Draw the fixation dot and the cue dot
#     fix_dot = visual.Circle(win, radius=5, fillColor=[255,0,0],colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
#     flash_pos = destvecRL[cfgStim['cueRndIdx'][1]-1]  # Use index to select cue position
#     flash_dot = visual.Circle(win, radius=5, fillColor=[0,0,255],colorSpace='rgb', pos=flash_pos)
    
#     image1.draw()
#     #win.flip()
#     #event.waitKeys()
#     image2.draw()

#     fix_dot.draw()
#     flash_dot.draw()

# # Flip the screen to show everything drawn
#     win.flip()
#    # event.waitKeys()

# # Wait for the experimenter to press the continue/start key
#     notWaiting = False
#     while not notWaiting:
#         keys = event.waitKeys(keyList=[cfgExp['yesKey']], clearEvents=True)
#         if cfgExp['yesKey'] in keys:
#             notWaiting = True
#         core.wait(0.5)  # Wait for a short period to prevent excessive CPU usage

# # Close the window when done
#     #win.close()
#     #core.quit()
#     right_pos = (-200, 0)  # 200 pixels to the right of the center
#     left_pos = (-200, 0)

# # Set positions for the textures
#     image1.pos = right_pos
#     image2.pos = left_pos
    
    # Draw the textures (image1 and image2) at their respective positions
    image1.draw()
    image2.draw()
    
    # Flip the screen to show the images
    win.flip()
    
    # Keep images on screen and wait for 2 seconds
    core.wait(2)
    
    # Draw the fixation dot in addition to the images
    fix_dot = visual.Circle(win, radius=8, fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
    
    image1.draw()  # Draw images again since flip clears the screen
    image2.draw()
    fix_dot.draw()
    
    # Flip the screen to show the fixation dot along with images
    win.flip()
    
    # Keep images and fixation dot on screen and wait for another 2 seconds
    core.wait(2)
    
    # Draw the flash dot in addition to the images and fixation dot
    flash_pos = destvecRL[cfgStim['cueRndIdx'][1] - 1]  # Use index to select cue position
    flash_dot = visual.Circle(win, radius=8, fillColor='red', colorSpace='rgb', pos=flash_pos)
    
    image1.draw()  # Draw images again since flip clears the screen
    image2.draw()
    fix_dot.draw()  # Draw fixation dot again
    flash_dot.draw()
    
    # Flip the screen to show the flash dot along with images and fixation dot
    win.flip()

# Keep everything on screen for 5 seconds
    core.wait(5)

    # Wait for the experimenter to press the continue/start key
    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys(keyList=[cfgExp['yesKey']], clearEvents=True)
        if cfgExp['yesKey'] in keys:
            notWaiting = True
        core.wait(0.0005)  # Wait for a short period to prevent excessive CPU usage
    
    # Close the window when done (if needed)
    # win.close()
    # core.quit()
    
    
#     # Create a rectangle to the left
#     left_rect = visual.Rect(
#     win=win,
#     width=100,     # Width of 100 pixels
#     height=100,    # Height of 100 pixels
#     fillColor='red'  # 200 pixels to the left of center
#     )

# # Create a rectangle to the right
#     right_rect = visual.Rect(
#     win=win,
#     width=100,
#     height=100,
#     fillColor='green'   # 200 pixels to the right of center
#     )
    
#     left_rect.pos=[-200,0]
#     right_rect.pos=[200,0]

# # Draw rectangles
#     left_rect.draw()
#     right_rect.draw()

# # Update the window to display the rectangles
#     win.flip()

# # Wait for 3 seconds
#     core.wait(3)


