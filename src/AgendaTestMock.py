import unittest
from unittest.mock import MagicMock

from Agenda import Agenda, Show

class AgendaTestMock(unittest.TestCase):

    def test_init(self):
        agenda = Agenda()
        self.assertEqual([], agenda.readShows())
        
if __name__ == '__main__':
    unittest.main()