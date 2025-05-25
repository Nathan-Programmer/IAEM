import requests
import re

def generateResponse(model, prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False 
        }
    )

    if response.status_code != 200:
        return "[Erro na resposta da IA]"
    
    try:

        data = response.json()
        text = data.get("response", "")

        textCompleted = re.split(r"\n(User|Bot):", text)[0].strip()
        return textCompleted
    
    except Exception:

        return "[Erro ao processar resposta]"
