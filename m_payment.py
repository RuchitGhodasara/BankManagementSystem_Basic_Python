def payment(i_d):
    import time
    import pandas as pd
    idsheet=pd.read_csv('mainFile.csv')
    print('')
    bb=0
    while bb<5:
        print((bb+1),') ',idsheet.loc[bb].values[1],'',idsheet.loc[bb].values[2])
        bb+=1
    print()
    cc=input('Make your choice from this : ')
    import bhul
    k=bhul.num(cc)
    if k==1:
        cc=int(cc)
        print()
        cc=cc-1
        import pandas as pd
        df=pd.read_csv('mainFile.csv')
        l=len(df['Id'])
        i=0
        while i<l:
            if (df['Id']==i_d).values[i]==True:
                print('Current balance : ',df.loc[i,'CurrentBalance'])
                bal=input('Enter Amount to Pay : ')
                from bhul import pay
                y=pay(bal,df.loc[i,'CurrentBalance'])
                if y==1:
                    bal=int(bal)
                    try:
                        df.loc[cc,'CurrentBalance']=(df.loc[cc,'CurrentBalance']+bal)
                        df.loc[i,'CurrentBalance']=(df.loc[i,'CurrentBalance']-bal)
                        df.to_csv('mainFile.csv',columns=['Id','FirstName','LastName','AccountType','CurrentBalance','Atm_','CreditCard_','InterestRate','Password'],index=0)
                        print('\n\n *** Payment Successful. ***\n')
                        print('Now Current Balance :',df.loc[i,'CurrentBalance'])
                        
                    except:
                        print('\n ** SORRY System is not Responding Right Now.. ')
                        print('Try after short time or contact near branch.\n')
                    break
                elif y==2:
                    print()
                    choic9=input('To Try again... " y " : ')
                    if choic9=='y':
                        print('\nWait...')
                        time.sleep(1)
                        payment(i_d)
                    break
                else:
                    print('\nWait...\n')
                    time.sleep(2)
                    from mainmenu import imp
                    imp(i_d)
                    break
            i+=1
                            
        
    elif k==2:
        choic8=input('To Retry... " r " : ')
        if choic8=='r':
            print('\nWait...')
            time.sleep(1.5)
            payment(i_d)
        
        
    else:
        print('Wait...')
        time.sleep(2)
        from mainmenu import imp
        imp(i_d)
            
            
            
    
    
    
