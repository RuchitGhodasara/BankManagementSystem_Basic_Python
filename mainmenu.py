import time


def imp(i_d):
    import time
    print('.\n'*4)
    print('### MAIN MENU ###')
    print()
    print('(1)  Current Balance')
    print('(2)  Make Payment')
    print('(3)  More services')
    print('(4)  About our Project')
    print('\n"Enter" for Log out')
    print()
    choic6 = input('Make your Choice : ')

    if choic6 == '1':
        print('We are catching your Data...')
        time.sleep(2)
        import c_balance
        b = c_balance.balance(i_d)
        print()
        print('## Your Current Balance is : ', b)
        print()
        print('Note it CareFully...\nWe are Shifting you to Main menu in a while...')
        time.sleep(8)
        imp(i_d)

    elif choic6 == '2':
        print('\n\nYour recent Transactions...')
        time.sleep(3)
        from m_payment import payment
        payment(i_d)
        print('\nWait...')
        time.sleep(1.5)
        #print('\n\n *** Payment Succsessful ***\n')
        #print('Now Current Balance :',df.loc[i,'CurrentBalance'])
        time.sleep(2.5)
        imp(i_d)

    elif choic6 == '3':
        print('\n\nGetting All the Services...')
        time.sleep(2.5)
        import m_more
        m_more.more(i_d)
        print('\nMake Sure you satisfied...\nWe are Shifting you to Main menu in a while...')
        time.sleep(4)
        imp(i_d)
    
    elif choic6 == '4':
        print('''\nWe Heet & Ruchit decided to make this bank management system,
With full hard work, planning and fun we ended up with complex but curious project.
We learnt a lot about how to manage dataset(here .csv) in python,
We did many experiments and had fun with function call.
As a result we enjoyed the project a lot.
.
Although we had to deal with some basic facts.
# 1st,  Bank accounts are different from this one.
# 2nd, App Security is the key factor.
# 3rd,  Data management.''')
        heet = input("\n\nEnter for exit...")
        imp(i_d)

    elif choic6 == '':
        from insert import backupp
        backupp()
        print('\n\n ###  Thank you For Visiting Our Virtual Bank  ###')
        print('\n*** We are Logging You Out in while...\n\n\n\n\n')
        time.sleep(3)
        import Start
        Start.login_start()

    else:
        print()
        print('You Entered Something Wrong...')
        print('\n** WANT TO TRY AGAIN ? **')
        print()
        choic7 = input('Press "y" to Continue : ')
        if choic7 == 'y' or choic7 == 'Y':
            print('\nSo, We are moving you to Main Menu again \nWait for a While...\n')
            time.sleep(4)
            imp(i_d)
        else:
            print('.\n'*5)
            import Start
            Start.login_start()
