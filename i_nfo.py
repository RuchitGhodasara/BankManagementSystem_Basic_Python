import time


def base_info():
    print()
    print('** Quick Instructions... **')
    print('To go thourgh this Press "y" otherwise any key : ')
    choic4 = input('Your choice : ')
    if choic4 == 'y' or choic4 == 'Y':
        print()
        '''print('First you have to Understand,')
            print('# You only use this app if and only is when you have account in our bank.')
            print('And after that you can Use Account Details OR ATM to Join this Service.')
            print()
            print('** But as you know We can not Make Our Start Like This.. **')
            print()'''
        print()
        print('\n ** Read this INSTRUCTIONS carefully\n')
        print('So, we will provide you an ** Virtual Account **')
        print('We will ask some basic Informations...')
        print('After all, We will create your Valid ID.\nWhich will also be valid for Further USE')
        # 'along with Transaction History'
        print('And with this ID we will let you use our Services.')
        print('## Note you have to Remember Your ID Password. ##')
        print('\n we are moving you in that page')
        print('Wait for a while...')
        time.sleep(10)


def ac_info():
    print()
    print('** Quick Instructions... **')
    print('To go thourgh this...')
    choic5 = input('      Press "i" : ')
    if choic5 == 'i' or choic5 == 'I':
        print()
        print('Basic Info You have to provide :')
        print('1st Amount')
        print('2nd Account Type')
        print('3rd Service Status like ATM or Credit Card')
    print()
    print('** We will Hope, **\nYou will provide ALL information with ** LESS AND LESS ERROR **')
    print()
    print('Wait for a while...')
    print('We are moving to next page...')
    time.sleep(3)


'''
time.sleep(3) is good..
first we used...
t1=time.time()
while 1:
    t2=time.time()
    if t2-t1 >5:
        break
                    '''
