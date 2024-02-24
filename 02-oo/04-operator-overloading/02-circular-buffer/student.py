class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__buffer = []

    def add(self, item):
        if len(self.__buffer) == self.__n:
            self.__buffer.pop(0)
        self.__buffer.append(item)

    def __getitem__(self, index):
        return self.__buffer[index]

    def __len__(self):
        return len(self.__buffer)
