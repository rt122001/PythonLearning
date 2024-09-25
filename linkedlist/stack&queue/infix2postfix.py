class Main:
    stack = []
    @staticmethod
    def push(item):
        Main.stack.append(item)
    @staticmethod
    def pop():
        return Main.stack.pop()
    #returns precedence of operators
    @staticmethod
    def precedence(symbol):
        if symbol in ['+', '-']:
            return 2
        elif symbol in ['*', '/']:
            return 3
        elif symbol == '^':
            return 4
        elif symbol in ['(', ')', '#']:
            return 1
        return 0
    #check whether the symbol is an operator
    @staticmethod
    def is_operator(symbol):
        return symbol in ['+', '-', '*', '/', '^', '(', ')']
    @staticmethod
    def convert(infix):
        postfix = ""
        j = 0
        Main.push('#')
        for symbol in infix:
            if not Main.is_operator(symbol):
                postfix += symbol
                j += 1
            else:
                if symbol == '(':
                    Main.push(symbol)
                else:
                    if symbol == ')':
                        while Main.stack[-1] != '(':
                            postfix += Main.pop()
                            j += 1
                        Main.pop()  # pop out '('
                    else:
                        if Main.precedence(symbol) > Main.precedence(Main.stack[-1]):
                            Main.push(symbol)
                        else:
                            while Main.precedence(symbol) <= Main.precedence(Main.stack[-1]):
                                postfix += Main.pop()
                                j += 1
                            Main.push(symbol)
        while Main.stack[-1] != '#':
            postfix += Main.pop()
            j += 1
        return postfix
    @staticmethod
    def evaluate(postfix):
        stack_int = []
        for ch in postfix:
            if ch.isdigit():
                stack_int.append(int(ch))
            else:
                operand2 = stack_int.pop()
                operand1 = stack_int.pop()
                if ch == '+':
                    stack_int.append(operand1 + operand2)
                elif ch == '-':
                    stack_int.append(operand1 - operand2)
                elif ch == '*':
                    stack_int.append(operand1 * operand2)
                elif ch == '/':
                    stack_int.append(operand1 / operand2)
        return stack_int[0]
    @staticmethod
    def main():
        infix = "1*(2+3)"
        postfix = Main.convert(infix)
        print("Infix expression is:", infix)
        print("Postfix expression is:", postfix)
        print("Evaluated expression is:", Main.evaluate(postfix))
Main.main()