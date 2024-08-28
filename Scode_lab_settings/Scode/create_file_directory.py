import os


def create_file_directory(cfgExp):
    # Move to the current directory
    curr_dir = os.getcwd()
    os.chdir(curr_dir)
    os.chdir('..')  # Move up one folder

    # Add sub-directories to the system path
    os.sys.path.append(os.path.join(os.getcwd(), 'Experiment_Functions'))
    os.sys.path.append(os.path.join(os.getcwd(), 'Eyelink'))
    os.sys.path.append(os.path.join(os.getcwd(), 'Stimuli'))
    os.sys.path.append(os.path.join(os.getcwd(), 'Results'))

    cfgFile = {}
    if cfgExp['pc'] == 'OPM' or cfgExp['pc'] == 'MEG':
        cfgFile['res'] = os.path.join(curr_dir, 'Results')
        cfgFile['stim'] = os.path.join(os.getcwd(), 'Stimuli', 'Visual_Stimuli')
        cfgFile['cue'] = os.path.join(os.getcwd(), 'Stimuli', 'Cue_Stimuli')

    # Create result directory with BIDS format
    sub_dir = os.path.join(cfgFile['res'], f"sub-{cfgExp['sub']}", f"ses-{cfgExp['ses']}", 'OPM')
    os.makedirs(sub_dir, exist_ok=True)
    cfgFile['subDir'] = sub_dir  # Store subject directory address

    # BIDS specific file name
    if cfgExp['test'] == 'train':
        cfgFile['BIDSname'] = f"sub-{cfgExp['sub']}_ses-{cfgExp['ses']}_train-{cfgExp['task']}_run-{cfgExp['run']}"
    else:
        cfgFile['BIDSname'] = f"sub-{cfgExp['sub']}_ses-{cfgExp['ses']}_task-{cfgExp['task']}_run-{cfgExp['run']}"

    cfgFile['edfFile'] = '_eyetracking.edf'  # Eyetracking file name
    cfgFile['logFile'] = '_logfile.pkl'  # Log file name (using pickle format for Python)
    cfgFile['eyelink'] = f"e{cfgExp['run']}{cfgExp['sub']}"  # File name to use on Eyelink PC

    # Move back to the experiment functions directory for necessary files
    os.chdir(curr_dir)

    return cfgFile



