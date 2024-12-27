import os
import requests
from transformers import pipeline
import torch
import runpod

# Detect device (CPU or GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=device)

def handler(event):
    try:
        # Get the S3 pre-signed URL from the input
        file_url = event.get("input", {}).get("file_url")
        if not file_url:
            return {"error": "File URL not provided."}

        # Download the file from the URL
        local_file_path = "/tmp/audio.wav"  # Temporary storage path
        response = requests.get(file_url, stream=True)
        if response.status_code != 200:
            return {"error": "Failed to download the file from the URL."}

        with open(local_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Transcribe the audio
        transcription = transcriber(local_file_path)

        # Return the transcription result
        return {"transcription": transcription["text"]}

    except Exception as e:
        return {"error": str(e)}

# Start the RunPod serverless handler
if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
