from show import Show

class Agenda:
    __shows: Show  = []
    
    def __init__(self):
        self.__shows = []
        pass

    def createShow(self, show):
        self.__shows.append(show)

    def readShows(self):
        return self.__shows

    def updateShow(self, index, updated_show):
        self.__shows[index] = updated_show

    def deleteShow(self, index):
        self.__shows.pop(index)
        
    def clearShows(self):
        self.__shows = []

    def mostrar_valor_show(self, index):
        if 0 <= index < len(self.__shows):
            return self.__shows[index].mostrar_valor()
        else:
            return "Índice inválido."