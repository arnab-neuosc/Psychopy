# Basic Setup
import sys
sys.path.append('/home/rakshita/Scode_project_OPMLAB_15/Scode_lab_settings/Scode')
#sys.path.append('C:/Users/chbh-stim/Downloads/Scode_project/Scode')

from psychopy import visual, core, event, gui
import os
import json
import numpy as np

#from basic_setup_experiment import basic_setup_experiment
from basic_setup_experiment_opm import basic_setup_experiment
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
from send_opm_trigger_new import send_ttl_trigger


# Close all existing windows and files
#core.quit()
os.system('cls' if os.name == 'nt' else 'clear')

cfgEyelink = basic_setup_experiment()

# Input and OS folder preparations
cfgExp = prompt_input()
cfgFile = create_file_directory(cfgExp)

# Make variables and read in images
cfgExp, cfgOutput = initialise_exp_variables(cfgExp)
cfgTrigger = introduce_triggers()
cfgStim = initialise_stim_variables()
cfgScreen = initialise_screen_variables(cfgExp)


# Open a window in PsychoPy
win = visual.Window(
    size=(1024,768) if cfgExp['task'] or cfgExp['train'] else (1024, 768),  # Fullscreen if task or train, else set specific size
    screen=cfgScreen['scrNum'],  # Screen number
    color='black',  # Background color
    fullscr=cfgExp['task'] or cfgExp['train'],  # Fullscreen mode if task or train
    units='pix'  # Coordinate units, adjust as necessary
)

# Obtain the windowRect (size and position of the window)
windowRect = win.size

# Store the window and its rect in the equivalent attributes
#cfgScreen = {}
cfgScreen['window'] = win
cfgScreen['windowRect'] = windowRect


cfgStim, cfgExp, cfgTrigger = read_visual_stim(cfgFile, cfgExp, cfgStim, cfgTrigger,cfgScreen)

cfgTxt = txt_collection()

cfgScreen = basic_setup_screen(cfgScreen)
#cfgEyelink = initialise_eyelink(cfgFile, cfgEyelink, cfgScreen, cfgExp)

# Visual stimulus and fixation cross characteristics and hardware timing
cfgScreen = fix_dot_properties(cfgScreen)
cfgExp = time2frame(cfgExp, cfgScreen)
cfgStim = visual_stim_properties(cfgScreen, cfgStim)
presentingStr = make_texture_images(cfgScreen, cfgStim, cfgExp)
#cfgTrigger = initialise_trigger_port(cfgExp, cfgTrigger)
#initialize_datapixx_device()

# Main Experiment
cfgExp = KbQueue_start_routine(cfgExp)
cfgScreen['vbl'] = win.flip()
cfgOutput['vbl'] = cfgScreen['vbl']


show_instructions(cfgScreen, cfgTxt, cfgExp, presentingStr, cfgStim)

cfgOutput = draw_myText(cfgScreen, cfgExp, cfgTxt['startTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim)

nstim = -1
#blk=1

for blk in range(0, cfgExp['numBlock']):
    cfgOutput['blkStrtTmPnt'][blk] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['blkStart'], cfgEyelink, 'A')
    #blkstartmpnt=send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['blkStart'], cfgEyelink, f'block n. {blk}')
    core.wait(0.3)
    
    for trl in range(0, cfgExp['numTrial']):
        nstim += 1
        
        cfgOutput['trlStrtTmPnt'][nstim] = send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['trialStart'], cfgEyelink, 'trial start')
        #trlstartmpnt=send_ttl_trigger(cfgTrigger, cfgExp, cfgTrigger['trialStart'], cfgEyelink, 'trial start')

        # Beginning of trial fixation dot
        cfgOutput = display_fixation_dot(cfgScreen, cfgExp, nstim, 1, cfgOutput)

        # Cue presentation
        cfgOutput = display_cue(cfgScreen, presentingStr, nstim, cfgStim, cfgExp, cfgTrigger, cfgOutput, cfgEyelink)

        # ISI with fixation dot presentation
        cfgOutput = display_fixation_dot(cfgScreen, cfgExp, nstim, 0, cfgOutput)

        # Present visual stimulus with/without red flash dot
        cfgOutput = display_visual_stim(presentingStr, nstim, cfgScreen, cfgExp, cfgOutput, cfgStim, cfgTrigger, cfgEyelink)

        # Listen for a response
        cfgOutput = response_collector(cfgExp, cfgOutput, cfgTrigger, nstim, cfgTxt, cfgScreen, cfgFile, cfgEyelink, cfgStim)
        

    cfgOutput = calculate_show_feedback(cfgOutput, cfgExp, nstim, blk, cfgScreen, cfgTrigger, cfgEyelink)
    if blk != cfgExp['numBlock']:
        cfgOutput = draw_myText(cfgScreen, cfgExp, cfgTxt['breakTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim)

cfgOutput = draw_myText(cfgScreen, cfgExp, cfgTxt['endTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim)
cfgOutput = cleanup(cfgFile, cfgExp, cfgScreen, cfgEyelink, cfgOutput, cfgTrigger, cfgTxt, cfgStim)

