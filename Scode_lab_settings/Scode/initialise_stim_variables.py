def initialise_stim_variables():

    cfgStim = {
        'stimRotSpeed': 2,  # number of 360-degree rotations per second
        'destRectH': 7,  # height of destination rectangle for stimulus in visual degrees
        'destRectW': 7,  # width of destination rectangle for stimulus in visual degrees
        'destRectCueSize': 3,  # size of destination rectangle for cue
        'visStimToR': [5, 1, 5, 1],  # visual degrees from center for stimulus on the right
        'visStimToL': [5, -1, 5, -1],  # visual degrees from center for stimulus on the left
        'cueToB': [0, 2, 0, 2]  # visual degrees from center for cue below
    }

    return cfgStim

