import copy
a = [1,2,3,4,['a','b']]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(5)
a[4].append('c')

if __name__ == '__main__':
    print a
    print b
    print c
    print d
