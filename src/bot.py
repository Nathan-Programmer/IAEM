# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-- [Create by Nathan/Nyogami]--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

# --- Importações
from .prompt.personality_manager import PersonalityManager
from .configs.ollama_api import generateResponse
from .prompt.prompt_builder import constructPrompt
from .prompt.memory_manager import MemoryManager
from .interface.gui_interface import ChatGUI
from utils.file_handler import loadJson
from os import path

# --- Caminho dos arquivos json

botConfig_path = path.join("jsonFiles/config.json")
botMemory_path = path.join("jsonFiles/memory.json")

class Bot:
    # -- Criação das variáveis para as funções
    
    def __init__(self):

        self.botConfig = loadJson(botConfig_path)
        self.botPersonality = PersonalityManager(botConfig_path)
        self.botModel = self.botConfig.get("model", "mistral")

        self.memoryManager = MemoryManager(botMemory_path, self.botPersonality.getActuallyPersonality())

    # -- Função de fala e memória
    def botResponse(self, user_input):

        print("[DEBUG] Construindo prompt...")

        # - Construir uma resposta adequada com base na pergunta e na personalidade da IA
        prompt = constructPrompt(
            user_input, 
            self.memoryManager.getVagueMemory(), 
            self.botPersonality.getPrompt(), 
            self.botPersonality.getName()
            )
        
        print("[DEBUG] Prompt construído com sucesso.")
        print(f"[PROMPT] >>> {prompt[:200]}...")  # Mostra os 200 primeiros caracteres
        print("[DEBUG] Chamando generateResponse...")

        response = generateResponse(self.botModel, prompt)

        print("[DEBUG] Resposta recebida.")

        # - Depuração para garantir que a resposta saia corretamente
        if not isinstance(response, str) or not response.strip():
            response = "I'm sorry, something went wrong with my response."
        
        # - Guardar a pergunta e a resposta em uma "memória"
        self.memoryManager.addEntry(user_input, response)
        return response
    
    def switchPersonality(self, new_name):
        if self.botPersonality.switch(new_name):
            # Atualiza o MemoryManager para a nova personalidade
            self.memoryManager.setPersonality(self.botPersonality.getActuallyPersonality())
            return True
        return False
    
    @staticmethod
    def criterio_promover(entry):
        if "#favorito" in entry["User"].lower() or "#favorito" in entry["Bot"].lower():
            return True
        if len(entry["Bot"]) > 100:
            return True
        return False

        # -- Função chamada ao encerrar o programa
    def shutdown(self):
        print("[DEBUG] Encerrando o programa. Promovendo e limpando memórias vagas...")
        self.memoryManager.promoteVagueToImportant(self.criterio_promover)
        self.memoryManager.clearVagueMemory()
        print("[DEBUG] Memórias tratadas com sucesso.")

    # -- Função para iniciar o bot
    def start(self):
        
        ChatGUI(self).iniciar()

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= [End] =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=