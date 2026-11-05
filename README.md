# OrderTalk

AI sales agent for online shops: it answers customer messages (Messenger, Instagram) and phone calls, checks the catalog and stock, and takes confirmed orders.

## Status

Early prototype. The scripts below are the first experiments, built on a fake restaurant ("Chez Test").

| File | What it does |
|---|---|
| `test_load.py` | Loads the Whisper speech-to-text model on the GPU and times it |
| `test_mic.py` | Records 5 s from the microphone and transcribes it (French) |
| `test_llm.py` | Lists the models available on Groq |
| `test_chat.py` | Terminal chat: type a customer sentence, get the agent's answer and its latency |

## Stack

- Speech-to-text: [faster-whisper](https://github.com/SYSTRAN/faster-whisper), model `large-v3-turbo`, on CUDA
- LLM: Groq API (`openai/gpt-oss-120b`) through the OpenAI-compatible client

## Setup (Windows, PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env          # then put your Groq key in .env
python test_chat.py
```

## Roadmap

1. Agent brain: product database, tool calling, confirmed orders
2. Backend (FastAPI) that receives messages
3. Instagram and Messenger integration
4. Shop owner dashboard
5. Multi-shop product and deployment
6. Pilot with real shops
7. Phone calls (STT, TTS, telephony)
