def introduce_triggers():

    cfgTrigger = {
        'off': 0,
        'cueRight': 1,       # Start of attention orientation
        'cueLeft': 2,        # Start of attention orientation
        'trialStart': 3,
        'stimOnset': 4,      # Onset of moving gratings - end of attention orientation
        'catchOnset': 5,     # Onset of catch trial
        'dotOnRight': 6,
        'dotOnLeft': 7,
        'resp': 8,           # Button press
        'blkStart': 20,      
        'blkEnd': 21,        
        'expEnd': 30,        
        'abort': 31
    }

    return cfgTrigger
