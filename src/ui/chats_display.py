import os
import sys
import customtkinter as ctk
from tkinter import TclError

# Adding src directory to path in order to import functionality
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from functionality.session_manager import SessionManager
from .session_display import SessionDisplay
from util.exceptions import SessionParsingException

DARKER_GREY = "#141414"

class ChatLabelFrame(ctk.CTkFrame):

    def __init__(self,master: ctk.CTk) -> None:
        super().__init__(master=master)

        self.main_label = ctk.CTkLabel(master=self,text="Chats",text_color="white",font=("arial",24,"bold"),bg_color=DARKER_GREY,height=50,width=420)
        self.main_label.pack()


class MessagesDisplay(ctk.CTkScrollableFrame):

    def __init__(self,master: ctk.CTk,available_sessions: list[dict]) -> None:
        super().__init__(master=master)

        self.configure(height=400,width=400)
        self.parent = master

        if not available_sessions:
            self.no_sessions_label = ctk.CTkLabel(master=self,text="No Sessions",text_color="white",font=("arial",24,"bold"))
            self.no_sessions_label.pack(anchor="w")
        
        else:
            self.available_sessions = available_sessions
            self.session_buttons = []

            self.create_session_buttons(self.available_sessions)
            
    def create_session_buttons(self,sessions: list[dict]) -> None:
        """
        Create buttons linking to sessions.
        :param session: List of dicts containing session names and other info
        :returns: None
        """
        for index,info in enumerate(sessions):
                if not info:
                    continue

                elif not info["name"]:
                    session_button = ctk.CTkButton(
                        master=self,
                        text=f"{index + 1}. Unnamed Chat",
                        font=("arial",18,"normal"),
                        width=380,
                        height=60,
                        command= lambda i=index: self.open_session(index=i)
                        )
                
                else:
                    session_button = ctk.CTkButton(
                        master=self,
                        text=f"{index + 1}. {info["name"]}",
                        font=("arial",18,"normal"),
                        width=380,
                        height=60,
                        command= lambda i=index: self.open_session(index=i)
                        )
                
                session_button.pack(pady=10,anchor="w") 
                
                self.session_buttons.append(session_button)
        
        if not self.session_buttons:
            self.no_sessions_label = ctk.CTkLabel(master=self,text="No Sessions",text_color="white",font=("arial",24,"bold"))
            self.no_sessions_label.pack(anchor="w")

            raise SessionParsingException("Was unable to create links to existing sessions.")


    def open_session(self,index: int) -> None:
        """
        Create a session display GUI based on the index of the pressed button's info in the object's available sessions.
        :param index: The index of the info used to initialize the button
        :returns: None
        """
        session_info = self.available_sessions[index]
        session_name = session_info["name"]

        self.session_display = SessionDisplay(chat_name=session_name)

        # Destroying chats window so only one session can be active at a time
        try:
            self.parent.destroy()
        
        except TclError:
            # Ignoring the TclError raised when window can't be destroyed after destruction
            pass

        self.session_display.mainloop()


        # TODO - Add the ability for chat history to be retrieved


class SessionManagementFrame(ctk.CTkFrame):

    def __init__(self,master: ctk.CTk) -> None:
        super().__init__(master=master,fg_color=DARKER_GREY)

        self.configure(height=300,width=400)

        self.session_management_label = ctk.CTkLabel(master=self,text="Add/Create session",font=("arial",18,"normal"))
        self.session_management_label.grid(column=0,row=0,columnspan=2,pady=10)

        self.add_session_entry = ctk.CTkEntry(master=self,placeholder_text="Invite code here...")
        self.add_session_entry.grid(column=0,row=1,padx=10,pady=10)

        self.add_session_button = ctk.CTkButton(master=self,text="Add Session",command=self.add_session)
        self.add_session_button.grid(column=1,row=1,pady=10)

        self.new_session_entry = ctk.CTkEntry(master=self,placeholder_text="Session name...")
        self.new_session_entry.grid(column=0,row=3,padx=10,pady=10)

        self.new_session_button = ctk.CTkButton(master=self,text="Create Session",command=self.create_new_session)
        self.new_session_button.grid(column=1,row=3,pady=10)

    def add_session(self) -> None:
        pass


    def create_new_session(self) -> None:
        pass


class ChatsDisplay(ctk.CTk):
    
    def __init__(self) -> None:
        super().__init__()

        self.title("Your Chats")
        self.geometry("400x600")

        try:
            self.wm_iconbitmap("../../assets/app_icon.ico")
        except TclError:
            # Acessing assets directly when the code is run from app.py
            self.wm_iconbitmap("assets/app_icon.ico")

        self.maxsize(width=400,height=600)

        self.session_manager = SessionManager()
        self.chat_label = ChatLabelFrame(master=self)
        self.chat_label.grid(column=0,row=0)

        self.messages_display = MessagesDisplay(master=self,available_sessions=self.session_manager.all_sessions)
        self.messages_display.grid(column=0,row=1)

        self.session_management_display = SessionManagementFrame(master=self)
        self.session_management_display.grid(column=0,row=2,sticky="nsew")


if __name__ == "__main__":
    display = ChatsDisplay()
    display.mainloop()

        