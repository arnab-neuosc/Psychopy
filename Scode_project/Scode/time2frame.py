from psychopy import visual, core
from ms2sec import ms2sec
import numpy as np


def time2frame(cfgExp, cfgScreen):
    """
    Converts time durations to frames.
    
    Args:
        cfgExp (dict): Experiment configuration containing durations in milliseconds.
        cfgScreen (dict): Screen configuration containing the inter-frame interval (ifi).

    Returns:
        dict: Updated experiment configuration with durations converted to frames.
    """

    cfgExp['ITIFrm'] = (np.round(ms2sec(cfgExp['ITIDur']) / cfgScreen['ifi'])).astype(int)  # ITI duration in frames
    cfgExp['cueFrm'] = (np.round(ms2sec(cfgExp['cueDur']) / cfgScreen['ifi'])).astype(int)  # cue duration in frames
    cfgExp['ISIFrm'] = (np.round(ms2sec(cfgExp['ISIDur']) / cfgScreen['ifi'])).astype(int)  # ISI duration in frames
    cfgExp['stimFrm'] = (np.round(ms2sec(cfgExp['stimDur']) / cfgScreen['ifi'])).astype(int)  # visual stimulus duration in frames
    cfgExp['dotFrm'] = (np.round(ms2sec(cfgExp['dotDur']) / cfgScreen['ifi'])).astype(int)  # dot duration in frames
    cfgExp['respTimOutFrm'] = (np.round(ms2sec(cfgExp['respTimOut']) / cfgScreen['ifi'])).astype(int)  # response time out duration in frames

    return cfgExp