# import os
# import pickle
# from psychopy import core, logging
# import el_stop
# from send_opm_trigger import send_ttl_trigger

# def cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim):

#     cfgOutput['endTmPnt'] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['expEnd'], cfgEyelink, 'end of experiment')

#     # Check if the log file is being overwritten
#     log_file_path = os.path.join(cfgFile['subDir'], cfgFile['BIDSname'], cfgFile['logFile'])
#     if os.path.exists(log_file_path):
#         logging.warning('Log file will be overwritten!')
#         cont = input('Do you want to continue? (y/n) ').strip().lower()
#         while True:
#             if cont == 'y':
#                 break
#             elif cont == 'n':
#                 raise Exception('The experiment aborted by operator.')

#     # Save the log file
#     try:
#         with open(log_file_path, 'wb') as file:
#             pickle.dump(cfgOutput, file)
#     except Exception as e:
#         logging.warning(f'Saving the log files failed: {e}')

#     # Stop Eyelink if it is on
#     try:
#         if cfgEyelink['on']:
#             el_stop(cfgFile)
#     except Exception as e:
#         logging.warning(f'Stopping the Eyelink failed: {e}')

#     # Close the window and clean up
#     cfgScreen['window'].close()
#     #core.quit()

#     return cfgOutput




import os
import pickle
from psychopy import core, logging
import el_stop
from send_opm_trigger import send_ttl_trigger

def cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim):

    cfgOutput['endTmPnt'] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['expEnd'], cfgEyelink, 'end of experiment')

    # Determine log file path
    log_file_path = os.path.join(cfgFile['subDir'], cfgFile['BIDSname'], cfgFile['logFile'])
    
    # Check if the directory exists, create if it does not
    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
            logging.info(f'Created directory for log file at {log_dir}')
        except Exception as e:
            logging.warning(f'Creating directory failed: {e}')
            raise

    # Check if the log file is being overwritten
    if os.path.exists(log_file_path):
        logging.warning('Log file will be overwritten!')
        cont = input('Do you want to continue? (y/n) ').strip().lower()
        while True:
            if cont == 'y':
                break
            elif cont == 'n':
                raise Exception('The experiment aborted by operator.')
            else:
                cont = input('Invalid input. Do you want to continue? (y/n) ').strip().lower()

    # Save the log file
    try:
        with open(log_file_path, 'wb') as file:
            pickle.dump(cfgOutput, file)
    except Exception as e:
        logging.warning(f'Saving the log file failed: {e}')

    # Stop Eyelink if it is on
    try:
        if cfgEyelink['on']:
            el_stop(cfgFile)
    except Exception as e:
        logging.warning(f'Stopping the Eyelink failed: {e}')

    # Close the window and clean up
    cfgScreen['window'].close()
    # core.quit()

    return cfgOutput
