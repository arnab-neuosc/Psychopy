from psychopy import visual, core
from angle2pix import angle2pix
def fix_dot_properties(cfgScreen):

    # Fixation dot properties
    cfgScreen['fixDotCentreBig'] = cfgScreen['centre']  # Center coordinates of the fixation dot
    #cfgScreen['fixDotSizeBig'] = 0.7  # Size in visual degrees
    #cfgScreen['fixDotRectBig'] = [
        #cfgScreen['fixDotCentreBig'][0] - angle2pix(cfgScreen, cfgScreen['fixDotSizeBig'] / 2),
        #cfgScreen['fixDotCentreBig'][1] - angle2pix(cfgScreen, cfgScreen['fixDotSizeBig'] / 2),
       # cfgScreen['fixDotCentreBig'][0] + angle2pix(cfgScreen, cfgScreen['fixDotSizeBig'] / 2),
        #cfgScreen['fixDotCentreBig'][1] + angle2pix(cfgScreen, cfgScreen['fixDotSizeBig'] / 2)
    #]
    cfgScreen['fixDotRectBig'] =[0,5]
    cfgScreen['fixDotColorBig'] = [-1, -1, 1.0]  # White color

    cfgScreen['fixDotCentreSmall'] = cfgScreen['centre']  # Center coordinates of the fixation dot
    #cfgScreen['fixDotSizeSmall'] = 0.4  # Size in visual degrees
    #cfgScreen['fixDotRectSmall'] = [
        #cfgScreen['fixDotCentreSmall'][0] - angle2pix(cfgScreen, cfgScreen['fixDotSizeSmall'] / 2),
        #cfgScreen['fixDotCentreSmall'][1] - angle2pix(cfgScreen, cfgScreen['fixDotSizeSmall'] / 2),
        #cfgScreen['fixDotCentreSmall'][0] + angle2pix(cfgScreen, cfgScreen['fixDotSizeSmall'] / 2),
        #cfgScreen['fixDotCentreSmall'][1] + angle2pix(cfgScreen, cfgScreen['fixDotSizeSmall'] / 2)
    #]
    cfgScreen['fixDotRectSmall'] = [0,0]
    cfgScreen['fixDotColorSmall'] = [1.0, -1, -1]  # Black color

    # Inputs to 'visual.Circle'
    cfgScreen['fixDotRect'] = [
        cfgScreen['fixDotRectBig'],
        cfgScreen['fixDotRectSmall']
    ]
    cfgScreen['fixDotColor'] = [
        cfgScreen['fixDotColorBig'],
        cfgScreen['fixDotColorSmall']
    ]
    cfgScreen['fixDotFlashColor'] = [1, 0, 0]  # Red color when flashing

    return cfgScreen




