from psychopy import visual, core, event, logging, prefs
import time

def basic_setup_experiment():

    # Basic setup
    cfgEyelink = {}

    # Check if the user wants to skip the sync test
    inp1 = input('Do you want to skip sync test? y/n').strip().lower()
    if inp1 == 'y':
        skipSync = True
        logging.warning('Sync test is skipped! Do not continue if it is an actual recording!')
        m = input('Do you want to continue? y/n   ').strip().lower()
        while True:
            if m == 'y':
                break
            elif m == 'n':
                raise Exception('The experiment aborted by operator.')
    else:
        skipSync = False

    # Set preference for skipping sync tests
    prefs.hardware['audioLib'] = ['pyo']  # Ensures audio library is set
    prefs.general['winType'] = 'pyglet'
    if skipSync:
        logging.warning('Sync test is being skipped')
        prefs.general['skipSync'] = True
    else:
        prefs.general['skipSync'] = False

    dummy = time.time()

    # Check if the user wants to use Eyelink
    inp3 = input('Do you want to use Eyelink? y/n').strip().lower()
    if inp3 == 'y':
        cfgEyelink['on'] = True
    else:
        logging.warning('Eyelink is off! Do not continue if it is an actual recording!')
        m = input('Do you want to continue? y/n').strip().lower()
        while True:
            if m == 'y':
                cfgEyelink['on'] = False
                break
            elif m == 'n':
                raise Exception('The experiment aborted by operator.')

    return cfgEyelink

