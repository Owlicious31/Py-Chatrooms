import os
import sys
import tkinter
import traceback
from CTkMessagebox import CTkMessagebox

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from src.ui.chats_display import ChatsDisplay

class App:

    def __init__(self) -> None:
        self.chat_display = ChatsDisplay()
        tkinter.Tk.report_callback_exception = self.show_error

    
    def run(self) -> None:
        self.chat_display.mainloop()


    def show_error(self, *args):
        err = traceback.format_exception(*args)[-1]
        if "KeyboardInterrupt" in err:
            return
        CTkMessagebox(title="Error", message=f"An error occured: {err}", icon="cancel")

if __name__ == "__main__":
    app = App()
    app.run()