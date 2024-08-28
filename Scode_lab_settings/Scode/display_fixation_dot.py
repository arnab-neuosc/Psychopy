# from psychopy import visual, core

# def display_fixation_dot(cfgScreen, cfgExp, nstim, ITI, cfgOutput):

#     # Define the fixation dot stimulus
#     fix_dot_stim = visual.Circle(cfgScreen['window'], radius=5, fillColor=cfgScreen['fixDotColor'], pos=cfgScreen['fixDotPos'])

#     if ITI:
#         # ITI phase
#         for frm in range(int(cfgExp['ITIFrm'][nstim] / 2)):
#             # Just flip the screen (no fixation dot)
#             cfgScreen['window'].flip()

#         for frm in range(int(cfgExp['ITIFrm'][nstim] / 2), int(cfgExp['ITIFrm'][nstim])):
#             # Draw the fixation dot
#             fix_dot_stim.draw()
#             # Flip the screen
#             cfgScreen['window'].flip()

#     else:
#         # ISI phase
#         for frm in range(cfgExp['ISIFrm']):
#             # Draw the fixation dot
#             fix_dot_stim.draw()
#             # Flip the screen
#             cfgScreen['window'].flip()

#     return cfgOutput

# from psychopy import visual, core

# def display_fixation_dot(cfgScreen, cfgExp, nstim, ITI, cfgOutput):
    
#     win=cfgScreen['window']

#     # Define the fixation dot stimulus
#     fix_dot_stim = visual.Circle(win, radius=5, fillColor='red', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])

#     if ITI:
#         # ITI phase
#         for frm in range(int(cfgExp['ITIFrm'][nstim] / 2)):
#             # Just flip the screen (no fixation dot)
#             cfgScreen['window'].flip()

#         for frm in range(int(cfgExp['ITIFrm'][nstim] / 2), int(cfgExp['ITIFrm'][nstim])):
#             # Draw the fixation dot
#             fix_dot_stim.draw()
#             # Flip the screen
#             cfgScreen['window'].flip()

#     else:
#         # ISI phase
#         for frm in range(cfgExp['ISIFrm']):
#             # Draw the fixation dot
#             fix_dot_stim.draw()
#             # Flip the screen
#             cfgScreen['window'].flip()

#     return cfgOutput


from psychopy import visual, core

def display_fixation_dot(cfgScreen, cfgExp, nstim, ITI, cfgOutput):
    """
    Displays a fixation dot for the duration specified in cfgExp for either ITI or ISI.

    Parameters:
        win: The PsychoPy window object.
        cfgExp: Configuration dictionary with experiment settings.
        nstim: The current stimulus number.
        ITI: Boolean, whether to display during ITI (True) or ISI (False).
        cfgOutput: Configuration dictionary for output settings.

    Returns:
        cfgOutput: Updated configuration dictionary for output settings.
    """
    win=cfgScreen['window']
    
    # Timing variables
    #flip_interval = win.monitorFramePeriod  # equivalent to cfgScreen.ifi in MATLAB
    vbl =  cfgScreen['vbl'] # Equivalent to the start VBL timestamp
    
    if ITI:
        # ITI case: first wait for half of the ITI frames without drawing anything
        for frm in range(int(cfgExp['ITIFrm'][nstim] / 2)):
            win.flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
        
        # Then draw the fixation dot for the remaining ITI frames
        fix_dot = visual.Circle(win, radius=8, fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
        for frm in range(int(cfgExp['ITIFrm'][nstim] / 2), int(cfgExp['ITIFrm'][nstim])):
            fix_dot.draw()
            vbl = win.flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])
    
    else:
        # ISI case: Draw the fixation dot for the entire ISI duration
        fix_dot = visual.Circle(win, radius=8, fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
        for frm in range(int(cfgExp['ISIFrm'])):
            fix_dot.draw()
            vbl = win.flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])

    return cfgOutput
