# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 2.7
    letters_hash = get_letters_hash(S)
    distances_hash = get_distances_hash(letters_hash,S)
    #print(letters_hash,distances_hash)
    return get_number_cyclic_automorphisms(S,letters_hash,distances_hash)

def get_distances_hash(letters_hash,S):
    distances_hash = {}
    for key in letters_hash.keys():
        distances = set()
        if key != S[0]:
            indices =letters_hash[key]
            base = indices[0]
            for i in range(1,len(indices)):
                distance = abs(base - indices[i])
                distances.add(distance)
            distances_hash[key] = distances
    return distances_hash


def get_number_cyclic_automorphisms(S,letters_hash,distances_hash):
    shifts_to_try = letters_hash[S[0]]
    #if not are_letters_count_valid(letters_hash, len(shifts_to_try)):
        #return 1
    number_cyclic_automorphisms = 0
    for i in range(len(shifts_to_try)):
        if is_shift_cyclic_automorphism(letters_hash,shifts_to_try[i],i,S,distances_hash):
            number_cyclic_automorphisms += 1
    return number_cyclic_automorphisms

def are_letters_count_valid(letters_hash, length):
    for key in letters_hash.keys():
        #if length != len(letters_hash[key]):
        if len(letters_hash[key]) %2 != 0:
            return False
    return True


def is_shift_cyclic_automorphism(letters_hash,shift,shift_index,S,distances_hash):
    if shift == 0:
        return True
    for key in distances_hash:
        if shift not in distances_hash[key]:
            return False
    #for key in letters_hash.keys():
#        if key != S[0]:
#            key_base_index = letters_hash[key][0]
#            key_shift_index = letters_hash[key][shift_index]
#            if key_shift_index - key_base_index != shift:
#                return False
    return True


def get_letters_hash(S):
    letters_hash = {}
    for i in range(len(S)):
        indices = letters_hash.get(S[i],[])
        indices += [i]
        letters_hash[S[i]] = indices
    return letters_hash

def Main():
    S = 'byebye'
    print(solution(S))
    S = 'codility'
    print(solution(S))
    S = 'aaa'
    print(solution(S))
    S = 'cococo'
    print(solution(S))
    S = 'cocaco'
    print(solution(S))
    S = 'aaabaaab'
    print(solution(S))
    S = 'reallyreallyreallyreallyreally'
    print(solution(S))
    S = 'reallyreally'
    print(solution(S))

if __name__ == '__main__':
    Main()