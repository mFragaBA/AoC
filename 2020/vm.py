class CodeExecutor():
    acc = 0
    lineno = 0
    code = []
    executedLines = []

    def parseOp(self, opString):
        op = opString[:3]
        sign = -1 if opString[4] == '-' else 1
        val = int(opString[5:])

        return (op, sign, val)

    def step(self):
        self.executedLines[self.lineno] = self.executedLines[self.lineno] + 1
        op, sign, val = self.code[self.lineno]

        if op == 'acc':
            acc = acc + sign * val
            self.lineno = self.lineno + 1
        elif op == 'jmp':
            self.lineno = self.lineno + sign * val
        else:
            self.lineno = self.lineno + 1

    def run(self):
        while self.lineno < len(self.code):
            self.step()

    def getAcc(self):
        return self.acc

    def getLineno(self):
        return self.lineno

    def loadCode(self, code):
        self.code = [self.parseOp(line) for line in code]
        self.executedLines = [0 for _ in range(len(self.code))]

    def resetState(self):
        self.acc = 0
        self.lineno = 0
        self.executedLines = [0 for _ in range(len(self.code))]

