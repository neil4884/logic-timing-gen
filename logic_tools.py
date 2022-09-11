class Table:
    def __init__(self, bit_size, *args):
        self.__table1 = []
        self.__table0 = []
        self.__bit_size = bit_size
        __v = 2 ** self.__bit_size - 1
        if len(args) == 1:
            for e in args[0]:
                if e > __v:
                    raise Exception('Invalid table, value more than maximum')
            self.__table1 = sorted([bin(e)[2:].zfill(bit_size) for e in args[0]])
            self.__table0 = sorted(
                [bin(e)[2:].zfill(bit_size) for e in [x for x in range(__v + 1) if x not in args[0]]])
        else:
            for e in args:
                if e > __v:
                    raise Exception('Invalid table, value more than maximum')
            self.__table1 = sorted([bin(e)[2:].zfill(bit_size) for e in args])
            self.__table0 = sorted(
                [bin(e)[2:].zfill(bit_size) for e in [x for x in range(__v + 1) if x not in args]])

        self.__ones = [[u for u in self.__table1 if u.count('1') == i] for i in range(0, self.__bit_size + 1)]
        self.__zeroes = [[u for u in self.__table0 if u.count('1') == i] for i in range(0, self.__bit_size + 1)]

        return

    def print(self, k=1):
        if k:
            for elem in self.__table1:
                print(elem)
            return
        for elem in self.__table0:
            print(elem)
        return

    def printGroup(self, k=1):
        if k:
            for u in self.__ones:
                for v in u:
                    print(v)
                if len(u):
                    print('-' * self.__bit_size)
            return
        for u in self.__zeroes:
            for v in u:
                print(v)
            if len(u):
                print('-' * self.__bit_size)
        return

    def generateAdjacent(self, k=1):
        bit_group = self.__table1
        n = len(bit_group)
        result = []
        merged = []
        if n > 1:
            print(self.nextAdjacent(bit_group[0], bit_group))
            print(bit_group)
        return bit_group

    @staticmethod
    def nextAdjacent(x, to_find: list):
        result = []
        for i, y in enumerate(to_find):
            if Table.isAdjacent(x, y):
                result.append(x)
                to_find.pop(0)
                result.extend(Table.nextAdjacent(y, to_find))
                return result
        return []

    @staticmethod
    def isAdjacent(lhs: str, rhs: str) -> bool:
        return Table.bitDifference(lhs, rhs) == 1
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
    def generateGrayTiming(filename, interval, verbose, variables):
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

    @staticmethod
    def generateTiming(filename, interval, verbose, variables, bits):
        t = 0
        if verbose:
            sout = '\t'.join(['$T', *['$I {}'.format(v) for v in variables]])
            print(sout)
            for bit in Table.generateBinary(len(variables), bits)[1]:
                sout = '\t'.join([str((t := t + interval) - interval), *list(bit)])
                print(sout)
            return
        with open(filename, mode='w', encoding='utf-8') as f:
            f.writelines('\t'.join(['$T', *['$I {}'.format(v) for v in variables]]) + '\n')
            f.writelines(['\t'.join([str((t := t + interval) - interval), *list(bit)]) + '\n'
                          for bit in Table.generateBinary(len(variables), bits)[1]])
        return

    @staticmethod
    def generateBinary(bit_size, decimals):
        return [bin(e)[2:].zfill(bit_size) for e in [x for x in range(2 ** bit_size) if x not in decimals]], \
               [bin(e)[2:].zfill(bit_size) for e in decimals]


if __name__ == '__main__':
    lab05_01_vars = ['A', 'B', 'C', 'D']
    lab05_01_test = [0, 1, 3, 2, 0, 4, 5, 7, 6, 4, 5, 13, 9, 11, 3, 1, 9,
                     15, 14, 12, 8, 10]
    Table.generateGrayTiming('lab05_01_01.tim', 100, 0, lab05_01_vars)
    Table.generateTiming('lab05_01_02.tim', 100, 0, lab05_01_vars, lab05_01_test)

    lab05_02_vars = ['A', 'B', 'C', 'D', 'E']
    lab05_02_test = [11, 15, 7, 3, 1, 0, 4, 12, 28, 20, 16, 17]
    Table.generateGrayTiming('lab05_02_01.tim', 100, 0, lab05_02_vars)
    Table.generateTiming('lab05_02_02.tim', 100, 0, lab05_02_vars, lab05_02_test)
