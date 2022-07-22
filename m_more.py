def card_s(i_d):
    import pandas as pd
    data=pd.read_csv('mainFile.csv',index_col=0)
    a_tm=data.loc[i_d,'Atm_']
    c_tm=data.loc[i_d,'CreditCard_']
    act=data.loc[i_d,'AccountType']
    if a_tm=='Y':
        a_='On'
    else:
        a_='Off'
    if c_tm=='Y':
        c_='On'
    else:
        c_='Off'
    if act=='S':
        act='Saving Account'
        ra=4
    else:
        act='Current Account'
        ra=0
    return [a_,c_,act,ra]

    
def more(i_d):
    print()
    print(' ##  Your Current Status of Services  ##')
    print()
    [atm,credit,a_c,rate]=card_s(i_d)
    print('1. Atm           :  ',atm)
    print()
    print('2. Credit Card   :  ',credit)
    print()
    print('3. Account Type  :  ',a_c)
    print()
    print('* Interest Rate  :  ',rate,'%')
    print()
    #Option for Update Services
    print('\n# To Edit Services...\n')
    choic8=input('      Press "y" :')
    if choic8=='y' or choic8=='Y':
        from changes import serv
        serv(i_d,atm,credit)
    print()   
    
    
