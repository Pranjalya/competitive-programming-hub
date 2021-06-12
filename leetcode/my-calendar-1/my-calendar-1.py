from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        if len(self.booked) == 0:
            self.booked.extend([start, end-1])
            return True

        for i in range(0, len(self.booked), 2):
            if self.booked[i] <= start <= self.booked[i+1]:
                return False

        i = bisect_left(self.booked, start)

        if i == len(self.booked):
            self.booked.extend([start, end-1])
            return True
        elif (end-1) >= self.booked[i]:
            return False
        else:
            self.booked = self.booked[:i]+[start, end-1]+self.booked[i:]

        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)