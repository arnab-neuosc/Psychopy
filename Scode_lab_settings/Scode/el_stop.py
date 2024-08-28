from psychopy import core, logging
import os
import shutil
import pylink

def el_stop(cfgFile, el):
    """
    Stop recording eye movements, save, close graphics window, close data file, and shut down tracker.
    
    Parameters:
    cfgFile (dict): Configuration related to files and directories.
    el (pylink.EyeLink): The EyeLink object.
    """
    try:
        # Stop recording
        el.stopRecording()
        
        # Close data file
        el.closeDataFile()
        
        # Download data file
        print(f"Receiving data file '{cfgFile['eyelink']}'")
        el.receiveDataFile(cfgFile['eyelink'], os.path.join(cfgFile['subDir'], cfgFile['eyelink']))

        # Copy and rename the eyelink file according to BIDS
        source_path = os.path.join(cfgFile['subDir'], cfgFile['eyelink'])
        target_path = os.path.join(cfgFile['subDir'], f"{cfgFile['BIDSname']}{cfgFile['edfFile']}")
        
        if os.path.exists(source_path):
            copy_status = shutil.copyfile(source_path, source_path)
            move_status = shutil.move(source_path, target_path)
            print(f"ReceiveFile status 1 & {copy_status} & {move_status}")

    except RuntimeError as e:
        logging.error(f"Error stopping Eyelink: {str(e)}")
    
    # Cleanup routine
    cleanup(el)

def cleanup(el):
    """
    Cleanup routine to shutdown Eyelink and close PsychoPy window.
    
    Parameters:
    el (pylink.EyeLink): The EyeLink object.
    """
    try:
        el.close()
        el.shutdown()
        core.quit()
    except RuntimeError as e:
        logging.error(f"Error during cleanup: {str(e)}")


