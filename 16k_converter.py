import soundfile as sf

# 1. Load your original audio file (works with .wav, .flac, .ogg, etc.)
# If you have an MP3, change the filename here accordingly
input_file = "test_call.mp3" 
output_file = "output_16k_mono_16bit.wav"

data, samplerate = sf.read(input_file)

# 2. Convert to Mono if the file is Stereo
if len(data.shape) > 1:
    # Average the channels to create a mono track
    data = data.mean(axis=1)

# 3. Save as 16kHz, 16-bit PCM WAV
# soundfile automatically handles the sample rate conversion during write if specified
sf.write(output_file, data, 16000, subtype='PCM_16')

print(f"Successfully converted and saved as {output_file}")


