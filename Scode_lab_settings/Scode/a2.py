# Basic Setup
import sys
#sys.path.append('/home/rakshita/Scode_project/Scode')
sys.path.append('C:/Users/chbh-stim/Downloads/Scode_project/Scode')

from psychopy import visual, core, event, gui
import os
import json
import numpy as np

from basic_setup_experiment import basic_setup_experiment
from create_file_directory import create_file_directory
from prompt_input import prompt_input
from initialise_exp_variables import initialise_exp_variables
from introduce_triggers import introduce_triggers
from initialise_stim_variables import initialise_stim_variables
from read_visual_stim import read_visual_stim
from initialise_screen_variables1 import initialise_screen_variables
from basic_setup_screen import basic_setup_screen
from txt_collection import txt_collection
from fix_dot_properties import fix_dot_properties
from time2frame import time2frame
from visual_stim_properties import visual_stim_properties
from make_texture_images import make_texture_images
from initialise_trigger_port import initialise_trigger_port
from KbQueue_start_routine import KbQueue_start_routine
from showInstructions import show_instructions
from draw_myText import draw_myText
from display_fixation_dot import display_fixation_dot
from display_visual_stim import display_visual_stim
from response_collector import response_collector
from display_cue import display_cue
from calculate_show_feedback import calculate_show_feedback
from cleanup import cleanup
from send_trigger2 import send_trigger
from initialise_eyelink import initialise_eyelink
from setup_datapixx import setup_datapixx
from setup_datapixx2 import initialize_datapixx_device
from send_opm_trigger import send_ttl_trigger

# Close all existing windows and files
#core.quit()
os.system('cls' if os.name == 'nt' else 'clear')

cfgEyelink = basic_setup_experiment()


def basic_setup_experiment():

    # Basic setup
    cfgEyelink = {}

    # Check if the user wants to skip the sync test
    inp1 = input('Do you want to skip sync test? y/n').strip().lower()
    if inp1 == 'y':
        skipSync = True
        logging.warning('Sync test is skipped! Do not continue if it is an actual recording!')
        m = input('Do you want to continue? y/n   ').strip().lower()
        while True:
            if m == 'y':
                break
            elif m == 'n':
                raise Exception('The experiment aborted by operator.')
    else:
        skipSync = False

    # Set preference for skipping sync tests
    prefs.hardware['audioLib'] = ['pyo']  # Ensures audio library is set
    prefs.general['winType'] = 'pyglet'
    if skipSync:
        logging.warning('Sync test is being skipped')
        prefs.general['skipSync'] = True
    else:
        prefs.general['skipSync'] = False

    dummy = time.time()

    # Check if the user wants to use Eyelink
    inp3 = input('Do you want to use Eyelink? y/n').strip().lower()
    if inp3 == 'y':
        cfgEyelink['on'] = True
    else:
        logging.warning('Eyelink is off! Do not continue if it is an actual recording!')
        m = input('Do you want to continue? y/n').strip().lower()
        while True:
            if m == 'y':
                cfgEyelink['on'] = False
                break
            elif m == 'n':
                raise Exception('The experiment aborted by operator.')

    return cfgEyelink

