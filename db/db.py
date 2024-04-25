import certifi #trae el paquete completo
from motor.motor_asyncio import AsyncIOMotorClient #trae una parte del paquete
import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URL= os.environ.get("MONGO_DB")
client = AsyncIOMotorClient(MONGO_URL, tlsCAFile=certifi.where())
database = client["ing_swii"]
collection = database["usuarios"]