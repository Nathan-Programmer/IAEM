import tkinter as tk
from tkinter import scrolledtext
import threading

class ChatGUI:
    def __init__(self, bot):

        self.bot = bot

        self.window = tk.Tk()
        self.window.title(f"{bot.botPersonality.getName()}")

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled', width=80, height=20)
        self.chat_area.pack(padx=10, pady=10)

        self.chat_area.tag_configure("ia", foreground="purple", font=("Helvetica", 10, "bold"))
        self.chat_area.tag_configure("user", foreground="green", font=("Helvetica", 10))
        self.chat_area.tag_configure("system", foreground="gray", font=("Helvetica", 9, "italic"))

        self.entry = tk.Entry(self.window, width=80)
        self.entry.pack(padx=10, pady=(0,10))
        self.entry.bind("<Return>", self.on_enter_pressed)

        self.display_bot_message("Olá, como posso ajudar você hoje?")

    def display_bot_message(self, message):

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{self.bot.botPersonality.getName()}: {message}\n", "ia")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def display_user_message(self, message):

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"Você: {message}\n", "user")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def display_typing_indicator(self):

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{self.bot.botPersonality.getName()} está digitando...\n", "system")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def remove_typing_indicator(self):

        self.chat_area.config(state='normal')
        last_line_start = self.chat_area.index("end-2l linestart")
        last_line_end = self.chat_area.index("end-2l lineend+1c")
        self.chat_area.delete(last_line_start, last_line_end)
        self.chat_area.config(state='disabled')

    def commands_user_message(self, user_input):
        
        if user_input.startswith("/personality"):
            parts = user_input.split(maxsplit=1)
            if len(parts) == 2:
                new_personality = parts[1]
                success = self.bot.switchPersonality(new_personality)
                self.display_user_message(user_input)
                if success:
                    self.display_bot_message(f"Personalidade alterada para '{new_personality}'.")
                    self.window.title(f"{self.bot.botPersonality.getName()}")
                else:
                    self.display_bot_message(f"Personalidade '{new_personality}' não encontrada.")
            else:
                self.display_bot_message("Uso correto: /personality <nome_da_personalidade>")
            return True
        return False
        
    def on_enter_pressed(self, event):

        user_input = self.entry.get().strip()

        if not user_input:
            return
        if self.commands_user_message(user_input):  # <-- Adicionei retorno aqui
            self.entry.delete(0, tk.END)
            return
    
        self.entry.delete(0, tk.END)
        self.display_user_message(user_input)
        self.display_typing_indicator()
        threading.Thread(target=self.get_bot_response, args=(user_input,)).start()

    def get_bot_response(self, user_input):

        resposta = self.bot.botResponse(user_input)

        def update_chat():
            self.remove_typing_indicator()
            self.display_bot_message(resposta)

        self.window.after(0, update_chat)

    def iniciar(self):

        self.window.mainloop()
