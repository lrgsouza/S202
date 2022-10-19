from CRUDescola import *

if __name__ == '__main__':

    escola = EscolaDB()

    # professor
    professor = [{
        'nome' :'Romario Alencar Azevedo',
        'idade' :33,
        'area' :'Matematica'
    },{
        'nome' :'Julio Cesar',
        'idade' :56,
        'area' :'Historia'
    },{
        'nome' :'Mirosvaldo Uriclécio',
        'idade' :29,
        'area' :'Matematica'
    },{
        'nome' :'Luiz inacio Osvaldinho',
        'idade' :85,
        'area' :'Historia'
    }]
    escola.create_professor(professor[0])
    escola.create_professor(professor[1])
    escola.create_professor(professor[2])
    escola.create_professor(professor[3])

    # Materia
    materia = [{
        'assunto':'Matematica',
        'horario':'19:30'

    },{
        'assunto':'Historia',
        'horario':'21:30'}
    ]
    escola.create_materia(materia[0])
    escola.create_materia(materia[1])


    #relacionamentos
    escola.create_relation_prof_materia(professor[0],materia[0],2005)
    escola.create_relation_prof_materia(professor[2],materia[0],2012)
    escola.create_relation_prof_materia(professor[1],materia[1],2009)
    escola.create_relation_prof_materia(professor[3],materia[1],2019)
