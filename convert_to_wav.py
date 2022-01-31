# Import necessary libraries
import pandas as pd
import numpy as np
import os
import subprocess
from pathlib import Path

# load metadata
folder = 'coughvid-19/'
filepath= folder + "metadata_compiled.csv"
df = pd.read_csv(filepath)

#### convert files to .wav ####
# select files with recommended "cough_detected" value
df = df[df['cough_detected']>=0.8]
names = df.uuid.to_numpy()
write_folder = 'wav_recordings'

# check if directory for wavs already created
if os.path.isdir(write_folder):
    print(f"dir: '{write_folder}' exists")
else:
    os.mkdir('wav_recordings')
    print(f"Created dir: {write_folder}")

# convert files left in df to .wav
n_files = len(names)
for i, name in enumerate(names):
    print(f"File {i+1} of {n_files}...")
    if os.path.isfile(folder + name + '.webm'):
        # use ffmpeg to convert .webm to .wav
        subprocess.call(["ffmpeg", "-i", folder+name+".webm", write_folder+"/"+name+".wav"])
    elif os.path.isfile(folder + name + '.ogg'):
        # use ffmpeg to convert .ogg to .wav
        subprocess.call(["ffmpeg", "-i", folder+name+".ogg", write_folder+"/"+name+".wav"])
    else:
        print(f"Error. Filename: {name +'.webm'}")