from psychopy import core, logging
import os
import pylink
import el_start

def initialise_eyelink(cfgFile, cfgEyelink, cfgScreen, cfgExp):
    """
    Initialise Eyelink, set parameters, and start recording.
    
    Parameters:
    cfgFile (dict): Configuration related to files and directories.
    cfgEyelink (dict): Configuration related to Eyelink settings.
    cfgScreen (dict): Configuration related to screen settings.
    cfgExp (dict): Configuration related to the experiment.
    
    Returns:
    dict: Updated cfgEyelink dictionary.
    """
    try:
        if cfgEyelink.get('on', False):
            eyelink_file_path = os.path.join(cfgFile['subDir'], cfgFile['eyelink'])
            if os.path.exists(eyelink_file_path):  # Check whether files already exist for this subject/session
                logging.warning('Eyelink file will be overwritten')
                inp1 = input('Do you want to continue? y/n   ')
                if inp1.lower() == 'n':
                    core.quit()  # Exit PsychoPy
                    raise RuntimeError('Session aborted by operator')
            
            cfgEyelink = el_start(cfgEyelink, cfgScreen, cfgFile, cfgExp)  # Set parameters of Eyelink and calibrate
    except Exception as e:
        logging.warning('Eyetracker setup failed! Eyelink triggers will not be sent!')
        while True:
            inp2 = input('Do you want to continue? y/n   ')
            if inp2.lower() == 'y':
                cfgEyelink['on'] = False
                break
            elif inp2.lower() == 'n':
                core.quit()  # Exit PsychoPy
                raise RuntimeError('The experiment aborted by operator.')

    return cfgEyelink


