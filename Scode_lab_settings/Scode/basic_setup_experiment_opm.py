from psychopy import visual, core, event, logging, prefs
import time

from psychopy import gui, logging, prefs
import time

def basic_setup_experiment():
    # Basic setup
    cfgEyelink = {}

    # Create a dialog box for skipping sync test
    dlg = gui.Dlg(title="Experiment Setup")
    dlg.addField('Skip sync test?', choices=['y', 'n'])
    dlg.addField('Use Eyelink?', choices=['y', 'n'])
    user_input = dlg.show()

    if dlg.OK:  # If the user clicked OK
        skipSync = user_input[0].strip().lower() == 'y'
        useEyelink = user_input[1].strip().lower() == 'y'
    else:
        raise Exception('The experiment was aborted by the operator.')

    # Process skipSync input
    if skipSync:
        logging.warning('Sync test is skipped! Do not continue if it is an actual recording!')
        continueDlg = gui.Dlg(title="Warning")
        continueDlg.addText('Do you want to continue?')
        continueDlg.addField('Continue?', choices=['y', 'n'])
        continue_input = continueDlg.show()
        
        if continue_input[0].strip().lower() != 'y':
            raise Exception('The experiment was aborted by the operator.')

    # Set preference for skipping sync tests
    prefs.hardware['audioLib'] = ['pyo']  # Ensures audio library is set
    prefs.general['winType'] = 'pyglet'
    prefs.general['skipSync'] = skipSync

    dummy = time.time()

    # Process useEyelink input
    if useEyelink:
        cfgEyelink['on'] = True
    else:
        logging.warning('Eyelink is off! Do not continue if it is an actual recording!')
        continueDlg = gui.Dlg(title="Warning")
        continueDlg.addText('Do you want to continue?')
        continueDlg.addField('Continue?', choices=['y', 'n'])
        continue_input = continueDlg.show()

        if continue_input[0].strip().lower() != 'y':
            raise Exception('The experiment was aborted by the operator.')
        cfgEyelink['on'] = False

    return cfgEyelink
