import requests
import re

def generateResponse(model, prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False 
            },
            timeout=120  # Timeout aumentado para 120 segundos
        )
        
        if response.status_code != 200:
            print(f"[ERRO] Código de status: {response.status_code}")
            return "[Erro na resposta da IA]"
        
        data = response.json()
        text = data.get("response", "")

        textCompleted = re.split(r"\n(User|Bot):", text)[0].strip()
        return textCompleted
    
    except requests.exceptions.ReadTimeout:
        print("[EXCEÇÃO] Tempo limite de resposta excedido (timeout).")
        return "[Desculpe, estou demorando para responder. Tente novamente mais tarde.]"

    except Exception as e:
        print(f"[EXCEÇÃO] {e}")
        return "[Erro ao processar resposta]"
