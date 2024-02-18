from domain.entities import Note,Disciplina,Student
from domain.validators import Validate_note,ValidationError
from repo.inmemory import StudentRepo,DisciplinaRepo,NoteRepo
from repo.repoError import RepoError
from utils.bubbleSort import bubble_sort
from utils.shellSort import shell_sort
class ServiceNote:
    def __init__(self,repo,validator,studRepo :StudentRepo,discRepo :DisciplinaRepo):
        self.repo=repo
        self.validator=validator
        self.studRepo=studRepo
        self.discRepo=discRepo

    def createNota(self,idStud,idDisc,nota):
        #se verifica daca exista un student cu id-ul idStud
        self.studRepo.cauta_student(idStud)
        #se verifica daca exista o disciplina cu id-ul idDisc
        self.discRepo.cauta_disciplina(idDisc)


        maxID=self.repo.maxID()
        nota_noua=Note(maxID+1,idStud,idDisc,nota)
        #se creeaza obictul de tip nota
        self.validator.validate(nota_noua)
        self.repo.store(nota_noua)
    def getAllGrades(self):
        #returneaza lista de note
        return self.repo.get_note()
    def cauta_nota(self,_id):
        return self.repo.cauta_nota(_id)
    def creare_lista_ordonata(self,idDisc):
        lista=self.repo.creare_lista(idDisc)
        """for i in range (len(lista)):
            lista[i]=(self.studRepo.cauta_student(lista[i][0])).get_nume(), lista[i][1]"""
        for i in range(len(lista)):
            lista[i]=(self.studRepo.cauta_student(lista[i][0])).get_nume(), lista[i][1]

        #return  sorted(lista,key=lambda x:(x[0],x[1]))
        return shell_sort(lista,key=lambda x:(x[0],x[1]))

    def creeaza_medii(self):
        lista=[]
        for stud in self.studRepo.get_students():
        #for i in range(1,self.studRepo.maxID()+1):
         #   nume=(self.studRepo.cauta_student(i)).get_nume()
            nume=stud.get_nume()
            nr=0
            suma=0
            for el in self.getAllGrades():
                if el.getIDstud() == stud.get_id():
                    suma += el.getNota()
                    nr+=1
            if nr>0:
                suma= suma/nr
                lista.append((nume,suma))
        lista=bubble_sort(lista, key= lambda x:x[1], reverse=True)

        lenght=len(lista)#//5
        ##20% din lungimea listei/

        return lista[:lenght+1]
    def creeaza_restanti(self,idDisc):
        lista=[]
        for stud in self.studRepo.get_students():
            nume = stud.get_nume()
            nr = 0
            suma = 0

            for el in self.getAllGrades():
                if el.getIDstud() == stud.get_id() and el.getIDdisc()==idDisc:
                    suma += el.getNota()
                    nr += 1
            if nr > 0 and suma/nr < 5.0:
                suma = suma / nr
                lista.append((nume, suma))

        return bubble_sort(lista, key=lambda x:(x[1],x[0]))


def test_ServiceNote():
    r=NoteRepo()
    v=Validate_note()
    d=DisciplinaRepo()
    new_disc=Disciplina(1,"Ioan","Matematica")
    d.store(new_disc)

    s=StudentRepo()
    new_stud=Student(1,"Andrei")
    s.store(new_stud)
    sr=ServiceNote(r,v,s,d)
    sr.createNota(1,1,5)
    try:
        sr.createNota(1,1,0)
        assert False
    except ValidationError as ve:
        assert len(ve.getErrors())==1

    try:
        sr.createNota(0,0,11)
        assert False
    except RepoError:
        assert True


    assert len(sr.getAllGrades())==1
#test_ServiceNote()

