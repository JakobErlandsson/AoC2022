from os import getenv


class Monkey:

    def __init__(self, items, operation, div, to_throw):
        self.items = items
        self.operation = operation
        self.div = div
        self.to_throw = to_throw
        self.inspections = 0

    def throw_to(self, index, other):
        item = self.items.pop(index)
        other.items.append(item)

    def test(self, number):
        return number % self.div == 0

    def calc_value(self, item):
        if self.operation[0] == '*':
            if self.operation[1] == 'old':
                return item*item
            else:
                return item*int(self.operation[1])
        else:
            return item+int(self.operation[1])


class Solution:

    def __init__(self):
        self.input_txt = [i.split('\n') for i in open("input.txt", 'r').read().split('\n\n')]
        self.monkeys = {}
        for r in self.input_txt:
            starting_items = [int(x.replace(',', '')) for x in r[1].split(' ')[4:]]
            operation = r[2].split(' ')[-2:]
            div = int(r[3].split(' ')[-1])
            true = int(r[4].split(' ')[-1])
            false = int(r[5].split(' ')[-1])

            self.monkeys[int(r[0].split(' ')[-1].replace(':', ''))] = Monkey(starting_items, operation, div,
                                                                             {'true': true, 'false': false})
        self.common_denominator = 1
        for m in self.monkeys.values():
            self.common_denominator *= m.div

    def do_round(self):
        for i in range(self.monkeys.__len__()):
            monke = self.monkeys[i]
            to_throw = []
            for (idx, item) in enumerate(monke.items):
                monke.inspections += 1
                item = monke.calc_value(item) % self.common_denominator
                if getenv('part') == 'part1':
                    item = item // 3
                monke.items[idx] = item
                if monke.test(item):
                    to_throw.append((idx, self.monkeys[monke.to_throw['true']]))
                else:
                    to_throw.append((idx, self.monkeys[monke.to_throw['false']]))
            for t in reversed(to_throw):
                monke.throw_to(t[0], t[1])


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        for _ in range(20):
            sol.do_round()
        insts = [sol.monkeys[m].inspections for m in range(sol.monkeys.__len__())]
    else:
        for _ in range(10000):
            sol.do_round()
        insts = [sol.monkeys[m].inspections for m in range(sol.monkeys.__len__())]
    sum = max(insts)
    insts.remove(max(insts))
    sum *= max(insts)
    print(sum)
