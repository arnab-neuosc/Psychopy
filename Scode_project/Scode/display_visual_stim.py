from psychopy import visual, core
#import send_trigger
from send_opm_trigger import send_ttl_trigger

def display_visual_stim(presentingStr, nstim, cfgScreen, cfgExp, cfgOutput, cfgStim, cfgTrigger, cfgEyelink):
    #cfgOutput['stmOnTmPnt']={}
    #cfgOutput['dotOnTmPnt']={}
    #cfgOutput['respStartTime']={}
    #cfgOutput['catchOnTmPnt']={}
    
    
    destvecRL=[cfgStim['destVisStimR'],cfgStim['destVisStimL']]
    
    win=cfgScreen['window']

    # Initialize the fixation dot stimulus
    fix_dot_stim = visual.Circle(win, radius=8, fillColor='white', colorSpace='rgb', pos=cfgScreen['fixDotRect'][0])
    fix_dot_flash_stim = visual.Circle(win, radius=8, fillColor='red', colorSpace='rgb')

    if cfgExp['corrResp'][nstim]:
        # Correct response: Display stimulus
        cfgOutput['stmOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['stimOnset'], cfgEyelink, 'stimulus onset')
        #send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['stimOnset'], cfgEyelink, 'stimulus onset')

        for frm in range(cfgExp['stimFrm'][nstim]):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            
            # Draw the fixation dot
            fix_dot_stim.draw()

            # Flip the screen
            cfgScreen['window'].flip()

        # Draw the fixation dot with the red flash for dot presentation
        cfgOutput['dotOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, int(cfgTrigger['dotDir'][nstim][0]), cfgEyelink, f'dot onset to {cfgTrigger["dotDir"][nstim][1]}')
        #send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['stimOnset'], cfgEyelink, f'dot onset to {cfgTrigger["dotDir"][nstim][1]}')

        for frmDot in range(cfgExp['stimFrm'][nstim], cfgExp['stimFrm'][nstim] + cfgExp['dotFrm']):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frmDot].draw()
            presentingStr['visStimL'][nstim][frmDot].draw()
            
            # Draw the fixation dot with the red flash
            fix_dot_stim.draw()
            if cfgStim['cueRndIdx'][nstim] == 2:  # Assuming index 0 means left
                fix_dot_flash_stim.pos = destvecRL[0]
            else:  # Assuming index 1 means right
                fix_dot_flash_stim.pos = destvecRL[1]
            fix_dot_flash_stim.draw()
            
            # Flip the screen
            cfgScreen['window'].flip()
            #core.wait(1)

        cfgOutput['respStartTime'][nstim] = core.getTime()  # Get reaction times relative to stimulus offset
        #respStartTime= core.getTime()

        # Clear the fixation dot
        fix_dot_stim.draw()
        cfgScreen['window'].flip()

    else:
        # Catch trial
        cfgOutput['catchOnTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['catchOnset'], cfgEyelink, 'catch onset')
        #send_ttl_trigger(cfgTrigger, cfgExp, 100, cfgEyelink, 'catch onset')

        for frm in range(cfgExp['stimFrm'][nstim]):
            # Draw the visual stimuli
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            
            # Draw the fixation dot
            fix_dot_stim.draw()

            # Flip the screen
            cfgScreen['window'].flip()

        # Clear the fixation dot
        fix_dot_stim.draw()
        cfgScreen['window'].flip()

        cfgOutput['respStartTime'][nstim] = core.getTime()  # Get reaction times relative to stimulus offset
        #cfgOutput['respStartTime']=core.getTime()

    return cfgOutput


