import os
from dotenv import load_dotenv

if os.path.exists("Internal"):
   load_dotenv("Internal")

class Config:
    API_ID=
    API_HASH=""
    TOKEN=""
    SUDO = list(int(i) for i in os.environ.get("SUDO", "").split(" "))
    START_IMG=""
    BOT_ID=
    BOT_USERNAME=""
    BOT_NAME=""
  
