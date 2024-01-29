from pymongo import MongoClient
from typing import Type, Mapping, Any
from ses_backend.schemas.schemas import Entity


class MongoDBRepository[EntityT : Entity]():
    def __init__(self, document_type: Type[EntityT]):
        self.document_type = document_type
        self.client:MongoClient[dict[str, Any]] = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['ses']
        self.collection = self.db[self.document_type.__name__.lower()]

    def get(self, id: str) -> EntityT:
        return self.collection.find_one({"_id": id})
    
    def get_all(self) -> list[EntityT]:
        items = self.collection.find()
        all_items:list[EntityT] = []
        for item in items:
            all_items.append(self.document_type(**item)) # type: ignore
        return all_items
    
    def create(self, entity: EntityT) -> EntityT:
        self.collection.insert_one(entity.model_dump(by_alias=True))
        return entity
    
    def update(self, entity: EntityT) -> EntityT:
        self.collection.update_one({"_id": entity.id}, {"$set": entity.model_dump()})
        return entity
    
    def delete(self, id: str) -> None:
        self.collection.delete_one({"_id": id})
    
    def find_by(self, query:Mapping[str, Any]) -> list[EntityT]:
        items = self.collection.find(query)
        all_items:list[EntityT] = []
        for item in items:
            all_items.append(self.document_type(**item)) # type: ignore
        return all_items
    
    def aggregate(self, query:list[Any]) -> list[EntityT]:
        items = self.collection.aggregate(query)
        all_items:list[EntityT] = []
        for item in items:
            all_items.append(self.document_type(**item))
        return all_items