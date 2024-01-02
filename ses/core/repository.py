from pymongo import MongoClient
from typing import Generic, TypeVar, Type, Any
from ses.schemas.schemas import EntityT

class MongoRepo(Generic[EntityT]):
    def __init__(self, entity_type: Type[EntityT], connection_string:str, db:str)->None:
        self.entity_type = entity_type
        self.client: MongoClient = MongoClient(connection_string)
        self.db = self.client[db]
        self.collection = self.db[entity_type.__name__]
    
    def get(self, id: str) -> EntityT:
        entity = self.collection.find_one({"_id": id})
        if entity is None:
            raise ValueError()
        return self.entity_type(**entity)
    
    def add(self, entity: EntityT) -> None:
        # May raise duplicate key
        self.collection.insert_one(entity.model_dump(by_alias=True))
    
    def add_many(self, entities: list[EntityT]) -> None:
        self.collection.insert_many(map(lambda e: e.model_dump(by_alias=True), entities))

    def remove(self, entity: EntityT) -> None:
        result = self.collection.delete_one({"_id": entity.id})
        if result.deleted_count == 0:
            raise ValueError()
    
    def remove_many(self, entities: list[EntityT]) -> None:
        self.collection.delete_many({"_id": {"$in": [entity.id for entity in entities]}})
    
    def get_by(self, filter:dict[str, Any]) -> list[EntityT]:
        return [self.entity_type(**found) for found in self.collection.find(filter)]
    