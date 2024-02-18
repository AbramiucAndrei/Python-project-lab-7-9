from service.disciplinaController import ServiceDisciplina
from service.studentController import ServiceStudent
from service.noteController import ServiceNote
from domain.entities import Student,Disciplina,Note
from domain.validators import ValidationError
from repo.repoError import RepoError
from utils.randomName import RandomName
class Ui:
    def __init__(self,srv_stud,srv_disc,srv_note):
        self.srv_stud=srv_stud
        self.srv_disc=srv_disc
        self.srv_note=srv_note

    def nume_random(self):
        """
        genereaza si returneaza un nume cu caractere din alfabet random
        """
        nume=""
        nume+=str(RandomName().getName().strip())
        nume+=" "
        nume+=str(RandomName().getName().strip())
        return nume
    def creeaza_student_random(self):
        """
        creaza si stocheaza in repo un student cu nume generat random
        """
        try:
            nume=self.nume_random()
            self.srv_stud.createStudent(nume)
        except RepoError as re:
            print(re)
        except ValidationError as ve:
            print(ve)
    def creeaza_disciplina_random(self):
        """
        creeaza si stocheaza in repo-ul disciplinelor o disciplina cu nume
        si profesor generate random
        """
        try:
            nume_disc=self.nume_random()
            prof=self.nume_random()
            self.srv_disc.createDiscipline(prof,nume_disc)
        except RepoError as re:
            print(re)
        except ValidationError as ve:
            print(ve)

    def comanda_valida(self,comanda):
        """
        verifica daca comanda este una din cele valabile
        """
        if not (comanda >= 1 and comanda <= 16):
            raise ValueError("Nu exista comanda")

    def get_comanda(self):
        """
        se citeste si returneaza o comanda valida

        """
        try:
            comanda = int(input("Introduceti comanda: "))
            self.comanda_valida(comanda)
            return comanda
        except ValueError as ex:
            print(ex)
            return self.get_comanda()

    def citeste_nume(self, msg):
        """
        functia citeste si returneaza un nume valid
        :param msg: mesajul ce se afiseaza inainte de citirea de la tastatura
        :return: numele,daca este valid
        """

        nume = input(msg).strip()
        #nume = RandomName().getName().strip()
        #nume=self.nume_random()
        for litera in range(len(nume)):
            if not (nume[litera].isalpha() or nume[litera] == ' '):
                raise ValueError("Nume invalid")

        return nume
    def citeste_id(self):
        """

        :param lista: lista cu studentii sau disciplinele
        :param err: mesajul de eroare, in cazul in care id ul citit nu e valid
        :return: id valid(ce se gaseste in lista)
        """
        try:
            _id = int(input("Introduceti un id: "))
            return _id
        except ValueError as ex:
            print(ex)
            return self.citeste_id()

    def citeste_student(self):
            """
            functia citeste numele unui nou student
            :param lista_stud: lista cu studentii de pana acum,in care va fi pus si cel nou
            :return: noul student
            """
            _nume = ""
            try:
                _nume = self.citeste_nume("Introduceti numele studentului: ")
                self.srv_stud.createStudent(_nume)
            except RepoError as er:
                print(er)
            except ValidationError as ex:
                print(ex)
            except ValueError as VE:
                print(VE)

    def citeste_disc(self):
        """
        functia citeste o noua disciplina
        :param lista_disc: lista cu disciplinele
        :return: noua disciplina citita
        """
        try:
            nume_disc = self.citeste_nume("Introduceti numele disciplinei: ")
            profesor_disc = self.citeste_nume("Introduceti numele profesorului: ")
            self.srv_disc.createDiscipline(profesor_disc,nume_disc)
        except ValueError as VE:
            print(VE)
        except ValidationError as er:
            print(er)
        except RepoError as ex:
            print(ex)
    def citeste_nota(self):
        """
        citeste si returneaza o nota valida
        """

        try:
            nota=int(input("Introduceti o nota: "))
            if not (nota>0 and nota <=10):
                raise ValueError("NOTA INVALIDA")
            return nota
        except ValueError as ve:
            print(ve)
            return self.citeste_nota()
    def sterge_student(self):
        """
        se citeste un id si se sterge studentul cu id ul respectiv
        """
        _id = self.citeste_id()
        try:
            self.srv_stud.stergeStudent(_id)
        except RepoError as er:
            print(er)
    def sterge_disciplina(self):
        """
                se citeste un id si se sterge disciplina cu id ul respectiv
        """
        _id=self.citeste_id()
        try:
            self.srv_disc.stergeDisciplina(_id)
        except RepoError as er:
            print(er)


    def modifica_nume_stud(self):
        """
        se citeste un id si un nou nume
        studentului cu id-ul citit i se va schimba numele in cel citit de la tastatura
        """
        try:
            _id=self.citeste_id()
            nume_nou=self.citeste_nume("Introduceti noul nume al studentului: ")
            self.srv_stud.modificaNume(nume_nou,_id)
        except RepoError as re:
            print(re)
        except ValueError as ve:
            print(ve)
    def modifica_nume_disc(self):
        """
        se citeste un id si un nou nume
        disciplinei cu id-ul citit i se va schimba numele in cel citit de la tastatura
        """
        try:
            _id=self.citeste_id()
            nume_nou=self.citeste_nume("Introduceti noul nume al disciplinei: ")
            self.srv_disc.modificaNume(nume_nou,_id)
        except RepoError as re:
            print(re)
        except ValueError as ve:
            print(ve)
    def modifica_prof_disc(self):
        """
        se citeste un id si un nou profesor
        disciplinei cu id-ul citit i se va schimba profesorul in cel citit de la tastatura
        """
        try:
            _id=self.citeste_id()
            prof_nou=self.citeste_nume("Introduceti noul nume al profesorului: ")
            self.srv_disc.modificaProf(prof_nou,_id)
        except RepoError as re:
            print(re)
        except ValueError as ve:
            print(ve)



    def afisare_student(self,student):
        """afisarea pe ecran a unui student"""
        print("id:", student.get_id(), ", nume:", student.get_nume(), end="")

    def afisare_disciplina(self,disc):
        """ afisarea pe ecran a unei discipline"""
        print("id:", disc.get_id(), ", nume:", disc.get_nume(), ", profesor:", disc.get_profesor(), end="")
    def afisare_nota(self,nota: Note):
        """afisarea pe ecran a unei note"""
        print("idNota:", nota.getIDnota(), ", idStud:", nota.getIDstud(), ", idDisc:", nota.getIDdisc(), ", nota:", nota.getNota(), end="")

    def afisare_lista_stud(self):
        """afisarea listei de studenti"""
        lista=self.srv_stud.getAllStudents()
        for stud in lista:
            self.afisare_student(stud)
            print(end="\n")
        # print("\n")

    def afisare_lista_disc(self):
        """afisarea listei de discipline"""
        lista=self.srv_disc.getAllDisciplines()
        for disc in lista:
            self.afisare_disciplina(disc)
            print(end="\n")
        # print("\n")

    def afisare_lista_note(self):
        """afisarea listei de note"""
        lista=self.srv_note.getAllGrades()
        for note in lista:
            self.afisare_nota(note)
            print(end="\n")

    def cauta_student(self):
        """
        se citeste un id si se cauta in lista de studenti, studentul cu id ul introdus
        """
        try:
            _id=self.citeste_id()
            return self.srv_stud.cautaStudent(_id)
        except RepoError as re:
            print(re)

    def cauta_disciplina(self):
        """
        se citeste un id si se cauta in lista de discipline, disciplina cu id ul introdus
        """
        try:
            _id=self.citeste_id()
            return self.srv_disc.cautaDisciplina(_id)
        except RepoError as re:
            print(re)

    def adauga_nota(self):
        """
        se citeste id ul unui student si al unei discipline si
        se adauga o nota
        """
        try:
            print("ID STUDENT: ")
            idStud=self.citeste_id()
            print("ID DISCIPLINA: ")
            idDisc=self.citeste_id()

            nota=self.citeste_nota()
            self.srv_note.createNota(idStud,idDisc,nota)
        except RepoError as re:
            print(re)

    def note_la_disciplina(self):
        print("ID DISCIPLINA")
        idDisc=self.citeste_id()
        try:
            nota=self.srv_disc.cautaDisciplina(idDisc)
            lista=self.srv_note.creare_lista_ordonata(idDisc)
            for el in lista:
                print("Nume: ",el[0],", Nota:",el[1])
        except RepoError as re:
            print(re)

    def creeaza_medii(self):
        try:
            lista=self.srv_note.creeaza_medii()
            for el in lista:
                print("Nume: ", el[0], ", Medie:", el[1])
        except RepoError as re:
            print(re)

    def restanti(self):
        print("ID DISCIPLINA")
        idDisc = self.citeste_id()
        try:
            lista = self.srv_note.creeaza_restanti(idDisc)
            for el in lista:
                print("Nume: ", el[0], ", Medie:", el[1])
        except RepoError as re:
            print(re)




    def afiseaza_comenzi(self):
        """afisarea comenzilor"""
        cmd="\n"
        cmd += "1.Adauga student\n"
        cmd += "2.Sterge student\n"
        cmd += "3.Adauga disciplina\n"
        cmd += "4.Sterge disciplina\n"
        cmd += "5.Modifica numele studentului cu un anumit id\n"
        cmd += "6.Modifica numele disciplinei cu un anumit id\n"
        cmd += "7.Modifica profesorul disciplinei cu un anumit id\n"
        cmd += "8.Adauga student cu nume random\n"
        cmd += "9.Adauga disciplina cu nume random\n"
        cmd += "10.Cautare student dupa id\n"
        cmd += "11.Cautare disciplina dupa id\n"
        cmd += "12.Adauga nota la un student si o disciplina\n"
        cmd += "13.Afisare lista de studenți și notele lor la o disciplină, ordonat: alfabetic după nume, notă\n"
        cmd += "14.Primi 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă)\n"
        cmd += "15.Studentii care NU au la momentul actual nota de trecere la o disciplina data ordonati crescator dupa nota,in cadrul aceleasi note ordonati alfabetic\n"
        cmd += "16.Exit\n"

        print(cmd)

    def run(self):
        while True:
            self.afiseaza_comenzi()
            comanda = self.get_comanda()
            if comanda == 1:
                self.citeste_student()
                self.afisare_lista_stud()
            elif comanda == 2:
                self.sterge_student()
                self.afisare_lista_stud()
            elif comanda == 3:
                self.citeste_disc()
                self.afisare_lista_disc()
            elif comanda==4:
                self.sterge_disciplina()
                self.afisare_lista_disc()
            elif comanda==5:
                self.modifica_nume_stud()
                self.afisare_lista_stud()
            elif comanda==6:
                self.modifica_nume_disc()
                self.afisare_lista_disc()
            elif comanda==7:
                self.modifica_prof_disc()
                self.afisare_lista_disc()
            elif comanda==8:
                self.creeaza_student_random()
                self.afisare_lista_stud()
            elif comanda==9:
                self.creeaza_disciplina_random()
                self.afisare_lista_disc()
            elif comanda==10:
                stud_cautat = self.cauta_student()
                if stud_cautat!=None:
                    print("Studentul a fost gasita: ")
                    self.afisare_student(stud_cautat)
            elif comanda==11:
                disc_cautata = self.cauta_disciplina()
                if disc_cautata!=None:
                    print("Disciplina a fost gasita: ")
                    self.afisare_disciplina(disc_cautata)
            elif comanda==12:
                self.adauga_nota()
                self.afisare_lista_note()
            elif comanda==13:
                self.note_la_disciplina()
            elif comanda==14:
                self.creeaza_medii()
            elif comanda==15:
                self.restanti()
            elif comanda==16:
                exit(0)
