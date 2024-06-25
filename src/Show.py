class Show:
    def __init__(self, local:str, horario:str, data:str, nomeContratante:str, valor:float):
        self.__local = local
        self.__horario = horario
        self.__data = data
        self.__nomeContratante = nomeContratante
        self.__valor = valor
        
    def __repr__(self):
        return f"Show(local={self.__local}, horario={self.__horario}, " \
               f"data={self.__data}, Nome do contratante={self.__nomeContratante}, " \
               f"valor={self.__valor})"
    
    def mostrar_valor(self):
        return self.__valor