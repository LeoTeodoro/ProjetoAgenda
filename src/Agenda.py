import Show

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
