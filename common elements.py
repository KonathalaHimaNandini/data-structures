def lcs(a,b):
    a_set=set(a)
    b_set=set(b)
    if (a_set &b_set):
        print(a_set&b_set)
    else:
        print("no common elements")
a=[3,4,2,2,4]
b=[3,2,2,7]
lcs(a,b)
