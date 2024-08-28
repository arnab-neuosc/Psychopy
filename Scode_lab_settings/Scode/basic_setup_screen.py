from psychopy import visual, core, event, prefs
from psychopy.visual import TextStim, Window
import ctypes

def basic_setup_screen(cfgScreen):

    win = cfgScreen['window']

    # Blend function
    win.blendMode = 'avg'  # Equivalent to GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA in PTB

    # Query the frame duration
    cfgScreen['ifi'] = win.getMsPerFrame()[0] / 1000.0  # Frame interval in seconds
    cfgScreen['refRate'] = 1.0 / cfgScreen['ifi']  # Frame refresh rate in Hz

    # Assuming we can get the nominal frame rate from the monitor properties or set it explicitly
    cfgScreen['FRDatapixx'] = win.getActualFrameRate()  # Actual frame rate

    cfgScreen['waitFrm'] = 1  # Wait for this many frames when presenting stim

    # Size of the on-screen window
    cfgScreen['WinXpix'], cfgScreen['WinYpix'] = win.size

    # Centre coordinates
    cfgScreen['centre'] = [win.size[0] // 2, win.size[1] // 2]

    # Set the maximum priority for this program
    # Note: PsychoPy doesn't have a direct equivalent of MaxPriority and Priority
    # but we can use ctypes to set high priority on Windows
    # try:
    #     ctypes.windll.user32.SetThreadPriority(ctypes.windll.kernel32.GetCurrentThread(), -15)  # high priority
    # except:
    #     pass

    # # Hide the cursor
    # event.Mouse(visible=False)
    
    core.rush(True)

    # Set text size for stimuli presented in the window
    cfgScreen['window'].textSize = cfgScreen['fntSize']  # Make sure fntSize is defined in cfgScreen

    # Hide the cursor over the window
    cfgScreen['window'].mouseVisible = False

    return cfgScreen