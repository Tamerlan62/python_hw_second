def substrings(s):
    length = len(s)
    
    for elem in range(length):
        for el in range(elem + 1, length + 1):
            yield s[elem:el]
            
for elem in substrings('abc'):
    print(elem)