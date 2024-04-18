class Repeat:
    def __init__(self, variable):
        self.__variable = variable

    def __iter__(self):
        return self

    def __next__(self):
        return self.__variable
