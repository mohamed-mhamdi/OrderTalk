import os, time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from the .env file

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-120b"

SYSTEM = """Tu es l'assistant téléphonique du restaurant "Chez Test".
Réponds en français, en une ou deux phrases courtes.

Informations du restaurant :
- Horaires : tous les jours de 12h à 15h et de 19h à 23h, fermé le lundi.
- Menu : pizza margherita 12 DT, pizza 4 fromages 15 DT, salade César 10 DT, tiramisu 7 DT.

Règles :
- Utilise UNIQUEMENT les informations ci-dessus.
- Si tu ne connais pas la réponse, dis que tu vas demander à un responsable.
- N'invente jamais un prix, un horaire ou un plat.
"""

print("Écris une phrase de client (ligne vide pour quitter).")
while True:
    question = input("Client : ").strip()
    if not question:
        break
    start = time.time()
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": question},
        ],
    )
    print("Agent :", resp.choices[0].message.content)
    print("(", round(time.time() - start, 2), "s )")