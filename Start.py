
def login_start():
    print()
    print()
    print('** LOGIN PAGE **')
    print()
    print('(1) Login ')
    print('(2) New user ')
    print('\n"Enter key" for Exit')
    print()
    choic1=input('Make Your Choice : ')
    print()
    if choic1=='1':
        from check import login_code
        login_code()
    elif choic1=='2':
        from i_nfo import base_info
        base_info()
        import iput
        iput.create()
    elif choic1=='':
        print(' ** Thank you for visiting our Virtual Bank...')
        import time
        time.sleep(2)
        import sys
        sys.exit()
    else:
        print('You have to INPUT Valid NUMBER :')
        choic2=input('Press "y" or "Y" to Continue Again : ')
        print()
        if choic2=='y' or choic2=='Y':
            login_start()
        else:
            import sys
            sys.exit()
        

####START######
print('Welcome to H & R Bank Services')
login_start()

