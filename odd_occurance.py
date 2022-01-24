def odd_times(array):
    unique_val=[]
    for n in array:
        if n not in unique_val:
            unique_val.append(n)
    for v in unique_val:
        count = 0
        for i in array:
            if v ==i:
                count +=1
        if count %2 != 0:
            return count

#other solutions
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]