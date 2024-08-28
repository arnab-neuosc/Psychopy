from psychopy import visual, core, event

def visual_stim_variables():

    # Primary settings
    win = visual.Window(
        monitor="testMonitor",  # Use appropriate monitor name or settings
        units="deg",            # Use visual degrees for stimulus positioning
        fullscr=True             # Fullscreen mode
    )

    # Retrieve screen number and resolution
    scr_num = win.monitor.name
    resolution = win.size
    disp_size = (win.monitor.getSizePix()[0] / 25.4, win.monitor.getSizePix()[1] / 25.4)  # Convert pixels to mm

    # Define the settings dictionary
    cfgScreen = {
        'win': win,              # Window object
        'scrNum': scr_num,       # Screen number or monitor name
        'resolution': resolution,  # Screen resolution (pixels)
        'dispSize': {
            'width': disp_size[0],   # Display width in millimeters
            'height': disp_size[1]   # Display height in millimeters
        },
        'distance': 60,            # Distance from participant to projector
        'black': (0, 0, 0),        # Black color in RGB
        'white': (1, 1, 1),        # White color in RGB
        'grey': (0.5, 0.5, 0.5),  # Grey color in RGB
        'fntSize': 50,             # Font size
        'destRectH': 5,            # Height of destination rectangle for stimulus in visual degrees
        'destRectW': 5,            # Width of destination rectangle for stimulus in visual degrees
        'visStimToR': [3, 2, 3, 2],  # Visual degrees from center for right stimuli
        'visStimToL': [3, -2, 3, -2], # Visual degrees from center for left stimuli
        'cueToB': [0, 2, 0, 0]     # Visual degrees from center for cue stimuli
    }

    return cfgScreen


