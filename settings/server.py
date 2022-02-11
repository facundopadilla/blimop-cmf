import os
from fastapi import FastAPI


class ServerManager:

    def __init__(self):
        self.app = FastAPI(title="Telegram Chat Bot", debug=int(os.environ.get("DEBUG", True)))

    def get_app(self) -> FastAPI:
        return self.app


server_manager = ServerManager()
