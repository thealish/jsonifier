import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("username"))
PGPASSWORD= str(os.getenv("pass"))
DATABASE = str(os.getenv("database"))

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

POSTGRES_URI= f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"