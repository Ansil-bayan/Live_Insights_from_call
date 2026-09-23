# Live Insights from Call

This repository contains a real‑time audio streaming and analysis pipeline built with Python. It includes:

- **Audio streaming server** (`audio_streamer.py`) that streams a WAV file over a WebSocket connection.
- **Pipeline runner** (`pipeline_runner.py`) that receives the audio, performs on‑device speech‑to‑text using Faster‑Whisper, extracts business‑relevant signals with a custom `SignalEngine`, and dispatches nudges via `NudgeController`.
- **Utility scripts** for audio conversion (`16k_converter.py`) and format checking (`audio_type_checker.py`).
- **Example client** (`test_receiver.py`) that demonstrates how to consume the streamed transcript.

## DEMO VIDEO



[![Watch the Video](https://github.com/user-attachments/assets/5bb998c4-9470-4a49-b90d-b4ba083f9fa8)]([JAM_VIDEO_URL](https://jam.dev/c/4cefdf5b-42af-431d-95f6-9f8af258c88a))

## Project Structure

```
Live Insights from Call/
├─ audio_streamer.py        # WebSocket audio server
├─ pipeline_runner.py       # Real‑time ASR + signal processing
├─ signal_engine.py         # Rule‑based signal detection
├─ nudge_controller.py      # Nudge throttling & prioritisation
├─ 16k_converter.py         # Convert audio to 16 kHz mono WAV
├─ audio_type_checker.py    # Print WAV metadata
├─ test_receiver.py         # Example client for the pipeline
├─ test_call.wav            # Sample audio file
└─ README.md                # Project documentation (this file)
```

## Getting Started

1. **Install dependencies** (see `requirements.txt`).
2. Ensure you have a recent version of Python (3.10+ recommended).
3. Run the audio streamer:
   ```bash
   python audio_streamer.py
   ```
4. In another terminal, start the pipeline runner:
   ```bash
   python pipeline_runner.py
   ```
   The runner will connect to the streamer, perform transcription, detect signals, and print nudges.

## License

This project is provided under the MIT License. Feel free to modify and extend it for your own use cases.
