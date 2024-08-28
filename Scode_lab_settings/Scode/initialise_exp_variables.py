import numpy as np
from psychopy import core, event

def initialise_exp_variables(cfgExp):

    #np.random.seed()  # Seed the random number generator

    # Total time: ~44 minutes without breaks (5 to 7.5 sec each trial, ~5.5 min each block)
    cfgExp['numBlock'] = 2  # Total number of blocks
    cfgExp['numTrial'] = 10  # Number of trials in each block
    cfgExp['numStim'] = cfgExp['numTrial'] * cfgExp['numBlock']  # Total number of stimuli
    cfgExp['ITIDur'] = 1000 + (1500 - 1000) * np.random.rand(cfgExp['numStim'])  # ITI duration in ms (jitter between 1 and 1.5 sec)
    cfgExp['cueDur'] = 200  # Duration of cue presentation in ms
    cfgExp['ISIDur'] = 1000  # Interval between cue and stimulus
    cfgExp['stimDur'] = 1000 + (2000 - 1000) * np.random.rand(cfgExp['numStim'])  # Duration of visual stimulus in ms (jitter between 1 and 2 sec)
    cfgExp['dotDur'] = 100  # Duration of red dot presentation
    cfgExp['corrResp'] = np.ones(cfgExp['numStim'], dtype=int)  # 1 => target present, 0 => catch trials
    cfgExp['corrResp'][1::10] = 0  # Every 10th trial is a catch trial
    cfgExp['corrResp'] = np.random.permutation(cfgExp['corrResp'])  # Randomize order of catch trials
    cfgExp['respTimOut'] = 3000  # Time during which subject can respond in ms (3000)

    # Initialize cfgOutput
    cfgOutput = {
        'presd': np.zeros(cfgExp['numStim'], dtype=int),  # Preallocate cfgOutput for unpressed trials
        'keyName': np.zeros(cfgExp['numStim'], dtype=int),  # Preallocate cfgOutput for unpressed trials
        'blkStrtTmPnt': np.zeros(cfgExp['numBlock'], dtype=int),
        'trlStrtTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'cueOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'stmOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'dotOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respStartTime': np.zeros(cfgExp['numStim'], dtype=int),
        'catchOnTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respTmPnt': np.zeros(cfgExp['numStim'], dtype=int),
        'respTmKbQueue': np.zeros(cfgExp['numStim'], dtype=int),
        #'keyName': np.zeros(cfgExp['numStim'], dtype=int),
        'RT_KbQueue': np.zeros(cfgExp['numStim'], dtype=int),
        'RT_trig': np.zeros(cfgExp['numStim'], dtype=int),
        'abrtTmPoint':[],
        'blkEnd': np.zeros(cfgExp['numStim'], dtype=int),
        'endTmPnt':()
        
        
    }

    # # Determine EEG lab and test/train status
    # cfgExp['EEGLab'] = 1 if cfgExp['pc'] == 'EEG' else 0
    # cfgExp['task'] = 1 if cfgExp['test'] == 'task' else 0
    # cfgExp['train'] = 1 if cfgExp['test'] == 'train' else 0
    
    
    if cfgExp['pc'] == 'OPM':
        cfgExp['EEGLab'] = 1
    else:
        cfgExp['EEGLab'] = 0

    if cfgExp['test'] == 'task':
        cfgExp['task'] = 1
    else:
        cfgExp['task'] = 0

    if cfgExp['test'] == 'train':
        cfgExp['train'] = 1
    else:
        cfgExp['train'] = 0

    return cfgExp, cfgOutput



