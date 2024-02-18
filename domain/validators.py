from domain.entities import Student,Disciplina,Note
class ValidationError(Exception):
    """
    clasa de generare de exceptie
    """
    def __init__(self,error):
        self.__error=error
    def getErrors(self):
        return self.__error


class Validate_student:
    """validarea studentului si aruncarea exceptiei daca este cazul"""
    def validate(self, stud):
        errors=[]
        nume = stud.get_nume()
        #if stud.get_id() == "":
        #    errors.append("Studentul nu are id!")
        if nume == "":
            errors.append("Studentul nu are nume!")

        if len(errors)>0 : raise ValidationError(errors)

class Validate_disciplina:
    """
    validarea disciplinei is aruncarea exceptiei daca este cazul
    """
    def validate(self, disc):
        errors=[]
       # if disc.get_id() == "":
        #    errors.append("Disciplina nu are id!")
        if disc.get_nume() == "":
            errors.append("Disciplina nu are nume!")
        if disc.get_profesor() == "":
            errors.append("Disciplina nu are profesor!")
        if len(errors)>0 : raise ValidationError(errors)

class Validate_note:
    def __init__(self):
        pass
    def validate(self,nota):
        err=[]
        if nota.getIDnota() <1:
            err.append("Id-ul notei este invalid")
        if nota.getIDdisc() <1:
            err.append("Id-ul disciplinei este invalid")
        if nota.getIDstud() <1:
            err.append("Id-ul studentului este invalid")
        if nota.getNota() < 1 or nota.getNota() > 10:
            err.append("Nota este invalida")
        if len(err) != 0:
            raise ValidationError(err)


#TESTE
def test_Validate_student():
    val=Validate_student()

    st=Student(15,"vasi")
    try:
        val.validate(st)
    except ValidationError as ex:
        assert False

    st=Student(15,"")
    try:
        val.validate(st)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==1

def test_Validate_disciplina():
    disc=Disciplina(15,"","")
    val=Validate_disciplina()

    try:
        val.validate(disc)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==2

    disc=Disciplina(15,"Dan Popescu","")
    try:
        val.validate(disc)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==1

def test_Validate_note():

    val=Validate_note()

    nota = Note(0, 0, 0, 15)
    try:
        val.validate(nota)
        assert False
    except ValidationError as ve:
        assert len(ve.getErrors())==4

    nota = Note(1, 1, 1, 11)
    try:
        val.validate(nota)
        assert False
    except ValidationError as ve:
        assert len(ve.getErrors()) == 1

test_Validate_student()
test_Validate_disciplina()
test_Validate_note()