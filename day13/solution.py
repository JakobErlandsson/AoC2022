import functools
from os import getenv


def check(lhs, rhs):
    if lhs == rhs:
        return 0
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs < rhs:
            return 1
        elif lhs > rhs:
            return -1
        else:
            return 0
    if isinstance(lhs, int) and isinstance(rhs, list):
        lhs = [lhs]
    if isinstance(lhs, list) and isinstance(rhs, int):
        rhs = [rhs]
    if isinstance(lhs, list) and isinstance(rhs, list):
        lhs = lhs.copy()
        rhs = rhs.copy()
        while lhs or rhs:
            if not lhs and not rhs:
                return 0
            if not lhs:
                return 1
            if not rhs:
                return -1
            l = lhs.pop(0)
            r = rhs.pop(0)
            res = check(l, r)
            if res != 0:
                break
        return res


class Solution:


    def __init__(self):
        self.input_file = [(eval(i.split('\n')[0]), (eval(i.split('\n')[1]))) for i in open("input.txt", 'r').read().split('\n\n')]
        if getenv('part') == 'part2':
            self.input_file = [item for t in self.input_file for item in t]
            self.input_file.append([[2]])
            self.input_file.append([[6]])
            sort = sorted(self.input_file, key=functools.cmp_to_key(check), reverse=True)

            i_2 = sort.index([[2]]) + 1
            i_6 = sort.index([[6]]) + 1
            print(i_2*i_6)
        else:
            sum_of_indices = 0
            for (i, (lhs, rhs)) in enumerate(self.input_file):
                if check(lhs, rhs) == 1:
                    sum_of_indices += i+1
            print(sum_of_indices)







if __name__ == '__main__':
    sol = Solution()


