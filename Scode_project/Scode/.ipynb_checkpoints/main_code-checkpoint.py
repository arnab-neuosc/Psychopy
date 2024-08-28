# Basic Setup
from psychopy import visual, core, event, gui
import os
import json
import numpy as np
from angle2pix import *

import basic_setup_experiment
import create_file_directory
import prompt_input
import initialise_exp_variables
import introduce_triggers
import initialise_stim_variables
import read_visual_stim
import initialise_screen_variables
import basic_setup_experiment
import txt_collection
import basic_setup_screen
import fix_dot_properties
import time2frame
import visual_stim_properties
import make_texture_images
import initialise_trigger_port
import KbQueue_start_routine
import showInstructions
import draw_myText
import display_fixation_dot
import display_visual_stim
import response_collector
import display_cue
import calculate_show_feedback
import cleanup
import send_trigger
import initialise_eyelink

# Close all existing windows and files
core.quit()
os.system('cls' if os.name == 'nt' else 'clear')

# Function Definitions (Assume these are provided)
# basic_setup_experiment, prompt_input, create_file_directory, initialise_exp_variables
# introduce_triggers, initialise_stim_variables, read_visual_stim, initialise_screen_variables
# txt_collection, basic_setup_screen, initialise_eyelink, fix_dot_properties
# time2frame, visual_stim_properties, make_texture_images, initialise_trigger_port
# KbQueue_start_routine, showInstructions, draw_myText, send_trigger, display_fixation_dot
# display_cue, display_visual_stim, response_collector, calculate_show_feedback, cleanup

# Basic PTB setup and clearing up
cfgEyelink = basic_setup_experiment()

# Input and OS folder preparations
cfgExp = prompt_input()
cfgFile = create_file_directory(cfgExp)

# Make variables and read in images
cfgExp, cfgOutput = initialise_exp_variables(cfgExp)
cfgTrigger = introduce_triggers()
cfgStim = initialise_stim_variables()
cfgStim, cfgExp, cfgTrigger = read_visual_stim(cfgFile, cfgExp, cfgStim, cfgTrigger)
cfgScreen = initialise_screen_variables(cfgExp)
cfgTxt = txt_collection()

# Screen Setup
win = visual.Window(size=[800, 600], color=[-1, -1, -1], fullscr=True)
cfgScreen['window'] = win
cfgScreen = basic_setup_screen(cfgScreen)
cfgEyelink = initialise_eyelink(cfgFile, cfgEyelink, cfgScreen, cfgExp)

# Visual stimulus and fixation cross characteristics and hardware timing
cfgScreen = fix_dot_properties(cfgScreen)
cfgExp = time2frame(cfgExp, cfgScreen)
cfgStim = visual_stim_properties(cfgScreen, cfgStim)
presentingStr = make_texture_images(cfgScreen, cfgStim, cfgExp)
cfgTrigger = initialise_trigger_port(cfgExp, cfgTrigger)

# Main Experiment
cfgExp = KbQueue_start_routine(cfgExp)
cfgScreen['vbl'] = win.flip()
cfgOutput['vbl'] = cfgScreen['vbl']
showInstructions(cfgScreen, cfgTxt, cfgExp, presentingStr, cfgStim)
cfgOutput = draw_myText(cfgScreen, cfgExp, cfgTxt['startTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgEyelink, cfgStim)

nstim = 0

for blk in range(1, cfgExp['numBlock'] + 1):
    cfgOutput['blkStrtTmPnt'][blk] = send_trigger(cfgTrigger, cfgExp, cfgTrigger['blkStart'], cfgEyelink, f'block n. {blk}')
    core.wait(0.003)
    
    for trl in range(1, cfgExp['numTrial'] + 1):
        nstim += 1
        #cfgOutput['trlStrtTmPnt'][nstim] = send_trigger(cfgTrigger, cfgExp, cfgTrigger['trialStart'], cfgEyelink, 'trial start')

        # Beginning of trial fixation dot
        cfgOutput = display_fixation_dot(cfgScreen, cfgExp, nstim, 1, cfgOutput)

        # Cue presentation
        cfgOutput = display_cue(presentingStr, nstim, cfgStim, cfgScreen, cfgExp, cfgTrigger, cfgOutput, cfgEyelink)

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

