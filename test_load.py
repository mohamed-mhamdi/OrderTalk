import time
from faster_whisper import WhisperModel

start = time.time()
model = WhisperModel("large-v3-turbo", device="cuda", compute_type="int8_float16")
print("Model loaded in", round(time.time() - start, 1), "seconds")