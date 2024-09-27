import os
from dotenv import load_dotenv

if os.path.exists("Internal"):
   load_dotenv("Internal")

class Config:
    API_ID=""
    API_HASH=""
    TOKEN=""
    SUDO=""
    START_IMG=""
    BOT_ID=""
    BOT_USERNAME=""
    BOT_NAME=""
  
