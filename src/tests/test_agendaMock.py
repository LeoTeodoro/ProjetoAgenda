import unittest
from unittest.mock import MagicMock, Mock, patch

from Agenda import Agenda, Show

class AgendaTestMock(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()
    
    def test_init(self):
        self.assertEqual([], self.agenda.readShows())

    @patch('Agenda.Agenda.updateShow')
    def test_updateShow_with_patch(self, mock_updateShow):
        show_mock = Mock(spec=Show)
        self.agenda.createShow(show_mock)
        updated_show_mock = Mock(spec=Show)
        self.agenda.updateShow(0, updated_show_mock)
        mock_updateShow.assert_called_with(0, updated_show_mock)

    def test_updateShow_with_Mock(self):
        show_mock = Mock(spec=Show)
        self.agenda.createShow(show_mock)
        updated_show_mock = Mock(spec=Show)
        self.agenda.updateShow(0, updated_show_mock)
        self.assertEqual([updated_show_mock], self.agenda.readShows())

    def test_mostrar_valor_show(self):
        mock_show = Mock(spec=Show)
        mock_show.mostrar_valor.return_value = 1000.0
        self.agenda.createShow(mock_show)
        self.assertEqual(self.agenda.mostrar_valor_show(0), 1000.0)

    def test_not_called(self):
        agenda_mock = Mock(spec=Agenda)
        show_mock = Mock(spec=Show)
        agenda_mock.createShow(show_mock)
        agenda_mock.reset_mock()
        agenda_mock.createShow.assert_not_called()

    def test_updateShow_with_Mock_2(self):
        agenda_mock = Mock(spec=Agenda)
        show_mock = Mock(spec=Show)
        agenda_mock.createShow(show_mock)
        updated_show_mock = Mock(spec=Show)
        agenda_mock.updateShow(0, updated_show_mock)
        updated_show_mock_2 = Mock(spec=Show)
        agenda_mock.updateShow(0, updated_show_mock_2)
        agenda_mock.updateShow.assert_called()

    def test_updateShow_with_Mock_falha(self):
        agenda_mock = Mock(spec=Agenda)
        show_mock = Mock(spec=Show)
        agenda_mock.createShow(show_mock)
        updated_show_mock = Mock(spec=Show)
        agenda_mock.updateShow(0, updated_show_mock)
        updated_show_mock_2 = Mock(spec=Show)
        agenda_mock.updateShow(0, updated_show_mock_2)
        
        with self.assertRaises(AssertionError):
            agenda_mock.updateShow.assert_called_once_with(0, updated_show_mock)
        
if __name__ == '__main__':
    unittest.main()