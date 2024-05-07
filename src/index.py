import Agenda
import Show

def main():
    agenda = Agenda.Agenda()
    show1 = Show.Show("Praça da Sé", "20:00", "20/12/2021", "João", 1000.00)
    show2 = Show.Show("Copacabana", "20:00", "20/12/2021", "Maria", 1000.00)
    show3 = Show.Show("Aniversário", "20:00", "20/12/2021", "Joquim", 1000.00)
    agenda.createShow(show1)
    agenda.createShow(show2)
    agenda.createShow(show3)
    shows = agenda.readShows()
    for show in shows:
        print(show)
    show4 = Show.Show("Confraternização da firma", "20:00", "20/12/2021", "Eduardo", 1000.00)
    agenda.updateShow(1, show4)
    shows = agenda.readShows()
    for show in shows:
        print(show)
    agenda.deleteShow(1)
    shows = agenda.readShows()
    for show in shows:
        print(show)
        
if __name__ == "__main__":
    main()