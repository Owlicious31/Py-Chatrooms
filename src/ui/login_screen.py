import customtkinter as ctk

class LoginFrame(ctk.CTkFrame):

    def __init__(self,master) -> None:
        super().__init__(master=master)
        
        self.login_label = ctk.CTkLabel(master=self,text_color="white",text="Login",font=("arial",80,"bold"))
        self.login_label.grid(column=0,row=0,columnspan=2)

        self.username_entry = ctk.CTkEntry(master=self,placeholder_text="Your Username")
        self.username_entry.grid(column=0,row=1,columnspan=2,pady=30)

        self.password_entry = ctk.CTkEntry(master=self,placeholder_text="Your Password")
        self.password_entry.grid(column=0,row=2,columnspan=2)

        self.login_button = ctk.CTkButton(master=self,text="Login",command=self.login_user)
        self.login_button.grid(column=0,row=3,pady=20,padx=30)

        self.new_user_checkbox = ctk.CTkCheckBox(master=self,text="I'm a new user",width=20,height=20)
        self.new_user_checkbox.grid(column=1,row=3,padx=10)


    def login_user(self) -> None:
        """
        Log a user into their account or sign up a new user.
        :returns: None
        """
        
        if self.new_user_checkbox.get() == 1:
            pass
            # TODO - Make signup method in login_manager and call it here.
            # Create a new user object and write it's password and username to the db
        
        else:
            pass
            # TODO - Make login method in login_manager and call it here.
            # Check if user exists and validate credentials


class LoginScreen(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("400x600")
        self.wm_iconbitmap("../../assets/app_icon.ico")
        self.maxsize(width=400,height=600)

        self.login_frame = LoginFrame(master=self)
        self.login_frame.place(x=40,y=150)


if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()