# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class TIME:
    def __init__(self, T):
        T_array = list(map(int, T.split(':')))
        self.hh, self.mm, self.ss = T_array[0], T_array[1], T_array[2]

    def __str__(self):
        return str(self.hh) + ':' + str(self.mm) + ':' + str(self.ss)


    def is_time_interesting(self):
        digit_count = {}
        for digit in self.get_digits_of_number(self.hh):
            digit_count[digit] = digit_count.get(digit, 0) + 1
        for digit in self.get_digits_of_number(self.mm):
            digit_count[digit] = digit_count.get(digit, 0) + 1
        for digit in self.get_digits_of_number(self.ss):
            digit_count[digit] = digit_count.get(digit, 0) + 1
        return len(digit_count.keys()) <= 2

    def update_time(self):
        self.ss = self.ss + 1
        if self.ss == 60:
            self.mm += 1
            self.ss = 0
        if self.mm == 60:
            self.hh += 1
            self.mm = 0

    def is_time_equal(self, other_time):
        return (other_time.ss == self.ss and other_time.mm == self.mm and other_time.hh == self.hh)

    def is_time_greater(self, other_time):
        if self.hh > other_time.hh:
            return True
        if self.hh == other_time.hh and self.mm > other_time.mm:
            return True
        if self.hh == other_time.hh and self.mm == other_time.mm and self.ss > other_time.ss:
            return True
        return False

    def get_digits_of_number(self, number):
        return (number // 10, number % 10)


def solution(S, T):
    # write your code in Python 2.7
    s_time, t_time = TIME(S), TIME(T)
    if s_time.is_time_greater(t_time):
        temp = s_time
        s_time = t_time
        t_time = temp
    num_times_interesting = 0
    while not s_time.is_time_equal(t_time):
        if s_time.is_time_interesting():
            print(s_time)
            num_times_interesting += 1
        s_time.update_time()
    if s_time.is_time_interesting():
        print(s_time)
        num_times_interesting += 1
    return num_times_interesting

def Main():
    S = '15:15:00'
    T = '15:15:12'
    #print(solution(S,T))
    S = '22:22:21'
    T = '22:22:23'
    #print(solution(S, T))
    S = '04:22:21'
    T = '10:22:02'
    #print(solution(S, T))
    S = '00:00:00'
    T = '23:59:59'
    print(solution(S, T))
    S = '04:45:54'
    S_time = TIME(S)
    #print(S_time.is_time_interesting())

if __name__ == '__main__':
    Main()
