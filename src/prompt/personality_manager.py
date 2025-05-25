# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-- [Create by Nathan/Nyogami]--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

# - Importações
from utils.file_handler import loadJson, saveJson

class PersonalityManager:

    # -- Variáveis
    def __init__(self, botConfig_path):

        self.botConfig_path = botConfig_path
        self.botConfig = loadJson(botConfig_path)

        self.botActuallyPersonality = self.botConfig.get("personality", "")
        self.botPersonalities = self.botConfig.get("personalities", {})

    # -- Pega o prompt de cada tipo de IA criada
    def getPrompt(self):

        actuallyPersonality = self.botPersonalities.get(self.botActuallyPersonality, {})
        return actuallyPersonality.get("prompt", "")

    # -- Pega o nome de cada tipo de IA criada
    def getName(self):
        
        actuallyPersonality = self.botPersonalities.get(self.botActuallyPersonality, {})
        return actuallyPersonality.get("name", "Bot")

    # -- Troca a IA que atual
    def switch(self, newPersonality):

        # --- Verifica se existe a IA dita no json
        if newPersonality in self.botPersonalities:

            # ---- Se realmente tiver ele vai salvar como a atual
            self.botActuallyPersonality = newPersonality
            self.botConfig["personality"] = newPersonality

            saveJson(self.botConfig_path, self.botConfig)
            return True
        # --- Caso não tenha, vai retornar como falso
        return False

    # -- Pega a atual IA sendo usada
    def getActuallyPersonality(self):

        return self.botActuallyPersonality

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= [End] =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=