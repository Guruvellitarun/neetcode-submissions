from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxfreq = 0


    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        self.group[f].append(val)
        self.maxfreq = max(self.maxfreq, f)

    def pop(self) -> int:
        value = self.group[self.maxfreq].pop()
        self.freq[value] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()