import asyncio
import json
import time
import wave
import websockets

HOST = "localhost"
PORT = 8765
CHUNK_DURATION_MS = 250


async def stream_wav_file(websocket, file_path: str):
    print(f"[Audio Streamer] Opening: {file_path}")
    try:
        wf = wave.open(file_path, "rb")
    except Exception as e:
        await websocket.send(
            json.dumps({"event": "error", "message": f"WAV open error: {str(e)}"})
        )
        return

    sample_rate = wf.getframerate()
    frames_per_chunk = int(sample_rate * (CHUNK_DURATION_MS / 1000.0))

    await websocket.send(
        json.dumps(
            {
                "event": "start",
                "sample_rate": sample_rate,
                "chunk_duration_ms": CHUNK_DURATION_MS,
            }
        )
    )

    chunk_index = 0
    start_time = time.time()

    while True:
        chunk_start = time.time()
        pcm_bytes = wf.readframes(frames_per_chunk)
        if not pcm_bytes:
            break

        emission_time_ms = int(time.time() * 1000)

        # Send raw binary audio chunk
        await websocket.send(pcm_bytes)

        # Send timestamp metadata for latency benchmarking
        await websocket.send(
            json.dumps(
                {
                    "event": "chunk_meta",
                    "chunk_index": chunk_index,
                    "emission_timestamp_ms": emission_time_ms,
                    "audio_offset_ms": chunk_index * CHUNK_DURATION_MS,
                }
            )
        )

        chunk_index += 1

        # Real-time 1x rate enforcement
        elapsed = time.time() - chunk_start
        sleep_time = (CHUNK_DURATION_MS / 1000.0) - elapsed
        if sleep_time > 0:
            await asyncio.sleep(sleep_time)

    wf.close()
    await websocket.send(
        json.dumps(
            {
                "event": "stop",
                "total_chunks": chunk_index,
                "duration_s": round(time.time() - start_time, 2),
            }
        )
    )
    print("[Audio Streamer] Audio stream complete.")


async def handler(websocket):
    try:
        async for message in websocket:
            data = json.loads(message)
            if data.get("action") == "start_stream":
                await stream_wav_file(
                    websocket, data.get("file_path", "test_call.wav")
                )
    except websockets.exceptions.ConnectionClosed:
        pass


async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"[Audio Streamer] Active on ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())