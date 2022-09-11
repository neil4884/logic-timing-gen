class Table:
    def __init__(self, bit_size, *args):
        self.__table = []
        self.__bit_size = bit_size
        __v = 2 ** self.__bit_size - 1
        if len(args) == 1:
            for e in args[0]:
                if e > __v:
                    raise Exception('Invalid table, value more than maximum')
            self.__table = sorted([bin(e)[2:].zfill(bit_size) for e in args[0]])
        else:
            for e in args:
                if e > __v:
                    raise Exception('Invalid table, value more than maximum')
            self.__table = sorted([bin(e)[2:].zfill(bit_size) for e in args])

        self.__group = [[u for u in self.__table if u.count('1') == i] for i in range(0, self.__bit_size + 1)]

        return

    def print(self):
        for elem in self.__table:
            print(elem)
        return

    def printGroup(self):
        for u in self.__group:
            for v in u:
                print(v)
            if len(u):
                print('-' * self.__bit_size)
        return

    def generateAdjacence(self):
        return

    @staticmethod
    def bitDifference(lhs: str, rhs: str) -> int:
        if len(lhs) == len(rhs):
            return sum([(c1 != c2) for c1, c2 in zip(lhs, rhs)])
        return -1

    @staticmethod
    def generateAll(bit_size):
        if bit_size:
            return [bin(e)[2:].zfill(bit_size) for e in range(2 ** bit_size)]
        return []

    @staticmethod
    def generateGray(bit_size):
        if bit_size:
            return [bin((i ^ (i >> 1)))[2:].zfill(bit_size) for i in range(1 << bit_size)]
        return []

    @staticmethod
    def generateTiming(filename, interval, verbose, /, variables):
        n = len(variables)
        gcs = Table.generateGray(n)
        t = 0
        if verbose:
            sout = '\t'.join(['$T', *['$I {}'.format(v) for v in variables]])
            print(sout)
            for gc in gcs:
                sout = '\t'.join([str((t := t + interval) - interval), *list(gc)])
                print(sout)
            sout = '\t'.join([str(interval * len(gcs)), *list(gcs[0])])
            print(sout)
            return

        with open(filename, mode='w', encoding='utf-8') as f:
            f.writelines('\t'.join(['$T', *['$I {}'.format(v) for v in variables]]) + '\n')
            f.writelines(['\t'.join([str((t := t + interval) - interval), *list(gc)]) + '\n' for gc in gcs])
            f.writelines('\t'.join([str(interval * len(gcs)), *list(gcs[0])]))

        return



if __name__ == '__main__':
    vars = ['A', 'B', 'C', 'D']
    Table.generateTiming('', 100, False, vars)
    pass