from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset
from lookup import get_lookup

compras = Database(database="database", collection="produtos", dataset=dataset)
compras.resetDatabase()

pessoas, carros = get_lookup()

#============= ENTREGA RELATORIO ==============

new = compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "cliente_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "comprador"  # nome da saida
        }
     }
    ,
    {"$group": {"_id": {"nome":{"$first":"$comprador.nome"}},"total": {"$sum": "$total"}}},  # formata os documentos
    {"$sort": {"total": -1} }, #ordena o total decrescente
    {"$unwind": '$_id'},
    {"$project":
         {"_id":0,"nome":"$_id.nome", "total": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}}
                }
     }, #organiza o que quero mostrar
    {"$replaceRoot": {
    "newRoot": {
        "nome": '$nome',
        "total": '$total',
        "desconto": '$desconto',
                }
                     }
    } #ordena a saída para o modelo proposto
])
writeAJson(new, "entrega_relatorio")






