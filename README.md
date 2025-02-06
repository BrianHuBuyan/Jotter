# Jotter
A prototype for an AI tool converting patient-doctor consultation audio to diarised transcripts and notes.

## Pipelines
Two versions of the program was made:
1. Using AWS transcribe health, S3 and OpenAi's chatgpt.

    Files were passed into transcribe health via S3, generating diarised transcripts that had notes generated using chatgpt api calls.
2. Using OpenAI Whisper and chatgpt with pyannote

    Whisper offered cheaper fees per request and more accurate transcriptions. However it lacked diarisation so pyannote was used to mitigate this.

### Helper functions
Pydub was used to create an audio processor program that truncated audio files, removing long silences and increasing playback speed to minimise cost incurred by api calls.

Tscribe was used to parse AWS transcribe responses

### Test data
Audio files and transcripts used for testing the programs were obtained from: \
Smith, Christopher William; Fareez, Faiha; Parikh, Tishya; Wavell, Christopher; Shahab, Saba; Chevalier, Meghan; et al. (2022). Collection of simulated medical exams. figshare. Dataset. https://doi.org/10.6084/m9.figshare.16550013.v1