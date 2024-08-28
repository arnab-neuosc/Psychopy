import pylink
import logging

def el_set_parameters(tracker, cfgScreen, cfgExp):
    """
    Set custom parameters for Eyelink.
    """
    try:
        # Set global variables for Eyelink
        el = tracker.getDefaults()
        el['calibrationtargetsize'] = 1
        el['calibrationtargetwidth'] = 0.5
        el['targetbeep'] = 0
        el['feedbackbeep'] = 0
        el['displayCalResults'] = 1
        el['eyeimagesize'] = 50  # percentage of screen
        el['cameraDistance'] = 50  # distance between participant and camera in cm
        el['backgroundcolour'] = cfgScreen['backgroundColor']  # set the Eyelink background color
        el['foregroundcolour'] = 255  # set the text/fixation cross color of Eyelink
        el['imgtitlecolour'] = 255
        el['calibrationtargetcolour'] = [255, 255, 255]
        el['msgfontcolour'] = 255

        # Update Eyelink defaults
        logging.info('Updating Parameters')
        tracker.setDefaults(el)

        # Make sure we're still connected
        if not tracker.isConnected():
            logging.warning('Eyelink is not connected! Restart the tracker.')
            cleanup(tracker)
            return

        # Configure screen pixel coordinates
        num_pix_smaller_than_fullScrn = 100
        screen_coords = (cfgScreen['fullScrn'][0] - num_pix_smaller_than_fullScrn,
                         cfgScreen['fullScrn'][1] - num_pix_smaller_than_fullScrn,
                         cfgScreen['fullScrn'][2] + num_pix_smaller_than_fullScrn,
                         cfgScreen['fullScrn'][3] + num_pix_smaller_than_fullScrn)
        tracker.sendMessage(f'SCREEN_COORDS {screen_coords[0]} {screen_coords[1]} {screen_coords[2]} {screen_coords[3]}')

        # Enable binocular tracking
        tracker.sendCommand('binocular_enabled = YES')
        cfgEyelink['eyeUsed'] = 'BOTH'

        # Configure other settings
        tracker.sendCommand('recording_parse_type = GAZE')
        tracker.sendCommand('saccade_velocity_threshold = 22')
        tracker.sendCommand('saccade_acceleration_threshold = 3800')
        tracker.sendCommand('saccade_motion_threshold = 0.0')
        tracker.sendCommand('saccade_pursuit_fixup = 60')
        tracker.sendCommand('fixation_update_interval = 0')
        tracker.sendCommand('calibration_type = HV9')
        tracker.sendCommand('generate_default_targets = YES')
        tracker.sendCommand('enable_automatic_calibration = YES')
        tracker.sendCommand('automatic_calibration_pacing = 1000')
        tracker.sendCommand('use_ellipse_fitter = NO')
        tracker.sendCommand('sample_rate = 1000')
        tracker.sendCommand('elcl_tt_power = 2')  # Illumination, 1 = 100%, 2 = 75%, 3 = 50%

        # Set eye-specific settings
        if cfgEyelink['eyeUsed'] == 'RIGHT_EYE':
            tracker.sendCommand('file_event_filter = RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')
            tracker.sendCommand('link_event_filter = RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')
        elif cfgEyelink['eyeUsed'] == 'LEFT_EYE':
            tracker.sendCommand('file_event_filter = LEFT,FIXATION,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')
            tracker.sendCommand('link_event_filter = LEFT,FIXATION,FIXUPDATE,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')
        elif cfgEyelink['eyeUsed'] == 'BOTH':
            tracker.sendCommand('file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')
            tracker.sendCommand('link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,MESSAGE,INPUT,BUTTON')

        # Ensure we get gaze data
        tracker.sendCommand('file_sample_data = LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT')
        tracker.sendCommand('link_sample_data = LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT')

        # Other settings
        tracker.sendCommand('heuristic_filter = 0')
        tracker.sendCommand('pupil_size_diameter = YES')

        # Send physical parameters to the EDF file
        tracker.sendMessage(f'Calibration_area: {cfgScreen["fullScrn"]}')
        tracker.sendMessage(f'Screen_size_mm: {cfgScreen["dispSize"]["height"]} {cfgScreen["dispSize"]["width"]}')
        tracker.sendMessage(f'Screen_distance_mm: {cfgScreen["distance"] * 10}')
        tracker.sendMessage(f'Camera_position_mm: {cfgEyelink["defaults"]["cameraDistance"] * 10}')

    except Exception as e:
        logging.warning(f'Error occurred in el_set_parameters: {e}')
        cleanup(tracker)
        raise

def cleanup(tracker):
    """
    Cleanup routine for Eyelink.
    """
    if tracker:
        tracker.close()
        tracker.exit()
    logging.info('Eyelink connection closed.')

