class Student:
    def __init__(self,id,_nume):
        """
        :param id: se primeste id-ul studentului
        :param _nume: se primeste numele studentului
        """
        self.__idStud=id
        self.nume=_nume
    def get_id(self):
        """
        :return: id-ul studentului
        """
        return self.__idStud
    def get_nume(self):
        """
        :return:numele studentului
        """
        return self.nume
    def set_nume(self,nume_nou):
        """
        :param nume_nou: se primeste noul nume al studentului,ce
        va fi inlocuit cu cel vechi
        """
        self.nume=nume_nou

class Disciplina:
    def __init__(self,id,_profesor,_numeDisc):
        """
        :param id: id-ul disciplinei
        :param _profesor: numele profesorului
        :param _numeDisc: numele disciplinei
        """
        self.__idDisc=id
        self.profesor=_profesor
        self.nume=_numeDisc
    def get_id(self):
        """
        :return: id-ul disciplinei
        """
        return self.__idDisc
    def get_profesor(self):
        """
        :return: profesorul disciplinei
        """
        return self.profesor
    def get_nume(self):
        """
        :return: numele disciplinei
        """
        return self.nume
    def set_profesor(self,profesor_nou):
        """
        :param profesor_nou: numele noului profesor de la disciplina "self"
        """
        self.profesor=profesor_nou
        #return self.profesor

    def set_nume(self,nume_nou):
        """
        :param nume_nou: numele nou al disciplinei "self"
        """
        self.nume=nume_nou
        #return self.nume

class Note:
    def __init__(self,id_nota,id_stud,id_disc,nota):
        self.id_nota=id_nota
        self.id_stud=id_stud
        self.id_disc=id_disc
        self.nota=nota

    def getIDnota(self):
        """
        return:id-ul notei
        """
        return self.id_nota
    def getIDstud(self):
        """
        return: id-ul studentului
        """
        return int(self.id_stud)
    def getIDdisc(self):
        """
        return:id-ul disciplinei
        """
        return self.id_disc
    def getNota(self):
        """
        return:nota
        """
        return self.nota


def test_Student():
    st=Student(1,"Andrei")
    assert st.get_id()==1
    assert st.get_nume()=="Andrei"
    st.set_nume("Matei")
    assert st.get_nume()=="Matei"
def test_Disciplina():
    dc=Disciplina(10,"Matei","Matematica")
    assert dc.get_id()==10
    assert dc.get_nume()=="Matematica"
    assert dc.get_profesor()=="Matei"
    dc.set_nume("Romana")
    assert dc.get_nume()=="Romana"
    dc.set_profesor("Andrei")
    assert dc.get_profesor()=="Andrei"
def test_Note():
    n=Note(1,2,3,10)
    assert n.getIDnota()==1 and n.getIDdisc()==3 and n.getIDstud()==2
    assert n.getNota()==10
test_Student()
test_Disciplina()
test_Note()