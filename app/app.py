import os
import sys
import tkinter
import traceback
from CTkMessagebox import CTkMessagebox

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from src.ui.login_screen import LoginScreen

class App:

    def __init__(self) -> None:
        self.login_screen = LoginScreen()
        tkinter.Tk.report_callback_exception = self.show_error

    
    def run(self) -> None:

        self.login_screen.mainloop()


    def show_error(self, *args):
        err = traceback.format_exception(*args)[-1]
        CTkMessagebox(title="Error", message=f"An error occured: {err}", icon="cancel")

if __name__ == "__main__":
    app = App()
    app.run()