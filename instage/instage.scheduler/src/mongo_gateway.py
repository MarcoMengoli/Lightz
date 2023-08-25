from pymongo import MongoClient
from model import Scene, Chore
from mappers import SceneMapper, ChoreMapper
from typing import Optional

class MongoGateway:
    def __init__(self, host: str = "localhost", port: int = 27017, db_name: str = "instage"):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.scenes_collection = None
        self.chores_collection = None

    def open(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
            self.scenes_collection = self.db['scenes']
            self.chores_collection = self.db['chores']
        except Exception as e:
            print(f"Error opening MongoGateway connection: {e}")

    def find_all_scenes(self) -> list[Scene]:
        try:
            documents = self.scenes_collection.find()
            return [SceneMapper.from_document(doc) for doc in documents]
        except Exception as e:
            print(f"Error fetching all scenes: {e}")
            return []

    def find_scenes_by_names(self, names: list[str]) -> list[Scene]:
        try:
            documents = self.scenes_collection.find({'name': {'$in': names}})
            return [SceneMapper.from_document(doc) for doc in documents]
        except Exception as e:
            print(f"Error fetching scenes by names: {e}")
            return []

    def find_chore_by_name(self, name: str) -> Optional[Chore]:
        try:
            chore_doc = self.chores_collection.find_one({'name': name})
            if not chore_doc:
                return None
            a = chore_doc['scene_names']
            scenes_for_chore = self.find_scenes_by_names(a)
            return ChoreMapper.from_document(chore_doc, scenes_for_chore)
        except Exception as e:
            print(f"Error fetching chore by name: {e}")
            return None
        
    def find_all_chores(self) -> list[str]:
        try:
            chore_docs = self.chores_collection.find()
            return [Chore(doc['name'], doc['scenes'], doc['timer']) for doc in chore_docs]
        except Exception as e:
            print(f"Error fetching all chores: {e}")
            return []

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
