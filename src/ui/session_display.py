import sys
import time
import threading
import customtkinter as ctk
from tkinter import TclError
import _tkinter

from src.functionality.session import Session
from src.functionality.db_manager import DatabaseManager

MESSAGE_DISPLAY_WIDTH = 32
MESSAGE_LINE_LIMIT = 50
MESSAGE_CHARACTER_LIMIT = MESSAGE_LINE_LIMIT * MESSAGE_DISPLAY_WIDTH
class SessionDisplay(ctk.CTk):

    def __init__(self, chat_name: str,username: str) -> None:
        super().__init__()

        self.protocol("WM_DELETE_WINDOW",self.quit)

        self.session = Session(chat_name,username)
        self.db_manager = DatabaseManager()

        self.title(f"Chat session - {chat_name}")
        self.geometry("400x600")

        try:
            self.wm_iconbitmap("../../assets/app_icon.ico")
        
        except TclError:
            # Acessing assets directly when the code is run from app.py
            self.wm_iconbitmap("assets/app_icon.ico")
        
        self.maxsize(width=400,height=600)

        self.messages_display = ctk.CTkScrollableFrame(master=self,height=300,width=270,border_width=5)
        self.messages_display.grid(column=0,row=1,columnspan=2,pady=30,padx=50)
        
        self.message_entry = ctk.CTkEntry(master=self,placeholder_text="Type your message")
        self.message_entry.grid(column=0,row=2,columnspan=2,pady=10,padx=50)

        self.send_message_button = ctk.CTkButton(master=self,height=20,text="Send Message",command=self.send_message)
        self.send_message_button.grid(column=0,row=3,columnspan=2,padx=50)

        self.return_button = ctk.CTkButton(master=self,text="Return to chats",command=self.return_to_chats)
        self.return_button.grid(column=0,row=0,sticky="w",pady=20,padx=10)

        self.messages_thread = threading.Thread(target=self.update_message_display,daemon=True)
        self.messages_thread.start()

        self.load_message_history()


    def display_message(self, message: str) -> None:
        """
        Packs messages on the message display. Messages that have exceed the display width are split into
        new messages and displayed with a recursive function call. Limit for these messages is 50 split messages.

        :param message: (string) the text to be displayed
        :return: None
        """
        lines_above_limit = int(len(message) / MESSAGE_DISPLAY_WIDTH)
        
        # a line limit is enforced to prevent recursion errors and to prevent overly long messages.
        if lines_above_limit > MESSAGE_LINE_LIMIT:
            self.display_message(f"[{self.session.username}] (Message was too long to be shown fully)")
        
        # In cases where a message takes up more than one 36-character line, one line is displayed and trimmed from
        # the message which is displayed again with a recursive function call.
        elif lines_above_limit != 0:
            message_label = ctk.CTkLabel(master=self.messages_display,text=message[:MESSAGE_DISPLAY_WIDTH])
            message_label.pack(anchor="w")

            trimmed_message = message[MESSAGE_DISPLAY_WIDTH:]
            self.display_message(trimmed_message)
        
        else:
            message_label = ctk.CTkLabel(master=self.messages_display,text=message)
            message_label.pack(anchor="w")


    def load_message_history(self) -> None:
        """
        Pack messages from the session's history onto the messages display.
        :return: None
        """
        for message in self.db_manager.get_message_history(self.session.name):
            self.display_message(message)
        
        self.messages_display._parent_canvas.yview_moveto(1.0)


    def send_message(self) -> None:
        """
        Call the session's send_message method and clear the message entry. Does not accept
        empty strings.
        :return: None
        """
        if not self.message_entry.get():
            return

        self.session.send_message(message=self.message_entry.get())
        self.message_entry.delete(0,"end")
    

    def update_message_display(self) -> None:
        """
        Update messages on the display in real-time. Checks each message sent to the session's
        queue and packs messages on the display if they aren't already in the displayed messages.
        This function runs in a background thread.
        :return: None
        """
        try:
            # Messages already on the display
            displayed_messages: list[str] = []
            
            while True:
                # All of the messages in the session's queue
                messages = self.session.receiver.messages
                
                # When no messages have been sent yet
                if not displayed_messages:
                    for message in messages:
                        message = message
                        self.display_message(message)

                        displayed_messages.append(message)
                        self.session.messages.append(message)
                        self.messages_display._parent_canvas.yview_moveto(1.0)

                else:
                    for i,message in enumerate(messages):
                        # Checking to see if the message's index exceeds the final index of the displayed messages
                        # / checking to see if the message is new or already displayed

                        if i > len(displayed_messages) - 1:
                            message = message
                            self.display_message(message)

                            displayed_messages.append(message)
                            self.session.messages.append(message)
                            self.messages_display._parent_canvas.yview_moveto(1.0)
                            
                time.sleep(1)
        
        # Ignoring the error raised when the thread joins after the window closes
        except _tkinter.TclError:
            pass

        except RuntimeError:
            pass


    def return_to_chats(self) -> None:
        from .chats_display import ChatsDisplay
        # Import is called in function to avoid circular imports

        self.db_manager.update_message_history(self.session.name,self.session.messages)
        self.chats_window = ChatsDisplay()

        # Destroying session window so only one session can be active at a time
        try:
            self.destroy()

        except TclError:
            # Ignoring the TclError raised when window can't be destroyed after destruction
            pass
        
        # Raising the window
        self.chats_window.deiconify()


    def quit(self) -> None:
        """
        Exit the mainloop and destroy the window. Ensures mainloop ends when "x" button is used to close the
        window
        :return: None
        """
        self.db_manager.update_message_history(self.session.name,self.session.messages)
        self.destroy()
        sys.exit(0)
