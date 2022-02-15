class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):  # проверка стека на пустоту. Метод возвращает True или False
        if not self.stack:
            return True
        else:
            return False

    def push(self, new_el):  # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(new_el)

    def pop(self):  # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        result = self.stack.pop()
        return result

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        result = self.stack[-1]
        return result

    def size(self):  # возвращает количество элементов в стеке.
        result = len(self.stack)
        return result

    def check_balance(self, brackets):
        balance = True
        for el in brackets:
            if el in '([{':
                self.push(el)
            elif el in ')]}':
                if self.is_empty():
                    balance = False
                    break
                el_from_stack = self.pop()
                if el_from_stack == '(' and el == ')':
                    continue
                elif el_from_stack == '[' and el == ']':
                    continue
                elif el_from_stack == '{' and el == '}':
                    continue
                balance = False
                break
        if balance and self.size() == 0:
            print('Balanced')
        else:
            print('Unbalanced')


if __name__ == '__main__':
    admin = Stack()
    admin.check_balance('((([])))')





