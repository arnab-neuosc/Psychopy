# from psychopy import visual, monitors
# from psychopy.tools.monitorunittools import mm2deg

# def initialise_screen_variables(cfgExp):
#     cfgScreen = {}

#     # Get the screen number (draw to the external screen if available)
#     cfgScreen['scrNum'] = 0  # Usually 0 is the primary screen in PsychoPy

#     if cfgExp['EEGLab']:
#         cfgScreen['distance'] = 60  # Distance from participant to the projector in cm
#         cfgScreen['dispSize'] = {'width': 502, 'height': 282}  # Physical size of screen in cm
#         screen_width_px, screen_height_px = visual.Window.size
#         cfgScreen['resolution'] = {'width': screen_width_px, 'height': screen_height_px}
#     else:
#         mon = monitors.Monitor('testMonitor')
#         cfgScreen['dispSize'] = {'width': mon.getWidth(), 'height': mon.getSizePix()[1] / (mon.getSizePix()[0] / mon.getWidth())}
#         cfgScreen['distance'] = 60  # Distance from participant to the monitor in cm
#         screen_width_px, screen_height_px = visual.Window.size
#         cfgScreen['resolution'] = {'width': screen_width_px, 'height': screen_height_px}

#     # Colors and font size
#     cfgScreen['black'] = 0
#     cfgScreen['white'] = 255
#     cfgScreen['grey'] = cfgScreen['white'] / 2
#     cfgScreen['backgroundColor'] = cfgScreen['black']
#     cfgScreen['fntSize'] = 50

#     # Screen settings based on task or train
#     if cfgExp['task'] or cfgExp['train']:
#         cfgScreen['fullScrn'] = [0, 0, cfgScreen['resolution']['width'], cfgScreen['resolution']['height']]  # Full screen for task/train
#     else:
#         cfgScreen['fullScrn'] = [300, 300, 900, 900]  # Smaller screen during testing

#     return cfgScreen


### update on 12 August
from psychopy import visual, monitors, colors
import numpy as np

def initialise_screen_variables(cfgExp):
    cfgScreen = {}
    
    # Get the screen number
    cfgScreen['scrNum'] = 0  # In PsychoPy, screen 0 is typically the primary screen, adjust as necessary
    
    if cfgExp['EEGLab']:
        cfgScreen['distance'] = 60  # Distance from participant to screen in cm
        cfgScreen['dispSize'] = {'width': 1024, 'height': 768}  # Physical size of screen in cm
        # Get the resolution of the screen
        monitor = monitors.Monitor(name='testMonitor', width=cfgScreen['dispSize']['width'], distance=cfgScreen['distance'])
        monitor.setSizePix([1024, 768])  # Set resolution based on your display (example: 1920x1080)
        cfgScreen['resolution'] = {'width': 1024, 'height': 768}
    else:
        # Get the physical size of the screen in millimeters
        monitor = monitors.Monitor(name='default')
        cfgScreen['dispSize'] = {'width': monitor.getWidth(), 'height': monitor.getWidth() / (16/9)}  # Assuming 16:9 aspect ratio
        cfgScreen['distance'] = 60  # Distance from participant to screen in cm
        cfgScreen['resolution'] = {'width': 1024, 'height': 768}  # Example resolution, modify as needed
    
   # Define colors using standard RGB values
    cfgScreen['black'] = [0, 0, 0]  # Black color in RGB
    cfgScreen['white'] = [255, 255, 255]  # White color in RGB
    cfgScreen['grey'] = [128, 128, 128]  # Grey color as the midpoint between black and white
    cfgScreen['backgroundColor'] = cfgScreen['black']
    
    cfgScreen['fntSize'] = 50
    
    # Set screen size (full screen or smaller screen for testing)
    if cfgExp['task'] or cfgExp['train']:
        cfgScreen['fullScrn'] = (0, 0, cfgScreen['resolution']['width'], cfgScreen['resolution']['height'])
    else:
        cfgScreen['fullScrn'] = (300, 300, 900, 900)
    
    return cfgScreen


