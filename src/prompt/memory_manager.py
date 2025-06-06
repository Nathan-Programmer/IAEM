# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-- [Create by Nathan/Nyogami]--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

# - Importações
from utils.file_handler import loadJson, saveJson

class MemoryManager:

    # -- Variáveis
    def __init__(self, path, personality):
        self.path = path
        self.personality = personality.lower()
        self.data = loadJson(path)

        # --- Garantir que a estrutura básica exista
        if "important_memory" not in self.data:
            self.data["important_memory"] = {}
        if "vague_memory" not in self.data:
            self.data["vague_memory"] = {}

        # --- Gatantir que sempre terá a personalidade da IA 
        for key in ["important_memory", "vague_memory"]:
            if self.personality not in self.data[key]:
                self.data[key][self.personality] = []

    # -- Retorna apenas a memória vaga (usada na construção do prompt)
    def getVagueMemory(self):
        return self.data["vague_memory"][self.personality]

    # -- Verifica se é importante essa memória ou não
    def addEntry(self, user_mensage, bot_mensage):
        
        if not user_mensage.strip() and not bot_mensage.strip():
            return
        
        # --- Empacota as duas mensagens para ser salva na memória
        entry = {"User": user_mensage, "Bot": bot_mensage}

        if "#importante" in user_mensage.lower() or "#importante" in bot_mensage.lower():
            self.data["important_memory"][self.personality].append(entry)
        else:
            self.data["vague_memory"][self.personality].append(entry)

        self.saveMemory()

    # -- Salva a memória
    def saveMemory(self):
        saveJson(self.path, self.data)

    def promoteVagueToImportant(self, criterio_func):
        vagas = self.data["vague_memory"][self.personality]
        importantes = self.data["important_memory"][self.personality]
        
        novas_vagas = []
        
        for entry in vagas:
            if criterio_func(entry):
                importantes.append(entry)
            else:
                novas_vagas.append(entry)
        
        self.data["vague_memory"][self.personality] = novas_vagas
        self.data["important_memory"][self.personality] = importantes
        
        self.saveMemory()

    # -- Deleta a memória que não é importante
    def clearVagueMemory(self):
        self.data["vague_memory"][self.personality] = []
        self.saveMemory()

    # -- Deleta a memória que é importante
    def clearImportantMemory(self):
        self.data["important_memory"][self.personality] = []
        self.saveMemory()

    # -- Seta a nova personalidade caso tenha mudada, na memória
    def setPersonality(self, new_personality):
        new_personality = new_personality.lower()
        if new_personality != self.personality:
            self.personality = new_personality

            # Garantir que a nova personalidade exista na estrutura
            for key in ["important_memory", "vague_memory"]:
                if self.personality not in self.data[key]:
                    self.data[key][self.personality] = []
            
            # Salvar memória atualizada para garantir consistência
            self.saveMemory()

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= [End] =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=