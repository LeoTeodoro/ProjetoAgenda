import numpy as np

class Agenda:
    def __init__(self):
        self.shows = []

    def createShow(self, show):
        self.shows.append(show)

    def readShows(self):
        return self.shows

    def updateShow(self, id, updated_show):
        for i, show in enumerate(self.shows):
            if show['id'] == id:
                self.shows[i] = updated_show
                return
        print(f"Show com id {id} não encontrado.")

    def deleteShow(self, id):
        for i, show in enumerate(self.shows):
            if show['id'] == id:
                del self.shows[i]
                return
        print(f"Show com id {id} não encontrado.")
