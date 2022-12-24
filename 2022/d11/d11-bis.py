import re
import math

## Idea: each item saves the reminder by 13, 19, 5, 2, 11, 17, 3 and 7
modulos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

old = 0
new = 0
worry_level = 0

class Monkey:
    monke_pattern = r"((\d+):\n  Starting items: (.+)\n  Operation: (.*)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+))+"

    def build_item(item):
        it = {}
        for modulo in modulos:
            it[modulo] = int(item)

        return it

    def __init__(self, monke_str):
        parsed_monke = re.match(Monkey.monke_pattern, monke_str, re.MULTILINE)
        self.monke_number = int(parsed_monke.group(2))
        self.items = [Monkey.build_item(item) for item in parsed_monke.group(3).split(", ")]
        self.op = parsed_monke.group(4)
        self.test_reminder = int(parsed_monke.group(5))
        self.true_monke = int(parsed_monke.group(6))
        self.false_monke = int(parsed_monke.group(7))
        self.inspected_amount = 0
        self.other_monkes = {}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def add_monkes(self, monkes):
        for monke in monkes:
            self.other_monkes[monke.monke_number] = monke

    def accept_item(self, item):
        self.items.append(item)

    def send_item(self, i, monke):
        self.other_monkes[monke].accept_item(self.items[i])

    def inspect(self, i):
        global old, new
        self.inspected_amount += 1
        #print(self.items[i])
        for modulo, value in self.items[i].items():
            old = value
            exec(self.op, globals())
            # worry level is not divided by three anymore
            # self.items[i] = math.floor(new / 3)
            self.items[i][modulo] = new % modulo

    def round(self):
        for i in range(len(self.items)):
            # print(i)
            self.inspect(i)
            if self.items[i][self.test_reminder] % self.test_reminder == 0:
                self.send_item(i, self.true_monke)
            else:
                self.send_item(i, self.false_monke)
        self.items = []


with open("input.txt", 'r') as infile:
    monkeys = [Monkey(monkey_str.strip()) for monkey_str in infile.read().split("Monkey")[1:]]

for monke in monkeys:
    monke.add_monkes(monkeys)
    # print(monke)

for round in range(10000):
    # print("round: " + str(round))
    for monke in monkeys:
        #print("monke: " + str(monke.monke_number))
        monke.round()

    # for monke in monkeys:
    #     print(monke.items)
    #     print(monke.inspected_amount)

sorted_monkes = sorted(monkeys, key = lambda m: m.inspected_amount)

print(sorted_monkes[-1].inspected_amount * sorted_monkes[-2].inspected_amount)
