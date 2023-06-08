import base64
import hashlib
from typing import Any, Mapping

from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient


class Client:
    def __init__(self):
        self.str_conn: str = "mongodb+srv://augenz:zcxBzVDzKtvEOgBO@cluster0.rjsjucx.mongodb.net"
        self.client: MongoClient[Mapping[str, Any] | Any] = MongoClient(self.str_conn)
        self.database: Database[Mapping[str, Any] | Any] = self.get_database(database_name="chat")
        self.collection: Collection[Mapping[str, Any] | Any] = self.create_collection(database_name="chat",
                                                                                      collection_name="messages")

    def get_database(self, database_name: str):
        return self.client[database_name]

    def create_collection(self, database_name: str, collection_name: str):
        database = self.get_database(database_name)
        return database[collection_name]

    def insert_messages_to_collection(self, from_value: str, to_value: str, read_status_key: bool,
                                      message_value: bytes):
        self.collection.insert_one(
            {
                "from": from_value,
                "to": to_value,
                "readStatus": read_status_key,
                "message": message_value
            }
        )

    def read_from_collection(self, from_value: str, to_value: str, read_status_key: bool):
        return self.collection.find(
            {
                "from": from_value,
                "to": to_value,
                "readStatus": read_status_key
            }
        )

    @staticmethod
    def generate_fernet_key(key: bytes) -> bytes:
        assert isinstance(key, bytes)
        hlib = hashlib.md5()
        hlib.update(key)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
