import repo.repoError
from repo.inmemory import StudentRepo
from repo.repoError import RepoError
from domain.entities import Student
from domain.validators import Validate_student,ValidationError
class ServiceStudent:
    def __init__(self,repo,validator):
        self.repo=repo
        self.validator=validator

    def createStudent(self,nume):
        maxID=self.repo.maxID()

        stud_nou=Student(maxID+1,nume)
        self.validator.validate(stud_nou)
        self.repo.store(stud_nou)
    def stergeStudent(self,_id):
        self.repo.sterge(_id)

    def modificaNume(self,nume_nou,_id):
        self.repo.modifica_nume(nume_nou,_id)
    def cautaStudent(self,_id):
        return self.repo.cauta_student(_id)

    def getAllStudents(self):
        return self.repo.get_students()

def test_ServiceStudent():
    r=StudentRepo()
    v=Validate_student()
    sr=ServiceStudent(r,v)
    sr.createStudent("Ioan")
    assert sr.cautaStudent(1)!=None
    try:
        assert sr.cautaStudent(2)==None
        assert False
    except RepoError as re:
        assert re.getErrors()=="Nu exista student cu acest ID"

    assert sr.cautaStudent(1).get_nume()=="Ioan"
    sr.stergeStudent(1)
    assert sr.getAllStudents()==[]
test_ServiceStudent()