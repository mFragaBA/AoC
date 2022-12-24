import re
import math

old = 0
new = 0
worry_level = 0

class Monkey:
    monke_pattern = r"((\d+):\n  Starting items: (.+)\n  Operation: (.*)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+))+"

    def __init__(self, monke_str):
        parsed_monke = re.match(Monkey.monke_pattern, monke_str, re.MULTILINE)
        self.monke_number = int(parsed_monke.group(2))
        self.items = [int(item) for item in parsed_monke.group(3).split(", ")]
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
        old = self.items[i]
        exec(self.op, globals())
        self.items[i] = math.floor(new / 3)

    def round(self):
        for i in range(len(self.items)):
            # print(i)
            self.inspect(i)
            if self.items[i] % self.test_reminder == 0:
                self.send_item(i, self.true_monke)
            else:
                self.send_item(i, self.false_monke)
        self.items = []


with open("input.txt", 'r') as infile:
    monkeys = [Monkey(monkey_str.strip()) for monkey_str in infile.read().split("Monkey")[1:]]

for monke in monkeys:
    monke.add_monkes(monkeys)
    # print(monke)

for round in range(20):
    # print("round: " + str(round))
    for monke in monkeys:
        #print("monke: " + str(monke.monke_number))
        monke.round()

    # for monke in monkeys:
    #     print(monke.items)

for monke in monkeys:
    print(monke.inspected_amount)
