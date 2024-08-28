# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard


# Run 'Before Experiment' code from VPIXX_init
from pypixxlib import _libdpx as dp
from pypixxlib import responsepixx as rp
import csv
import numpy as np

def initialize_datapixx_device():
    """
    Initializes the DataPixx device by opening the connection, checking readiness,
    stopping all schedules, and writing the register cache.
    Raises a ConnectionError if the VPixx hardware is not detected.
    """
    from pypixxlib import _libdpx as dp
    
    # Close any existing DataPixx connection
    dp.DPxClose()

    # Initialize DataPixx
    print("Opening DataPixx device...")
    dp.DPxOpen()
    
    # Check if DataPixx is ready
    isReady = dp.DPxIsReady()
    if not isReady:
        raise ConnectionError('VPixx Hardware not detected! Check your connection and try again.')
    
    # Stop all existing schedules and write the register cache
    dp.DPxStopAllScheds()
    dp.DPxWriteRegCache()

    print("DataPixx device initialized and ready.")





	

