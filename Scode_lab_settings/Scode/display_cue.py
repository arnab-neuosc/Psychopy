# from psychopy import visual, core
# #import send_trigger

# def display_cue(presentingStr, nstim, cfgStim, cfgScreen, cfgExp, cfgTrigger, cfgOutput, cfgEyelink):

#     # Send trigger for cue onset
#     #cfgOutput['cueOnTmPnt'][nstim] = send_trigger(cfgTrigger, cfgExp, cfgTrigger['cuesDir'][nstim][0], cfgEyelink, f'cue onset to {cfgTrigger["cuesDir"][nstim][1]}')

#     # Draw the cue stimulus and fixation dot for the specified number of frames
#     for frm in range(cfgExp['cueFrm']):
#         # Draw the cue stimulus
#         presentingStr['cueStim'][nstim].draw()
        
#         # Draw the fixation dot
#         fix_dot_stim = visual.Circle(cfgScreen['window'], radius=10, fillColor=cfgScreen['fixDotColor'][0], pos=(15,15),units='pix')
#         fix_dot_stim.draw()

#         cfgScreen['window'].flip()

#     return cfgOutput


# from psychopy import visual, core
# import numpy as np


# def display_cue(presentingStr, nstim, cfgStim, cfgScreen, cfgExp, cfgTrigger, cfgOutput, cfgEyelink):
#     # Convert trigger string to int and send trigger
#     # trigger_value = int(cfgTrigger['cuesDir'][nstim][0])
#     # cfgOutput['cueOnTmPnt'][nstim] = send_trigger(cfgTrigger, cfgExp, trigger_value, cfgEyelink, 
#     #                                               f"cue onset to {cfgTrigger['cuesDir'][nstim][1]}")

#     # Display the cue for the specified number of frames
#     for frm in range(cfgExp['cueFrm']):
#         cue_texture = presentingStr['cueStim'][3]

#         # size_x = cue_texture.size[0]
#         # size_y = cue_texture.size[1]

#         cue_texture.size = [0.1, 0.05]

#         # Draw the cue stimulus
#         cue_texture.draw()
#         #cfgScreen['window'].flip()

#         # Draw the fixation dot
#         fix_dot = visual.Circle(cfgScreen['window'], radius=8, fillColor=cfgScreen['fixDotColor'][0], pos=(0, 100), units="pix")
#         fix_dot.draw()

#         # Flip the screen to show both the cue stimulus and the fixation dot
#         cfgScreen['window'].flip()

#         # Wait for the specified inter-frame interval (ifi)
#         core.wait(cfgScreen['waitFrm'] * cfgScreen['ifi'])

#     return cfgOutput

# Example usage (assuming cfgScreen, cfgExp, etc. are defined):
# cfgOutput = display_cue(presentingStr, nstim, cfgStim, cfgScreen, cfgExp, cfgTrigger, cfgOutput, cfgEyelink)

# Example usage (assuming cfgScreen, cfgExp, etc. are defined):
# cfgOutput = display_cue(presentingStr, nstim, cfgStim, cfgScreen, cfgExp, cfgTrigger, cfgOutput, cfgEyelink)









from psychopy import visual, core
from send_opm_trigger import send_ttl_trigger


def display_cue(cfgScreen, presentingStr, nstim, cfgStim, cfgExp, cfgTrigger, cfgOutput, cfgEyelink):

    # Send trigger for cue onset
    cfgOutput['cueOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, int(cfgTrigger['cuesDir'][nstim][0]), cfgEyelink, 'Step1')
    
    # Load and prepare the cue stimulus
    cue_texture = presentingStr['cueStim'][nstim]

    # Loop over frames for the duration of the cue
      # equivalent to cfgScreen.ifi in MATLAB
    win=cfgScreen['window']
    vbl =  cfgScreen['vbl'] # Equivalent to the start VBL timestamp

    for frm in range(cfgExp['cueFrm']):
        # Draw the cue stimulus
        cue_texture.draw()

        # Draw the fixation dot
        fix_dot = visual.Circle(win, radius=8, fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
        fix_dot.draw()

        # Flip the window at the correct time
        win.flip(vbl + (cfgScreen['waitFrm'] - 0.5) * cfgScreen['ifi'])

    return cfgOutput

