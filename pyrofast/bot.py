from dotenv import load_dotenv
import os

class Bot(Client):
    def __init__(self, name, api_id=None, api_hash=None, bot_token=None, **kwargs):
        load_dotenv()

        api_id = api_id or os.getenv("API_ID")
        api_hash = api_hash or os.getenv("API_HASH")
        bot_token = bot_token or os.getenv("BOT_TOKEN")

        if not api_id or not api_hash:
            raise ValueError("API_ID y API_HASH son obligatorios. Defínelos en .env o pásalos al Bot.")

        super().__init__(name, api_id=api_id, api_hash=api_hash, bot_token=bot_token, **kwargs)
