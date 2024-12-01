from motor import motor_asyncio
from pymongo.server_api import ServerApi
from config.config import settings

conn = motor_asyncio.AsyncIOMotorClient(
    settings.DATABASE_URI, server_api=ServerApi("1")
)

students_db = conn.get_database(settings.DATABASE_STUDENTS)
