# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 2.7
    print(get_number_of_steps_from_bits(S))
    integer = get_integer_from_string(S)
    return get_number_of_steps(integer)

def get_number_of_steps_from_bits(bits):
    first_non_zero = 0
    while bits[first_non_zero] == '0':
        first_non_zero += 1
        if first_non_zero == len(bits):
            return 0
    steps = 1
    for i in range(len(bits)-1, first_non_zero,-1):
        if bits[i] == '1':
            steps += 1
        steps += 1
    return steps

def get_number_of_steps(integer):
    number_of_steps = 0
    while(integer != 0):
        if integer % 2 == 0:
            integer /= 2
        else:
            integer -= 1
        number_of_steps += 1
    return number_of_steps

def get_integer_from_string(S):
    integer,increment = 0,1
    for i in range(1,len(S)+1):
        if S[-i] == '1':
            integer += increment
        increment *= 2
    return integer

def Main():
    S = '011100'
    print(solution(S))
    S = '00'
    print(solution(S))
    S = '01'
    print(solution(S))

if __name__ == '__main__':
    Main()