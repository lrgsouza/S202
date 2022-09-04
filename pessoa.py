from helper.WriteAJson import writeAJson

class Pessoa():

    def __init__(self,db):
        self.db = db

    def readAllBooks(self):
        return self.db.read()

    def updatePrice(self,id,preco):
        self.db.update(id,preco=preco)
        titulo = self.db.readOne(id)[0]['titulo']
        print(f"Preco do Livro {titulo} atualizado para R${preco}.")
        pass

    def addBook(self, id,titulo, autor, ano, preco):
        self.db.create(id,titulo, autor, ano, preco)
        print(f'Livro: {titulo} adicionado')

    def deleteBook(self, id):
        titulo = self.db.readOne(id)[0]['titulo']
        self.db.delete(id)
        print(f"Livro {titulo} deletado da coleção.")
        pass