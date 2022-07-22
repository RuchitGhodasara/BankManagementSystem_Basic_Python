def change_(_i, do_t, w):  # _i for id  ;  do_t for do this   ;  w for which thing to change
    import pandas as pd
    df = pd.read_csv('mainFile.csv')
    l = len(df['Id'])
    if w == 'A':
        i = 0
        while i < l:
            if (df['Id'] == _i).values[i] == True:
                df.loc[i, 'Atm_'] = do_t
                try:
                    df.to_csv('mainFile.csv', columns=['Id', 'FirstName', 'LastName', 'AccountType',
                                                       'CurrentBalance', 'Atm_', 'CreditCard_', 'InterestRate', 'Password'], index=0)
                    return do_t
                except:
                    print('\n\n * Sorry We could not update it...')
                break
            i = i+1

    if w == 'C':
        r = 0
        while r < l:
            if (df['Id'] == _i).values[r] == True:
                df.loc[r, 'CreditCard_'] = do_t
                try:
                    df.to_csv('mainFile.csv', columns=['Id', 'FirstName', 'LastName', 'AccountType',
                                                       'CurrentBalance', 'Atm_', 'CreditCard_', 'InterestRate', 'Password'], index=0)
                    return do_t
                except:
                    print('\n\n * Sorry We could not update it...')
                break
            r = r+1


def how(i_d, atm, credit):
    #from m_more import card_s
    # [atm,credit,a_c,rate]=card_s(iddd)
    if atm == 'On':
        print('\nEnter word -->> " off " if you want...\n')
        _at = input('Want to OFF ATM ? : ')
        if _at == 'off':
            nw1 = change_(i_d, 'N', 'A')
            if nw1 == 'N':
                nw1 = 'OFF'
                print('* ATM is now ', nw1)
        else:
            print('OK atm is still ON')
    elif atm == 'Off':
        print('\n\nPress word --: " yes " if you want...\n')
        _a_ = input('Want to place an Order of ATM ? : ')
        if _a_ == 'yes':
            nw2 = change_(i_d, 'Y', 'A')
            if nw2 == 'Y':
                nw2 = 'ON'
                print('* We have Recorded your " ATM " Service as', nw2)
        else:
            print('OK still your ATM is OFF.\n')

    if credit == 'On':
        print('\n\nEnter word -->> " off " if you want...\n')
        _cr = input('Want to OFF Credit Card ? : ')
        if _cr == 'off':
            nw3 = change_(i_d, 'N', 'C')
            if nw3 == 'N':
                nw3 = 'OFF'
                print('* CreditCard is now ', nw3)
        else:
            print('OK Credit Card is still ON')
    elif credit == 'Off':
        print('\n\nPress word --: " yes " if you want...\n')
        _c_ = input('Want to place an Order of Credit Card ? : ')
        if _c_ == 'yes':
            nw4 = change_(i_d, 'Y', 'C')
            if nw4 == 'Y':
                nw4 = 'ON'
                print('* We have Recorded your "Credit Card" Service as', nw4)
        else:
            print('OK still your Credit Card is OFF.\n')


def serv(i_d, atm, credit):
    print()
    print('You can make your card OFF')
    print('Or you can Place an Order for New card...\n')
    how(i_d, atm, credit)
