import unittest
from unittest.mock import MagicMock

from Agenda import Agenda, Show

class AgendaTestMock(unittest.TestCase):

    def test_init(self):
        agenda = Agenda()
        self.assertEqual([], agenda.readShows())

    def test_createShow(self):
        agenda = Agenda()
        show_mock = MagicMock(spec=Show)
        agenda.createShow(show_mock)
        self.assertEqual([show_mock], agenda.readShows())
        
if __name__ == '__main__':
    unittest.main()