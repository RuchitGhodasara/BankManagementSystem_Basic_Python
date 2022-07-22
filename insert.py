def add_id(idd,passwordd):
    import pandas as pd
    idsheet=pd.read_csv('id_password_.csv')
    #idsheet=pd.DataFrame([[idd,passwordd]],columns=['Id','Password'])
    #print(idsheet)
    idsheet.loc[len(idsheet)]=[idd,passwordd]
    idsheet.to_csv('id_password_.csv',columns=['Id','Password'],index=0)
    print()
    print()

def ac_add(I,First,Last,Account,Current,tm_,reditCard_,Interest,Pass):
    import pandas as pd
    df=pd.read_csv('mainFile.csv')
    df.loc[len(df)]=[I,First,Last,Account,Current,tm_,reditCard_,Interest,Pass]
    df.to_csv('mainFile.csv',columns=['Id','FirstName','LastName','AccountType','CurrentBalance','Atm_','CreditCard_','InterestRate','Password'],index=0)
    print('\n\n')

def backupp():
    try:
        import pandas as pd
        df=pd.read_csv('mainFile.csv')
        df.to_csv('mainFile_backup.csv',columns=['Id','FirstName','LastName','AccountType','CurrentBalance','Atm_','CreditCard_','InterestRate','Password'],index=0)
        print()
    except:
        print('\n\n***Sorry for INTURRUPTING at LAST...')
        print('But our database is not catching BACKUP facilities due to some Thechnical reasons...')
        print('\n**So you are advide to Use Offline transaction for some time...')
        print()
