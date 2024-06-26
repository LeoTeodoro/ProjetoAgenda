import unittest

from Agenda import Agenda
from Show import Show


class TestAgenda(unittest.TestCase):

    def test_create_show(self):
        agenda = Agenda() # Cria uma nova agenda
        show = Show("Ginasio Municipal", "18:00", "09/05/2024", "Gusttavo Lima", 500.00) # Cria um objeto Show
        agenda.createShow(show) # Adiciona o show na agenda
        shows = agenda.readShows() # Recupera a lista de shows da agenda
        self.assertEqual(len(shows), 1) # Verifica se há apenas 1 show
        self.assertEqual(shows[0], show) # Verifica se o show adicionado é o mesmo que foi criado

    def test_update_show(self):
        agenda = Agenda() # Cria uma nova agenda
        show1 = Show("Local 1", "19:00", "10/05/2024", "Ana Castela", 700.00) # Cria um objeto Show
        show2 = Show("Local 2", "20:00", "11/05/2024", "Gustavo Mioto", 800.00) # Cria um objeto Show
        agenda.createShow(show1) # Adiciona o show na agenda
        agenda.createShow(show2) # Adiciona o show na agenda

        updated_show = Show("Local 3", "21:00", "12/05/2024", "Luan Pereira", 900.00)
        agenda.updateShow(0, updated_show) # Atualiza o show no índice 0

        shows = agenda.readShows() # Recupera a lista de shows da agenda
        self.assertEqual(shows[0], updated_show) # Verifica se o show foi atualizado corretamente

    def test_delete_show(self):
        agenda = Agenda() # Cria uma nova agenda
        show1 = Show("Local X", "17:00", "07/05/2024", "Henrique e Juliano", 100.00) # Cria um objeto Show
        show2 = Show("Local Y", "18:00", "08/05/2024", "Jorge e Matheus", 200.00) # Cria um objeto Show
        agenda.createShow(show1) # Adiciona o show na agenda
        agenda.createShow(show2) # Adiciona o show na agenda
        
        agenda.deleteShow(1) # Remove o show do índice 1
        shows = agenda.readShows() # Recupera a lista de shows da agenda
        self.assertEqual(shows[0], show1) # Verifica se o primeiro show restante está correto
        
    def test_read_shows(self):
        agenda = Agenda() # Cria uma nova agenda
        show1 = Show("Local A", "19:00", "10/05/2024", "Henrique e Juliano", 700.00) # Cria um objeto Show
        show2 = Show("Local B", "20:00", "11/05/2024", "Jorge e Mateus", 800.00) # Cria um objeto Show
        agenda.createShow(show1) # Adiciona o show na agenda
        agenda.createShow(show2) # Adiciona o show na agenda
        shows = agenda.readShows() # Recupera a lista de shows da agenda
        self.assertEqual(shows, [show1, show2]) # Verifica se a lista retornada está correta

    def test_clear_show(self):
        agenda = Agenda() # Cria uma nova agenda
        show1 = Show("Local L", "19:00", "10/05/2024", "Henrique e Juliano", 700.00) # Cria um objeto Show
        show2 = Show("Local M", "20:00", "11/05/2024", "Jorge e Mateus", 800.00) # Cria um objeto Show
        agenda.createShow(show1) # Adiciona o show na agenda
        agenda.createShow(show2) # Adiciona o show na agenda
        agenda.clearShows() # Limpa a lista de shows
        self.assertEqual(agenda.readShows(), []) # Verifica se a lista está vazia após a limpeza

    def test_clear_shows_not_empty(self):
        agenda = Agenda() # Cria uma nova agenda
        show1 = Show("Local L", "19:00", "10/05/2024", "Henrique e Juliano", 700.00) # Cria um objeto Show
        show2 = Show("Local M", "20:00", "11/05/2024", "Jorge e Mateus", 800.00) # Cria um objeto Show
        agenda.createShow(show1) # Adiciona o show na agenda
        agenda.createShow(show2) # Adiciona o show na agenda
        
        self.assertTrue(agenda.readShows())  # Verifica se a lista de shows não está vazia

        agenda.clearShows() # Limpa a lista de shows

        self.assertFalse(agenda.readShows()) # Verifica se a lista de shows está vazia
        
    def test_update_show_invalid_index(self):
        agenda = Agenda()
        show = Show("Local X", "17:00", "07/05/2024", "Henrique e Juliano", 100.00)
        agenda.createShow(show)

        updated_show = Show("Local 3", "21:00", "12/05/2024", "Luan Pereira", 900.00)

        with self.assertRaises(IndexError): # Verifica se a exceção é lançada
            agenda.updateShow(50, updated_show)  # Índice inválido
            
    def test_delete_show_invalid_index(self):
        agenda = Agenda()
        show = Show("Local X", "17:00", "07/05/2024", "Henrique e Juliano", 100.00)
        show2 = Show("Local X", "17:00", "07/05/2024", "Henrique e Juliano", 100.00)
        agenda.createShow(show)
        agenda.createShow(show2)

        with self.assertRaises(IndexError): # Verifica se a exceção é lançada
            agenda.deleteShow(20)  # Índice inválido

if __name__ == "__main__":
    unittest.main()