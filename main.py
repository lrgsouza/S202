from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.Livros import dataset
from pessoa import Pessoa


##### == ENTREGA RELATORIO 5 == ####

#criando e resetando db
db = Database("relatorio_cinco","Livros",dataset)
db.resetDatabase()
#iniciando uma instancia de Pessoa
pessoa = Pessoa(db)

#adiciando um livro
pessoa.addBook(3,"Harry Potter and the Half Blood Prince","J.K. Rowling",2005,9.99)

#lendo todos os Livros
writeAJson(pessoa.readAllBooks(),'leituras_realizadas')

#alterando preço de um livro
pessoa.updatePrice(3, 14.90)

#deletando um livro
pessoa.deleteBook(3)