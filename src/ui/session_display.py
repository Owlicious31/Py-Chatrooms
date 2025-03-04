import os
import sys
import customtkinter as ctk
from tkinter import TclError

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from functionality.session import Session
from util.exceptions import NoMessageProvidedException

class SessionDisplay(ctk.CTk):

    def __init__(self,chat_name: str) -> None:
        super().__init__()

        self.session = Session()

        self.title(f"Chat session - {chat_name}")
        self.geometry("400x600")
        self.wm_iconbitmap("../../assets/app_icon.ico")
        self.maxsize(width=400,height=600)

        self.messages_display = ctk.CTkScrollableFrame(master=self,height=300,width=270,border_color="black",border_width=5)
        self.messages_display.grid(column=0,row=1,columnspan=2,pady=30,padx=50)
        
        self.message_entry = ctk.CTkEntry(master=self,placeholder_text="Type your message")
        self.message_entry.grid(column=0,row=2,columnspan=2,pady=10,padx=50)

        self.send_message_button = ctk.CTkButton(master=self,height=20,text="Send Message",command=self.send_message)
        self.send_message_button.grid(column=0,row=3,columnspan=2,padx=50)

        self.return_button = ctk.CTkButton(master=self,text="Return to chats",command=self.return_to_chats)
        self.return_button.grid(column=0,row=0,sticky="w",pady=20,padx=10)


    def send_message(self) -> None:
        if not self.message_entry.get():
            return

        messages = self.session.process_and_return_message(message=self.message_entry.get())
        
        for child in self.messages_display.winfo_children():
            child.destroy()

        for message in messages:
            message_label = ctk.CTkLabel(master=self.messages_display,text=message)
            message_label.pack(anchor="w")

        #TODO - Stop messages from being sent when the program first opens and sync messages between users
        # and reduce message sending delay. Add docstrings.
        

    def return_to_chats(self) -> None:
        from chats_display import ChatsDisplay
        #Import is called in function to avoid circular imports

        self.chats_window = ChatsDisplay()

        # Destroying session window so only one session can be active at a time
        try:
            self.destroy()

        except TclError:
            # Ignoring the TclError raised when window can't be destroyed after destruction
            pass

        self.chats_window.mainloop()

if __name__ == "__main__":
    app = SessionDisplay(chat_name="Test")
    app.mainloop()