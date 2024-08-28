#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:22:46 2024

@author: rakshita
"""
import numpy as np
import pandas as pd
import mne

raw = mne.io.read_raw_fif("test_trigger.fif")
s=raw.copy().pick(picks="stim")
channel_name = 'di32'
picks = mne.pick_channels(raw.info['ch_names'], include=[channel_name])
data, times = raw[picks, :]
df = pd.DataFrame(data.T, columns=[channel_name])
df['Time (s)'] = times

# Save the DataFrame to a CSV file
df.to_csv('channel_data.csv', index=False)
i=np.where(df[:-1] != df[1:])[0]