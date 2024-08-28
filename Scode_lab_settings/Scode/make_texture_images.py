import numpy as np
from psychopy import visual
import random

def make_texture_images(cfgScreen, cfgStim, cfgExp):
    # Initializing the presentingStr dictionary to store the stimuli
    presentingStr = {
        'visStimR': [],
        'visStimL': [],
        'cueStim': []
    }
    visStimR_texture = []
    visStimL_texture = []
    cue_texture=[]

    # Extend visStim to visStimMat as needed (randomly read in R & L visual stim)
    # Assumes each visStim is a list of image file paths or numpy arrays representing images
    num_repeats = int(np.ceil(max(cfgExp['stimFrm']) / 100))
    cfgStim['visStimMat'] = cfgStim['visStim'] * num_repeats
    cfgStim['visStimMat1'] = cfgStim['visStim1'] * num_repeats

    # Create enough visual stimuli for each trial
    max_stim_frames = max(cfgExp['stimFrm']) + 50  # Adding 50 to ensure enough frames
    
    cfgStim['visStimL'] =[]
    
    cfgStim['visStimR']=[]
    

    for stm in range(len(cfgExp['stimFrm'])):
        # Slice to the required number of frames
        cfgStim['visStimR'].append(cfgStim['visStimMat1'][:max_stim_frames])
        cfgStim['visStimL'].append(cfgStim['visStimMat'][:max_stim_frames])
        
        #n=171
    # for i in range(cfgExp['numStim']):
    #     visStimR_texture.append(random.randint(0,1))
    #     visStimL_texture.append(random.randint(0,1))
        

    # Create textures for stim images
    # for readImg in range(cfgExp['numStim']):
        
    #     for frm in range(len(cfgStim['visStimR'][readImg])):
    #         try:
    #             # Load the image into PsychoPy visual.ImageStim and store the texture
    #             # visStimR_texture = visual.ImageStim(cfgScreen['window'], image=cfgStim['visStimR'][readImg][frm],units="pix")
    #             # visStimL_texture = visual.ImageStim(cfgScreen['window'], image=cfgStim['visStimL'][readImg][frm],units="pix")
    #             # visStimR_textures.append(visStimR_texture)
    #             # visStimL_textures.append(visStimL_texture)
    #             visStimR_texture[readImg][frm]=cfgStim['visStimR'][readImg][frm]
    #             visStimL_texture[readImg][frm]=cfgStim['visStimL'][readImg][frm]

    #             # Debugging print statement
    #             print(f"Loaded visStimR image {frm} for stimulus {readImg}")
    #             print(f"Loaded visStimL image {frm} for stimulus {readImg}")
    #         except Exception as e:
    #             print(f"Error loading frame {frm} for stimulus {readImg}: {e}")
    #             #visStimR_textures.append(None)
    #             #visStimL_textures.append(None)

    #     # presentingStr['visStimR'].append(visStimR_textures)
    #     # presentingStr['visStimL'].append(visStimL_textures)
    
    presentingStr['visStimR']=cfgStim['visStimR']
    presentingStr['visStimL']=cfgStim['visStimL']

    # Create textures for cue images
    # for stim in range(cfgExp['numStim']):
    #     try:
    #         # Load the cue image into PsychoPy visual.ImageStim and store the texture
    #         #cue_texture = visual.ImageStim(cfgScreen['window'], image=cfgStim['cueStim'][stim],units="pix")
    #         #presentingStr['cueStim'].append(cue_texture)
    #         cue_texture[stim] =cfgStim['cueStim'][stim]

    #         # Debugging print statement
    #         print(f"Loaded cue image {stim}")
    #     except Exception as e:
    #         print(f"Error loading cue stimulus {stim}: {e}")
    #         #presentingStr['cueStim'].append(None)  # Placeholder for missing images
    
    presentingStr['cueStim']=cfgStim['cueStim']

    return presentingStr

# Example Usage:
# cfgScreen = {'window': visual.Window([800, 600])}
# cfgStim = {'visStim': ['image1.jpg', 'image2.jpg'], 'cueStim': ['cue1.jpg', 'cue2.jpg']}
# cfgExp = {'stimFrm': [10, 20], 'numStim': 2}
# presentingStr = make_texture_images(cfgScreen, cfgStim, cfgExp)
