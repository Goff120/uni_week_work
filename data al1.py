class Queue:
    def __init__(self, the_max=10):
        self.tail = 0
        self.head = 0
        self.data = [None] * the_max
        self.the_max = the_max

    def add_el(self, new):
        if (self.tail + 1) % self.the_max == self.head:
            raise ValueError("chill bro you at max")
        self.data[self.tail] = new
        self.tail = (self.tail + 1) % self.the_max

    def remove_el(self):
        if self.head == self.tail:
            raise ValueError("Chill bro you got nothing")
        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.the_max
        return value

    def peek_el(self):
        if self.head == self.tail:
            raise ValueError("Chill bro you got nothing")
        return self.data[self.head]

    def length(self):
        return (self.tail - self.head + self.the_max) % self.the_max
    
    def is_full(self):
        if (self.tail + 1) % self.the_max == self.head:
            return True
        else:
            return False
        
    def is_empty(self):
        if self.tail == self.head:
            return True
        else:
            return False


class Stack:
    def __init__(self, the_max=10):
        self.head = -1
        self.the_max = the_max
        self.data = [None] * the_max

    def push_el(self, new):
        if self.head == self.the_max - 1:
            raise ValueError("chill bro you at max")
        self.head += 1
        self.data[self.head] = new

    def pop_el(self):
        if self.head == -1:
            raise ValueError("Chill bro you got nothing")
        value = self.data[self.head]
        self.data[self.head] = None
        self.head -= 1
        return value

    def peek_el(self):
        if self.head == -1:
            raise ValueError("Chill bro you got nothing")
        return self.data[self.head]

    def length_el(self):
        return self.head + 1

def reverse():
    qu = Queue()
    qu.add_el(1)
    qu.add_el(2)
    qu.add_el(3)
    qu.add_el(4)
    qu.add_el(5)

    sa = Stack()
    for _ in range(5):
        value = qu.peek_el()
        sa.push_el(value)
        qu.remove_el()

    new_data = []
    for _ in range(5):
        value = sa.peek_el()
        new_data.append(value)
        sa.pop_el()

    print(new_data)

def dup_letter(string):
    stak = Stack(len(string))
    for letter in string:
        if stak.head != -1 and stak.peek_el() == letter:
            stak.pop_el()
        else:
            stak.push_el(letter)
    out = ""
    for i in range(stak.head + 1):
        out += stak.data[i]
    print(out)



if __name__ == "__main__":
    print("=== Testing Queue ===")
    q = Queue(5)
    q.add_el(10)
    q.add_el(20)
    q.add_el(30)
    print("Peek:", q.peek_el())  # should be 10
    print("Removed:", q.remove_el())  # removes 10
    print("Peek:", q.peek_el())  # should be 20
    print("Length:", q.length())  # should be 2

    print("\n=== Testing Stack ===")
    s = Stack(5)
    s.push_el(1)
    s.push_el(2)
    s.push_el(3)
    print("Peek:", s.peek_el())  # should be 3
    print("Popped:", s.pop_el())  # removes 3
    print("Peek:", s.peek_el())  # should be 2
    print("Length:", s.length_el())  # should be 2

    reverse()

    q2 = Queue(5)
    print(q2.is_empty()) #t
    print(q2.is_full()) #f
    for x in range (4):
        q2.add_el(x)

    print(q2.is_empty()) #f
    print(q2.is_full()) #t


    dup_letter("abbccd")
    dup_letter("dsallasg")
    dup_letter("abccbadd")