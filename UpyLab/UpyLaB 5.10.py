def dupliques(seq):
    for elem in seq:
        if seq.count(elem) > 1:
            return True
    return False


dupliques(['a', 'b', 'c', 'a'])
dupliques(['a', 'b', 'c'])
