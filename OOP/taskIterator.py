class Iterator:

    def __init__(self, array) -> None:
        self.array = array
        self.index = 0

    def hasNext(self):
        return self.index <= len(self.array) - 1

    def next(self):
        currentElement = self.array[self.index]
        self.index += 1
        return currentElement


class ArrayList:
    array = []

    def iterator(self):
        return Iterator(self.array)

    def add(self, element):
        self.array.append(element)

    def print(self):
        print(self.array)


def main():
    list = ArrayList()
    list.add(1)
    list.add(2)
    list.add(3)
    list.print()
    iterator = list.iterator()

    while iterator.hasNext():
        print(iterator.next())




main()
