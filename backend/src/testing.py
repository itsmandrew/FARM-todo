import os
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
print(f"MONGODB_URI: {MONGODB_URI}")


async def test_connection():
    client = None  # Initialize client to None
    try:
        # Initialize the MongoDB client
        client = AsyncIOMotorClient(MONGODB_URI)
        # Test the connection
        await client.admin.command('ping')
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {str(e)}")
    finally:
        # Close the connection only if the client was initialized
        if client:
            client.close()

# Run the test
asyncio.run(test_connection())
