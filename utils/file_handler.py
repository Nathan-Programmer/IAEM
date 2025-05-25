# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-- [Create by Nathan/Nyogami]--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

# - Importações
import json
import os

# - Abrir o json
def loadJson(caminho):

    # -- Verifica se existe Algo no arquivo json
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # -- Se não tiver nada ele cria um
    return {}

# - Salvar coisas no json
def saveJson(caminho, dados):

    # -- Abre as identações, navegando entre elas para inserir o novo conteúdo
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= [End] =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=