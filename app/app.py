import os
import sys
from CTkMessagebox import CTkMessagebox

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir,"..")
sys.path.append(os.path.abspath(parent_dir))

from src.ui.login_screen import LoginScreen

class App:

    def __init__(self) -> None:
        
        self.login_screen = LoginScreen()
    
    def run(self) -> None:

        self.login_screen.mainloop()

if __name__ == "__main__":
    app = App()

    try:
        app.run()
    
    except Exception as e:
        CTkMessagebox(title="Error", message=f"An error occured: {e}", icon="cancel")