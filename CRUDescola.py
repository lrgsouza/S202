from db.database import Graph


class EscolaDB:

    def __init__(self):
        self.db = Graph(uri='bolt://3.86.76.100:7687',
                        user='neo4j', password='commissions-hinge-beat')

    # ================================ professor CRUD ===============================================
    # professor CREATE
    def create_professor(self, professor):
        return self.db.execute_query('CREATE (n:Professor {nome:$nome, idade:$idade, area:$area}) return n',
                                     {'nome': professor['nome'], 'idade': professor['idade'], 'area': professor['area']})
    # professor READ
    def read_professor(self, professor):
        return self.db.execute_query('MATCH (n:Professor {nome:$nome}) RETURN n',
                                     {'nome': professor['nome']})
    # professor UPDATE
    def update_professor_age(self, professor):
        return self.db.execute_query('MATCH (n:Professor {nome:$nome}) SET n.idade = $age RETURN n',
                                     {'nome': professor['nome'], 'idade': professor['idade']})
    def update_professor_area(self, professor):
        return self.db.execute_query('MATCH (n:Professor {nome:$nome}) SET n.area = $age RETURN n',
                                     {'nome': professor['nome'], 'area': professor['area']})
    # professor DELETE
    def delete_professor(self, professor):
        return self.db.execute_query('MATCH (n:Professor {nome:$nome}) DELETE n',
                                     {'nome': professor['nome']})

    # ================================ materia CRUD ===============================================
    # materia CREATE
    def create_materia(self, materia):
        return self.db.execute_query('CREATE (n:Materia {assunto:$assunto, horario:$horario}) return n',
                                     {'assunto': materia['assunto'], 'horario': materia['horario']})
    # materia READ
    def read_materia(self, materia):
        return self.db.execute_query('MATCH (n:Materia {assunto:$assunto}) RETURN n',
                                     {'assunto': materia['assunto']})
    # materia UPDATE
    def update_materia_assunto(self, materia):
        return self.db.execute_query('MATCH (n:Materia {assunto:$assunto}) SET n.assunto = $assunto RETURN n',
                                     {'assunto': materia['assunto']})
    def update_materia_horario(self, materia):
        return self.db.execute_query('MATCH (n:Materia {assunto:$assunto}) SET n.horario = $horario RETURN n',
                                     {'assunto': materia['assunto'], 'horario': materia['horario']})
    # materia DELETE
    def delete_materia(self, materia):
        return self.db.execute_query('MATCH (n:Materia {nome:$nome}) DELETE n',
                                     {'nome': materia['nome']})

    # ================================ relacionamento CRUD ===============================================
    # relacionamento CREATE
    def create_relation_prof_materia(self, professor, materia, ano):
        return self.db.execute_query('MATCH (n:Professor {nome:$prof_nome}), (m:Materia {assunto:$materia_assunto}) '
                                     'CREATE (n)-[r:LECIONA{desde: $desde}]->(m) RETURN n, r, m',
                                     {'prof_nome': professor['nome'], 'materia_assunto': materia['assunto'],
                                      'desde': ano})

    # relacionamento READ
    def read_relation_prof_materia(self, professor, materia):
        return self.db.execute_query('MATCH (n:Professor {nome:$prof_nome})-[r]->(m:Materia {assunto:$materia_assunto})'
                                     ' RETURN n, r, m',
                                     {'prof_nome': professor['nome'], 'materia_assunto': materia['assunto']})

    # relacionamento UPDATE
    def update_relation_prof_materia(self, professor, materia, ano):
        return self.db.execute_query('MATCH (n:Professor {nome:$prof_nome})-[r]->(m:Materia {assunto:$materia_assunto})'
                                     'SET r.desde = $desde RETURN r',
                                     {'prof_nome': professor['nome'], 'materia_assunto': materia['assunto'],
                                      'desde': ano})
    # relacionamento DELETE
    def delete_relation_prof_materia(self, professor, materia):
        return self.db.execute_query('MATCH (n:Professor {nome:$prof_nome})-[r]->(m:Materia {assunto:$materia_assunto})'
                                     'DELETE r',
                                     {'prof_nome': professor['nome'], 'materia_assunto': materia['assunto']})

