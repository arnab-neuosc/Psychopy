from psychopy import parallel

def initialise_trigger_port(cfgExp, cfgTrigger):
    # cfgTrigger = initialise_trigger_port(cfgExp, cfgTrigger)
    # initiates sending triggers to MEG PC and puts everything in cfgTrigger

    cfgTrigger['address'] = None

    if cfgExp['EEGLab'] == 1:
        cfgTrigger['address'] = 0x378  # port address (same as hex2dec('378') in MATLAB)
        try:
            # Set the port address
            port = parallel.ParallelPort(address=cfgTrigger['address'])
            # Reset the trigger by sending a 0 to the port
            port.setData(0)
            cfgTrigger['status'] = "Port initialized successfully"
        except Exception as e:
            cfgTrigger['status'] = f"Error initializing port: {str(e)}"

    return cfgTrigger

