import customtkinter as ctk
from all_chats_display import AllChatsDisplay

class ChatDisplayFrame(ctk.CTkFrame):
        
    def __init__(self,master) -> None:
        super().__init__(master=master)

        self.messages_display = ctk.CTkScrollableFrame(master=self)
        self.messages_display.grid(column=0,row=1,columnspan=2,pady=10,padx=20)
        
        self.message_entry = ctk.CTkEntry(master=self,placeholder_text="Type your message")
        self.message_entry.grid(column=0,row=2,columnspan=2,pady=10)

        self.send_message_button = ctk.CTkButton(master=self,height=20,text="Send Message",command=self.send_message)
        self.send_message_button.grid(column=0,row=3,columnspan=2)


    def send_message(self) -> None:
        # Message will be retrieved from a client with a fuction in functionality and added as a label to the messages display frame.
        # TODO - Create function to get input from the two users and create a new label in the frame containing the message
        pass


class SessionDisplay(ctk.CTk):

    def __init__(self,contact_name: str) -> None:
        super().__init__()

        self.title(f"Chat session - {contact_name}")
        self.geometry("400x600")
        self.maxsize(width=400,height=600)

        self.chat_frame = ChatDisplayFrame(master=self)
        self.chat_frame.place(x=70,y=150)

        self.return_button = ctk.CTkButton(master=self,text="Return to chats",command=self.return_to_chats)
        self.return_button.grid(column=0,row=0,sticky="w",pady=20,padx=10)
    
    def return_to_chats(self) -> None:
        self.chats_window = AllChatsDisplay()
        self.chats_window.mainloop()


if __name__ == "__main__":
    app = SessionDisplay(contact_name="Test")
    app.mainloop()