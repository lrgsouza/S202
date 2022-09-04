import pymongo


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "localhost:27017"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, id, titulo, autor, ano, preco):
        return self.collection.insert_one({"_id": id, "titulo": titulo,"autor":autor, "ano": ano,"preco": preco})

    def read(self):
        return self.collection.find({})

    def readOne(self,id):
        return self.collection.find({"_id":id})

    def update(self, id, preco):
        return self.collection.update_one(
            {"_id": id},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, id):
        return self.collection.delete_one({"_id": id})
