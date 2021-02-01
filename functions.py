import time

def create_suite2(a,b):
    arr = []
    for i in range(1, 300):
        for j in range(1, 300):
            arr.append(a*i)
            arr.append(b*j)
            arr.append(a*i + b*j)

    res = []
    for ar in arr:
        if ar not in res:
            res.append(ar)

    res.sort()
    print(res)

    c = 0
    n = -1
    for i in range(len(res) -1):
        if res[i] +1 == res[i+1]:
            if c == 0:
                n = res[i]
            c += 1
            if c == 1000:
                break
        else:
            c = 0
    print(n)

def create_suite3(a,b,c):
    arr = []
    for i in range(0,50):
        for j in range(0, 50):
            for k in range(0, 50):
                arr.append(a*i)
                arr.append(b*j)
                arr.append(c*k)
                arr.append(a*i + b*j + c*k)

    res = []
    for ar in arr:
        if ar not in res:
            res.append(ar)

    res.sort()
    print(res)
    c = 0
    n = -1
    for i in range(len(res) -1):
        if res[i] +1 == res[i+1]:
            if c == 0:
                n = res[i]
            c += 1
            if c == 1000:
                break
        else:
            c = 0
            n = -1
    print(n)

def get_number_with_2(a,b,n):
    i = 0
    while i * a <= n:
        if (n - (i*a)) % b == 0:
            return i, int((n - (i*a)) / b)
        i += 1
    return -1, -1

def get_number_with_3(a,b,c,n):
    a *= 10
    b *= 10
    c *= 10
    n *= 10
    i = j = 0
    find = False
    while i * a <= n:
        while (i*a) + (j * b) <= n:
            if (n - (i*a) - (j*b)) % c == 0:
                return i,j, int((n - (i*a) - (j*b)) / c)
            j += 1
        i += 1
        j = 0
    return -1,-1,-1

def get_number_with_5(a,b,c,d,e,n):
    a *= 10
    b *= 10
    c *= 10
    d *= 10
    e *= 10
    n *= 10

    i = j = k = l = 0
    while i*a <= n:
        while (i*a) + (j*b) <= n:
            while (i*a) + (j*b) + (k*c) <= n:
                while (i*a) + (j*b) + (k*c) + (l*d) <= n:
                    res = (n -(i*a) -(j*b) - (k*c) - (l*d))
                    if res % e == 0:
                        return i,j,k,l, int((n - (i*a) -(j*b) -(k*c) - (l*d)) /e)
                    l += 1
                k += 1
                l = 0
            j += 1
            l = k = 0
        i += 1
        l = k = j = 0
    return -1,-1,-1,-1,-1

def pgcd(a,b):
    while b != 0:
        r = a % b
        a,b = b, r
    return a

def is_divide(money, a):
    if (money*10) % (a*10) == 0:
        return int(money/a)
    else:
        return 0

def get_profit(a, action1, b, action2):
    action1_cost = action1['cost']*10
    action2_cost = action2['cost']*10
    return (a*action1_cost*int(action1['profit']) + b*action2_cost*int(action2['profit']))/1000

