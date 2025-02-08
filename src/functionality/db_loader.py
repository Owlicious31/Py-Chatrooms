import requests

BIN_ID = "67a65014ad19ca34f8fb9865"
def load_json_data() -> dict:
    """
    Load the user json file from jsonbin.io
    """

    response = requests.get(f"https://api.jsonbin.io/v3/b/{BIN_ID}")
    

    return dict()