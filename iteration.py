class EvenNumbers:
    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 20:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration
          
obj = EvenNumbers()

for n in obj:
    print(n)
