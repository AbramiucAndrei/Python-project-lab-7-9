from console.UI import Ui
#from tests import teste
from service.studentController import ServiceStudent
from service.disciplinaController import ServiceDisciplina
from service.noteController import ServiceNote###
from repo.inmemory import StudentRepo,DisciplinaRepo,NoteRepo
from repo.infile import FileDiscRepo,FileStudRepo,FileNoteRepo
from domain.validators import Validate_student, Validate_disciplina, Validate_note

#teste()
#repoStud=StudentRepo()
repoStud=FileStudRepo("studenti.txt")
valStud=Validate_student()
srv_stud=ServiceStudent(repoStud,valStud)

#repoDisc=DisciplinaRepo()
repoDisc=FileDiscRepo("discipline.txt")
valDisc=Validate_disciplina()
srv_disc=ServiceDisciplina(repoDisc,valStud)

#repoNote=NoteRepo()
repoNote=FileNoteRepo("note.txt")
valNote=Validate_note()
srv_note=ServiceNote(repoNote,valNote,repoStud,repoDisc)

generate=Ui(srv_stud,srv_disc,srv_note)
generate.run()



#run()
#lab 9 - teams
#lab 10 - with open("") as f:
#lab 12 - sortare dupa 2 parametri(dupa nota,in caz de egalitate dupa nume)