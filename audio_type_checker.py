#this is the script to get the sample rate, sample width and number of channels of a wav file
import wave

# Open the WAV file in read-binary mode ('rb')
with wave.open('test_call.wav', 'rb') as obj:
    # Get the number of channels (1 for mono, 2 for stereo)
    channels = obj.getnchannels()
    
    # Get the sample width in bytes (e.g., 2 bytes = 16-bit audio)
    sample_width = obj.getsampwidth()
    
    # Get the sample rate (sampling frequency in Hz)
    sample_rate = obj.getframerate()
    
    print(f"Channels: {channels}")
    print(f"Sample Width: {sample_width} bytes ({sample_width * 8} bits)")
    print(f"Sample Rate: {sample_rate} Hz")
