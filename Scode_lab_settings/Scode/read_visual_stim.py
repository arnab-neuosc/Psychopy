import os
import re
import numpy as np
from psychopy import visual

def read_visual_stim(cfgFile, cfgExp, cfgStim, cfgTrigger,cfgScreen):
    # Directory Search for Stimulus and Cue Files
    win=cfgScreen['window']
    fileDirStim = [f for f in os.listdir(cfgFile['stim']) if f.endswith('.bmp')]  # only use the files ending in .bmp
    fileDirCue = [f for f in os.listdir(cfgFile['cue']) if f.endswith('.jpg')]  # only use the files ending in .jpg

    # Sorting the Stimulus Files by Number in Filename
    idx = sorted(range(len(fileDirStim)), key=lambda i: int(re.search(r'(?<=cube3D)\d+', fileDirStim[i]).group()))
    cfgStim['fNameStimSortd'] = [fileDirStim[i] for i in idx]

    # Preallocation for Visual Stimulus and Cue Stimulus
    
    cfgStim['visStim'] = [None] * 150
    cfgStim['visStim1'] = [None] * 150
    
    for spd in range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']):
        index = spd // cfgStim['stimRotSpeed']
        if index < len(cfgStim['visStim']):
            cfgStim['visStim'][index] = visual.ImageStim(win, image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]),pos=(-256,0))
            cfgStim['visStim1'][index] = visual.ImageStim(win, image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]),pos=(256,0))



    # # Reading Stimulus Images
    # for spd in range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']):
    #     cfgStim['visStim'][spd] = visual.ImageStim(win, image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]))
   
    cfgStim['visStim'] = [stim for stim in cfgStim['visStim'] if stim is not None]  # remove empty indices
    cfgStim['visStim1'] = [stim for stim in cfgStim['visStim1'] if stim is not None]

    # Randomizing Cue Indices
    np.random.seed(None)  # equivalent to 'rng('shuffle')' in MATLAB
    cfgStim['cueRndIdx'] = np.random.permutation(cfgExp['numStim'])

    # Ensuring an Equal Number of 1s and 2s in Cue Indices
    cfgStim['cueRndIdx'][cfgStim['cueRndIdx'] % 2 == 0] = 2
    cfgStim['cueRndIdx'][cfgStim['cueRndIdx'] % 2 != 0] = 1
    
    cfgStim['cueStim'] = [None] * cfgExp['numStim']
    #cfgStim['cueStim1'] = [None] * cfgExp['numStim']

    # Reading Cue Images Randomly
    for stim in range(cfgExp['numStim']):
        cfgStim['cueStim'][stim] = visual.ImageStim(win, image=os.path.join(cfgFile['cue'], fileDirCue[cfgStim['cueRndIdx'][stim] - 1]),pos=(0,-256))
        #cfgStim['cueStim1'][stim]=visual.ImageStim(win,image=os.path.join(cfgFile['cue'], fileDirCue[cfgStim['cueRndIdx'][stim] - 1]))
    # Preallocation for Correct Responses, Cue, Stim, and Dot Triggers
    cfgExp['cuesDir'] = [None] * cfgExp['numStim']
    cfgTrigger['cuesDir'] = [[None, None] for _ in range(cfgExp['numStim'])]
    cfgTrigger['dotDir'] = [[None, None] for _ in range(cfgExp['numStim'])]

    # Assigning Directions and EEG Trigger Codes
    right_indices = np.where(cfgStim['cueRndIdx'] == 1)[0]
    left_indices = np.where(cfgStim['cueRndIdx'] == 2)[0]
    no_resp_indices = np.where(cfgExp['corrResp'] == 0)[0]

    for idx in right_indices:
        cfgExp['cuesDir'][idx] = 'Right'
        cfgTrigger['cuesDir'][idx][0] = '1'
        cfgTrigger['cuesDir'][idx][1] = 'Right'
        cfgTrigger['dotDir'][idx][0] = '6'
        cfgTrigger['dotDir'][idx][1] = 'Right'

    for idx in left_indices:
        cfgExp['cuesDir'][idx] = 'Left'
        cfgTrigger['cuesDir'][idx][0] = '2'
        cfgTrigger['cuesDir'][idx][1] = 'Left'
        cfgTrigger['dotDir'][idx][0] = '7'
        cfgTrigger['dotDir'][idx][1] = 'Left'

    for idx in no_resp_indices:
        cfgExp['cuesDir'][idx] = 'no resp'
        cfgTrigger['cuesDir'][idx] = ['100', 'no resp']
        cfgTrigger['dotDir'][idx] = ['100', 'no resp']

    return cfgStim, cfgExp, cfgTrigger


    # # Reading Stimulus Images
    # for spd in range(0, len(cfgStim['fNameStimSortd']), cfgStim['stimRotSpeed']):
    #     cfgStim['visStim'][spd] = visual.ImageStim(win, image=os.path.join(cfgFile['stim'], cfgStim['fNameStimSortd'][spd]))
    # cfgStim['visStim'] = [stim for stim in cfgStim['visStim'] if stim is not None]  # remove empty indices

    # # Randomizing Cue Indices
    # np.random.seed(None)  # equivalent to 'rng('shuffle')' in MATLAB
    # cfgStim['cueRndIdx'] = np.random.permutation(cfgExp['numStim'])

    # # Ensuring an Equal Number of 1s and 2s in Cue Indices
    # cfgStim['cueRndIdx'][cfgStim['cueRndIdx'] % 2 == 0] = 2
    # cfgStim['cueRndIdx'][cfgStim['cueRndIdx'] % 2 != 0] = 1

    # # Reading Cue Images Randomly
    # for stim in range(cfgExp['numStim']):
    #     cfgStim['cueStim'][stim] = visual.ImageStim(win, image=os.path.join(cfgFile['cue'], fileDirCue[cfgStim['cueRndIdx'][stim] - 1]))

    # # Preallocation for Correct Responses, Cue, Stim, and Dot Triggers
    # cfgExp['cuesDir'] = [None] * cfgExp['numStim']
    # cfgTrigger['cuesDir'] = [[None, None] for _ in range(cfgExp['numStim'])]
    # cfgTrigger['dotDir'] = [[None, None] for _ in range(cfgExp['numStim'])]

    # # Assigning Directions and EEG Trigger Codes
    # right_indices = np.where(cfgStim['cueRndIdx'] == 1)[0]
    # left_indices = np.where(cfgStim['cueRndIdx'] == 2)[0]
    # no_resp_indices = np.where(cfgExp['corrResp'] == 0)[0]

    # for idx in right_indices:
    #     cfgExp['cuesDir'][idx] = 'Right'
    #     cfgTrigger['cuesDir'][idx][0] = '1'
    #     cfgTrigger['cuesDir'][idx][1] = 'Right'
    #     cfgTrigger['dotDir'][idx][0] = '6'
    #     cfgTrigger['dotDir'][idx][1] = 'Right'

    # for idx in left_indices:
    #     cfgExp['cuesDir'][idx] = 'Left'
    #     cfgTrigger['cuesDir'][idx][0] = '2'
    #     cfgTrigger['cuesDir'][idx][1] = 'Left'
    #     cfgTrigger['dotDir'][idx][0] = '7'
    #     cfgTrigger['dotDir'][idx][1] = 'Left'

    # for idx in no_resp_indices:
    #     cfgExp['cuesDir'][idx] = 'no resp'
    #     cfgTrigger['cuesDir'][idx] = ['no resp', 'no resp']
    #     cfgTrigger['dotDir'][idx] = ['no resp', 'no resp']

    # return cfgStim, cfgExp, cfgTrigger



