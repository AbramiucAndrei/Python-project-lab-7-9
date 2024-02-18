from repo.inmemory import DisciplinaRepo,StudentRepo,NoteRepo
from domain.entities import Disciplina,Student,Note
class FileDiscRepo(DisciplinaRepo):
    def __init__(self,fileName):
        self.fileName=fileName
        DisciplinaRepo.__init__(self)
        self.importData()

    def importData(self):
        """try:
            f = open(self.fileName, "r")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"r") as f:
            line = f.readline().strip()
            while line != "":
                line = line.split(";")
                d=Disciplina(int(line[0]),line[1],line[2])
                self.store(d)
                line=f.readline().strip()

    def exportData(self):
        """try:
            f=open(self.fileName,"w")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"w") as f:
            for el in DisciplinaRepo.get_discipline(self):
                line=str(el.get_id())+";"+el.get_profesor()+";"+el.get_nume()+"\n"
                f.write(line)


    def store(self,disc):
        DisciplinaRepo.store(self,disc)
        self.exportData()

    def sterge(self,id):
        DisciplinaRepo.sterge(self,id)
        self.exportData()
    def modifica_nume(self,nume_nou,_id):
        DisciplinaRepo.modifica_nume(self,nume_nou,_id)
        self.exportData()
    def modifica_profesor(self, profesor_nou, _id):
        DisciplinaRepo.modifica_profesor(self,profesor_nou,_id)
        self.exportData()
    def maxID(self):
        return DisciplinaRepo.maxID(self)
    def get_discipline(self):
        return DisciplinaRepo.get_discipline(self)

class FileStudRepo(StudentRepo):
    def __init__(self,fileName):
        self.fileName=fileName
        StudentRepo.__init__(self)
        self.importData()

    def importData(self):
        """try:
            f = open(self.fileName, "r")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"r") as f:
            line = f.readline().strip()
            while line != "":
                line = line.split(";")
                s=Student(int(line[0]),line[1])
                self.store(s)
                line=f.readline().strip()
    def exportData(self):
        """try:
            f=open(self.fileName,"w")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"w") as f:
            for el in StudentRepo.get_students(self):
                line=str(el.get_id())+";"+el.get_nume()+"\n"
                f.write(line)


    def store(self, stud):
        StudentRepo.store(self,stud)
        self.exportData()
    def sterge(self, id):
        StudentRepo.sterge(self,id)
        self.exportData()
    def modifica_nume(self, nume_nou,_id):
        StudentRepo.modifica_nume(self,nume_nou,_id)
        self.exportData()
    def cauta_student(self,_id):
        return StudentRepo.cauta_student(self,_id)
    def maxID(self):
        return StudentRepo.maxID(self)
    def get_students(self):
        return StudentRepo.get_students(self)


class FileNoteRepo(NoteRepo):
    def __init__(self,fileName):
        self.fileName=fileName
        NoteRepo.__init__(self)
        self.importData()

    def importData(self):
        """try:
            f = open(self.fileName, "r")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"r") as f:
            line = f.readline().strip()
            while line != "":
                line = line.split(";")
                n=Note(int(line[0]),int(line[1]),int(line[2]),int(line[3]))
                self.store(n)
                line=f.readline().strip()

    def exportData(self):
        """try:
            f=open(self.fileName,"w")
        except IOError as io:
            print(io)
            return"""
        with open(self.fileName,"w") as f:
            for el in NoteRepo.get_note(self):
                line=str(el.getIDnota())+";"+str(el.getIDstud())+";"+str(el.getIDdisc())+";"+str(el.getNota())+"\n"
                f.write(line)


    def store(self,nota):
        NoteRepo.store(self,nota)
        self.exportData()

    def maxID(self):
        return NoteRepo.maxID(self)
    def cauta_nota(self,_id):
        return NoteRepo.cauta_nota(self,_id)
    def creare_lista(self,idDisc):
        return NoteRepo.creare_lista(self,idDisc)
    def get_note(self):
        return NoteRepo.get_note(self)

