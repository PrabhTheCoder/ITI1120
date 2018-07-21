class Fibonacci:
    def get_nth_fibonacci(self, n):
        self.l = [0,1]
        n -= 1
        if n == 0
            return self.l[0]
        elif n == 1:
            return self.l[1]
        for i in range(2, n):
            self.l.append(self.l[i-2] + self.l[i-1])
        return self.l[-1]
