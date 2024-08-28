from psychopy import visual, core, event, logging
import pylink
import os

def el_start(cfgEyelink, cfgScreen, cfgFile, cfgExp):
    """
    Open screen for calibration, calibrate and start recording.
    """
    # Create the window
    win = visual.Window(size=cfgScreen['size'], fullscr=True, screen=cfgScreen['screen'], 
                        units='pix', allowGUI=False, monitor=cfgScreen['monitor'])

    try:
        # Initialize the Eyelink connection
        tracker = pylink.EyeLink(cfgEyelink['trackerIP'])
        tracker.open()
        
        if not tracker.isConnected():
            logging.error('Eyelink Init aborted.')
            cleanup(tracker, win)
            return
        
        logging.info('Eyelink initialized')

        # Check if the Eyelink file already exists
        if os.path.exists(os.path.join(cfgFile['subDir'], cfgFile['eyelink'])):
            cont = input('Warning! Eyelink file will be overwritten, do you want to continue? (y/n) ').strip().lower()
            while cont not in ['y', 'n']:
                cont = input('Please enter y or n: ').strip().lower()
            if cont == 'n':
                raise RuntimeError('The experiment aborted by operator.')

        # Open the EDF file
        status = tracker.openFile(cfgFile['eyelink'])
        if status:
            raise RuntimeError(f'Could not open EDF file on Eyelink computer, error: {status}')
        else:
            logging.info('EDF file opened on Eyelink computer')

        # Set custom parameters
        el_set_parameters(tracker, cfgScreen, cfgExp)

        logging.info('Starting Calibration')
        tracker.doTrackerSetup()

        logging.info('Start Eyetrack recording')
        tracker.startRecording()
        core.wait(0.1)  # Record a few samples before we actually start displaying
        tracker.sendMessage('SYNCTIME')  # Mark zero-plot time in data file

    except Exception as e:
        logging.warning(f'Error occurred in el_start: {e}')
        cleanup(tracker, win)
        raise

    finally:
        # Make sure to close the window and clean up even if an error occurred
        cleanup(tracker, win)


def cleanup(tracker, win):
    """
    Cleanup routine for Eyelink.
    """
    if tracker:
        tracker.close()
        tracker.exit()
    if win:
        win.close()
    core.quit()

