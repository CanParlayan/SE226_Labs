from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline()
        x = x.split()
        y = []
        for i in x:
            if i not in y:
                y.append(i)
        for i in range(0, len(y)):
            print('Frequency of', y[i], 'is :', x.count(y[i]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline()
        words_dict = {}
        for word in x.split():
            words_dict[word] = words_dict.get(word, 0) + 1
        for key in words_dict:
            print("{} : {}".format(key, words_dict[key]))


txt = "strange.txt"
list = ListCount(txt)
list.calculateFreqs(txt)
dic = DictCount(txt)
dic.calculateFreqs(txt)
