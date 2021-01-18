from bson import ObjectId

from models.stocks import TickerData


class CRUD:
    def __init__(self):
        self.database = TickerData

    def delete(self, id):
        self.database.objects(id=id).delete()

    def insert(self, data):
        self.database(**data).save()

    def update(self, id: str, data: dict):
        self.database.objects(id=id).update(**data)

    def read(self):
        return [i.__dict__ for i in self.database.objects().all()]

    def get_ids(self):
        return [i['id'] for i in self.database.objects().all()]


ob = CRUD()
print(ob.get_ids())
print(ob.update(id=ObjectId('6005a62bc4ccbfea7cb96fb1'), data={"name": "Pria"}))

print(ob.read())
