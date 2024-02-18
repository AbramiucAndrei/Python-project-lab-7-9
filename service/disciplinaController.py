from repo.inmemory import DisciplinaRepo
from repo.repoError import RepoError
from domain.entities import Disciplina
from domain.validators import Validate_disciplina, ValidationError

class ServiceDisciplina:
    def __init__(self,repo,validator):
        self.repo=repo
        self.validator=validator

    def createDiscipline(self,profesor,nume):
        maxID=self.repo.maxID()

        disc_noua=Disciplina(maxID+1,profesor,nume)
        self.validator.validate(disc_noua)
        self.repo.store(disc_noua)
    def stergeDisciplina(self,id):
        self.repo.sterge(id)

    def modificaNume(self,nume_nou,_id):
        self.repo.modifica_nume(nume_nou,_id)
    def modificaProf(self,prof_nou,_id):
        self.repo.modifica_profesor(prof_nou,_id)
    def cautaDisciplina(self,_id):
        return self.repo.cauta_disciplina(_id)


    def getAllDisciplines(self):
        return self.repo.get_discipline()

"""def test_ServiceDisciplina():
    r=DisciplinaRepo()
    v=Validate_disciplina()
    sr=ServiceDisciplina(r,v)
    sr.createDiscipline("Ioan","Matematica")
    assert sr.cautaDisciplina(1)!=None
    try:
        assert sr.cautaDisciplina(2)==None
        assert False
    except RepoError as re:
        assert re.getErrors()=="Nu exista disciplina cu acest ID"

    assert sr.cautaDisciplina(1).get_nume()=="Matematica"
    sr.stergeDisciplina(1)
    assert sr.getAllDisciplines()==[]
test_ServiceDisciplina()"""

