from psychopy import visual, core

def make_texture_images(cfgScreen, cfgStim, cfgExp):


    presentingStr = {
        'visStimR': [],
        'visStimL': [],
        'cueStim': []
    }

    
    visStimMat = [cfgStim['visStim']] * (int(max(cfgExp['stimFrm']) / 100) + 1)
    
    
    for stm in range(len(cfgExp['stimFrm'])):
        visStimR = visStimMat[:max(cfgExp['stimFrm']) + 50]
        visStimL = visStimMat[:max(cfgExp['stimFrm']) + 50]
        presentingStr['visStimR'].append([visual.ImageStim(cfgScreen['window'], image=img) for img in visStimR])
        presentingStr['visStimL'].append([visual.ImageStim(cfgScreen['window'], image=img) for img in visStimL])

    
    for readImg in range(cfgExp['numStim']):
        presentingStr['visStimR'][readImg] = [visual.ImageStim(cfgScreen['window'], image=img) for img in presentingStr['visStimR'][readImg]]
        presentingStr['visStimL'][readImg] = [visual.ImageStim(cfgScreen['window'], image=img) for img in presentingStr['visStimL'][readImg]]

    
    for stim in range(cfgExp['numStim']):
        presentingStr['cueStim'].append(visual.ImageStim(cfgScreen['window'], image=cfgStim['cueStim'][stim]))

    return presentingStr


cfgScreen = {
    'window': visual.Window([800, 600], fullscr=False)  # Example window setup
}
cfgStim = {
    'visStim': 'path/to/visualStim.png',  # Example image path
    'cueStim': ['path/to/cue1.png', 'path/to/cue2.png']  # Example cue images
}
cfgExp = {
    'stimFrm': [10, 20, 30],  # Example frame durations
    'numStim': 2  # Example number of stimuli
}



