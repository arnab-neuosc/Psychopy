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
from pypixxlib import _libdpx as dp
#import pylink


# send_trigger(cfgTrigger, cfgExp, code, cfgEyelink, eyelinkMsg)
# Sends trigger during MEG, code should indicate trigger code you want to send
# eyelinkMsg includes the message you want to send to Eyelink as trigger

   
# Convert the decimal value to a 24-bit binary string and then to an integer
#code = 3
#doutValue = code & 0xffffff 
dp.DPxClose()

print("Opening DataPixx device...")
dp.DPxOpen()
code=240 
doutValue = code
bitMask = 0xffffff  # 24-bit mask to specify the bits being set

# Set the output value to send the trigger
dp.DPxSetDoutValue(doutValue, bitMask)
dp.DPxWriteRegCache()

# Reset the output value to zero
doutValue = int('000000000000000000000000', 2)
dp.DPxSetDoutValue(doutValue, bitMask)
dp.DPxWriteRegCache()
    
#print('Error Occured during trigger')

# Get the time point of interest
timepoint = core.getTime()



