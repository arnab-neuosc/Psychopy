from psychopy import visual
from angle2pix import angle2pix

#def CenterRect(rect, windowRect):
    # Function to center one rectangle (rect) within another (windowRect)
   # xCenter = windowRect[0] + (windowRect[2] - windowRect[0]) / 2
   # yCenter = windowRect[1] + (windowRect[3] - windowRect[1]) / 2
    #rectWidth = rect[2] - rect[0]
    #rectHeight = rect[3] - rect[1]
    #return [xCenter - rectWidth / 2, yCenter - rectHeight / 2, xCenter + rectWidth / 2, yCenter + rectHeight / 2]

def visual_stim_properties(cfgScreen, cfgStim):
    cfgScreen['windowRect']=[0,0,1024,768]
    cfgStim['destVisStimR']=[256,0]
    cfgStim['destVisStimL'] = [-256,0]
    cfgStim['rectRL'] = [0,0]
    cfgStim['destCue'] = [0,-256]
    # Convert visual angle to pixels for the destination rectangle width and height
    #destRectWPixels = angle2pix(cfgScreen, cfgStim['destRectW'])
    #destRectHPixels = angle2pix(cfgScreen, cfgStim['destRectH'])

    # Define the destination rectangle for the visual stimulus centre
    #cfgStim['destVisStimCentre'] = [-256,0]
    #cfgStim['destVisStimCentre'] = CenterRect(cfgStim['destVisStimCentre'], cfgScreen['windowRect'])

    # Convert visual angles to pixels for the positions to the right and left
    #visStimToRPixels = angle2pix(cfgScreen, cfgStim['visStimToR'])
    #visStimToLPixels = angle2pix(cfgScreen, cfgStim['visStimToL'])

    # Calculate the destination rectangles for the right and left visual stimuli
    #cfgStim['destVisStimR'] = [
    #cfgStim['destVisStimCentre'][i] + visStimToRPixels[i] for i in range(4)
   # ]
   # cfgStim['destVisStimL'] = [
   # cfgStim['destVisStimCentre'][i] - visStimToLPixels[i] for i in range(4)
   # ]
   
   

# Calculate the centre of visual stimuli (for dot flash presentation)
    #cfgStim['rectRL'] = [
    #CenterRect(cfgScreen['fixDotRect'][1], cfgStim['destVisStimR']),
    #CenterRect(cfgScreen['fixDotRect'][1], cfgStim['destVisStimL'])
    #]

# Define the destination rectangle for the cue
   # destRectCueSizePixels = angle2pix(cfgScreen, cfgStim['destRectCueSize'])
   # rectCue = [0, 0, destRectCueSizePixels, destRectCueSizePixels]

# Convert the cue position to pixels and adjust the destination cue rectangle
    # cueToBPixels = angle2pix(cfgScreen, cfgStim['cueToB'])
    # centeredRectCue = CenterRect(rectCue, cfgScreen['windowRect'])
    # cfgStim['destCue'] = [
    # centeredRectCue[0] + cueToBPixels[0],
    # centeredRectCue[1] + cueToBPixels[1],
    # centeredRectCue[2] + cueToBPixels[2],
    # centeredRectCue[3] + cueToBPixels[3]
    # ]

    return cfgStim