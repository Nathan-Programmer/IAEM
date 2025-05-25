import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.json')

def carregar_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
