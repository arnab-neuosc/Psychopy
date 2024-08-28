from psychopy import visual, core
import numpy as np
from send_opm_trigger import send_ttl_trigger


def calculate_show_feedback(cfgOutput, cfgExp, nstim, blk, cfgScreen, cfgTrigger, cfgEyelink):
    
    #cfgOutput['blkEnd']={}

    # Calculate feedback
    start_idx = (blk) * cfgExp['numTrial']
    end_idx = ((blk+1) * cfgExp['numTrial'])-1
    FB = cfgOutput['presd'][start_idx:end_idx] - cfgExp['corrResp'][start_idx:end_idx]

    TPR = np.sum(FB == 1) / len(FB)  # True Positive Rate
    TNR = np.sum(FB == 0) / len(FB)  # True Negative Rate
    FPR = np.sum(FB == 2) / len(FB)  # False Positive Rate
    FNR = np.sum(FB == -1) / len(FB)  # False Negative Rate

    correct_percentage = (TPR + TNR) * 100
    feedback_text = f"Correct = {correct_percentage:.2f}%"

    # Flip screen
    cfgScreen['window'].flip()

    # Send trigger for end of block
    cfgOutput['blkEnd'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['blkEnd'], cfgEyelink, 'end of block')

    # Draw feedback text
    feedback_stim = visual.TextStim(cfgScreen['window'], text=feedback_text, color=cfgScreen['white'], pos=(0, 0))
    feedback_stim.draw()
    cfgScreen['window'].flip()
    
    # Wait for 3 seconds
    core.wait(3)

    return cfgOutput

