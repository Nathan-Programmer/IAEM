# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-- [Create by Nathan/Nyogami]--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

def constructPrompt(userInput, history, basePrompt, botName="Bot"):

    # - Formatar o prompt para ser aceito no código
    prompt = basePrompt + "\n"

    # - Criar a conversa na memória do bot
    for treand in history:
        prompt += f"User: {treand['User']}\n{botName}: {treand['Bot']}\n"

    # - Adicionar no prompt a pergunta do usuário e depois a fala do bot
    if userInput.strip().startswith("*") and userInput.strip().endswith("*"):
        prompt += f"{userInput}\n{botName}:"
    else:
        prompt += f"User: {userInput}\n{botName}:"

    return prompt

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= [End] =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=