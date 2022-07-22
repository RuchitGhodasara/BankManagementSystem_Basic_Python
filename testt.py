def change_(_i,do_t,w):#_i for id  ;  do_t for do this   ;  w for which thing to change
    import pandas as pd
    df=pd.read_csv('mainFiletest.csv')
    l=len(df['Id'])
    print('\n\n\n\nHIIIIIIIIIIIIIIIIIII\n\n\nCHANGE')
    if w=='A':
        i=0
        print('\n\n\nW=====A\n\n')
        while i<l:
            if (df['Id']==_i).values[i]==True:
                print('\n i is ',i,'\n\ninside the IIIIIIIIFFFFFFFFFF')
                df.loc[i,'Atm_']=do_t
                print('\n i is ',i,'\n\ninside the IIIIIIIIFFFFFFFFFF')
                try:
                    print('\n\n\n  IN TRY\n\n')
                    df.to_csv('mainFiletest.csv',columns=['Id','FirstName','LastName','AccountType','CurrentBalance','Atm_','CreditCard_','InterestRate','Password'],index=0)
                    print('\n\n\nALLLLLL')
                    return do_t
                except:
                    print('\n\n * Sorry We could not update it...')
                break
            i=i+1
            
    if w=='C':
        r=0
        while r<l:
            if (df['Id']==_i).values[r]==True:
                df.loc[r,'CreditCard_']=do_t
                try:
                    df.to_csv('mainFiletest.csv',columns=['Id','FirstName','LastName','AccountType','CurrentBalance','Atm_','CreditCard_','InterestRate','Password'],index=0)
                    return do_t
                except:
                    print('\n\n * Sorry We could not update it...')
                break
                    

def how(i_d,atm,credit):
    #from m_more import card_s
    #[atm,credit,a_c,rate]=card_s(iddd)
    if atm=='On':
        print('\n\nEnter word -->> " off " if you want...\n')
        _at=input('Want to OFF ATM ? : ')
        if _at=='off':
            nw1=change_(i_d,'N','A')
            if nw1=='N':
                nw1='OFF'
                print('* ATM is now ',nw1)
        else:
            print('OK atm is still ON')
    elif atm=='Off':
        print('\n\nPress word --: " yes " if you want...\n')
        _a_=input('Want to place an Order of ATM ? : ')
        if _a_=='yes':
            nw2=change_(i_d,'Y','A')
            if nw1=='Y':
                nw1='ON'
                print('* We Recorded your " ATM " Service as',nw2)
        else:
            print('OK we you NOT have accsess to use ATM\n')
        
    if credit=='On':
        print('\n\nEnter word -->> " off " if you want...\n')
        _cr=input('Want to OFF CreditCard ? : ')
        if _cr=='off':
            nw3=change_(i_d,'N','C')
            if nw3=='N':
                nw3='OFF'
                print('* CreditCard is now ',nw3)            
        else:
            print('OK Credit Card is still ON')
    elif credit=='Off':
        print('\n\nPress word --: " yes " if you want...\n')
        _c_=input('Want to place an Order of CreditCard ? : ')
        if _c_=='yes':
            nw4=change_(i_d,'Y','C')
            if nw4=='Y':
                nw4='ON'
                print('* We Recorded your "CreditCard" Service as',nw4)            
        else:
            print('OK we you NOT have accsess to use ATM\n')


def serv(i_d,atm,credit):
    print()
    print('You can make your card OFF for an imergency')
    print('Or you can Place an order for New card...\n')
    how(i_d,atm,credit)




    
