from pydub import AudioSegment
from pydub.effects import speedup
from pydub.silence import split_on_silence
import subprocess

filepath = "Consultation transcript\\Data\\Audio Recordings\\CAR0001.mp3"

def remove_silence(input__file, output_file, sil_len = 500, sil_thresh = -30): #threshold may need calibrating based on doctor's recording set up

    audio = AudioSegment.from_mp3(input__file)

    #keeps 500ms of silence 
    chunks = split_on_silence(audio, min_silence_len = sil_len, silence_thresh = sil_thresh, keep_silence=500)

    output = AudioSegment.empty()
    for chunk in chunks:
        output += chunk
    
    # speed up with a factor of 1.2x
    new_file = speedup(output, 1.2, 150)

    new_file.export(output_file, format="mp3")


remove_silence(filepath, "CAR0001_sil_removed_120.mp3" )

