from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client.student_management

async def test_connection():
    collections = await db.list_collection_names()
    print("Connected to MongoDB. Collections:", collections)

import asyncio
asyncio.run(test_connection())
