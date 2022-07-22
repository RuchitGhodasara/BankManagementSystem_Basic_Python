def mistak(f, l):
    if len(f) < 3 or len(l) < 3:
        return 0
    try:
        for a in f:
            try:
                namef = int(a)
                print('Name does not contains "Digits"...\n')
                return 0
                break
            except:
                print('', end='')
    except:
        print('', end='')
    try:
        for b in l:
            try:
                namef = int(b)
                print('Name does not contains "Digits"...\n')
                return 0
            except:
                print('', end='')
    except:
        print('', end='')


def m_(money):
    try:
        m = int(money)

    except:
        print('Not an Integer..\n')
        print('Account balance Should only contain Digits...')
        return 1
    if not(0 < m < 15001):
        print('Amount Is " Out off Range "')
        return 1
    else:
        return 2

    # return (Valid 1)
    # print('hi')


def num(cc):
    try:
        cc = int(cc)
        if 0 < cc < 6:
            return 1
        else:
            print('Your choice is "Out of Range"')
            return 2
    except:
        print('\n *** This is Not a Number !!! \n')
        return 3


def pay(bal, cur):
    try:
        bal = int(bal)
        if 0 < bal < cur:
            return 1
        else:
            print('Your Amount is "Out of Range"')
            print('You can pay 0 rupees to ', cur)
            return 2
    except:
        print('\n *** This is Not a Number !!! \n')
        return 3
