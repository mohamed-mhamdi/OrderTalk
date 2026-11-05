import time
import sounddevice as sd
import os, sys

for lib in ("cublas", "cudnn"):
    dll_dir = os.path.join(sys.prefix, "Lib", "site-packages", "nvidia", lib, "bin")
    os.add_dll_directory(dll_dir)
    os.environ["PATH"] = dll_dir + os.pathsep + os.environ["PATH"]
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000   # Whisper expects 16 kHz audio
SECONDS = 5

model = WhisperModel("large-v3-turbo", device="cuda", compute_type="int8_float16")

print("Speak in French for 5 seconds after pressing Enter...")
input()
audio = sd.rec(int(SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
sd.wait()
audio = audio.flatten()   # (N, 1) -> (N,)

start = time.time()
segments, info = model.transcribe(audio, language="fr", beam_size=1)
text = " ".join(s.text.strip() for s in segments)
print("Text:", text)
print("Transcription took", round(time.time() - start, 2), "seconds")