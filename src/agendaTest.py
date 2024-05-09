import unittest

from Agenda import Agenda
from Show import Show


class TestAgenda(unittest.TestCase):

    def test_create_show(self):
        agenda1 = Agenda()
        show = Show("Ginasio Municipal", "18:00", "09/05/2024", "Gusttavo Lima", 500000.00)
        agenda1.createShow(show)
        shows1 = agenda1.readShows()
        self.assertEqual(len(shows1), 1)
        self.assertEqual(shows1[0], show)

    def test_update_show(self):
        agenda2 = Agenda()
        show1 = Show("Local 1", "19:00", "10/05/2024", "Updated Name", 700.00)
        show2 = Show("Local 2", "20:00", "11/05/2024", "Another Name", 800.00)
        agenda2.createShow(show1)
        agenda2.createShow(show2)

        updated_show = Show("Updated Local", "21:00", "12/05/2024", "New Name", 900.00)
        agenda2.updateShow(0, updated_show)

        shows2 = agenda2.readShows()
        self.assertEqual(shows2[0], updated_show)

    def test_delete_show(self):
        agenda3 = Agenda()
        show1 = Show("Local X", "17:00", "07/05/2024", "Test", 100.00)
        show2 = Show("Local Y", "18:00", "08/05/2024", "Another Test", 200.00)
        agenda3.createShow(show1)
        agenda3.createShow(show2)
        
        agenda3.deleteShow(1)
        shows3 = agenda3.readShows()
        self.assertEqual(shows3[0], show1)




if __name__ == "__main__":
    unittest.main()