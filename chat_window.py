import tkinter as tk
from tkinter import scrolledtext
from chatbot import Chatbot


class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("BWS Personal Search Robot")

        self.chat_display = scrolledtext.ScrolledText(master, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.msg_entry = tk.Entry(master, width=50)
        self.msg_entry.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self):
        user_message = self.msg_entry.get()
        self.display_message("Question: " + user_message)

        # Get response from your chatbot
        bot_response = Chatbot.get_response(user_message)
        self.display_message("Robot: " + bot_response)

        self.msg_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)


root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
