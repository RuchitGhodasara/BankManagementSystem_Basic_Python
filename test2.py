def ac():
    import bhul
    import time
    print()
    print('Note - Max Valid Amount is : 15000')
    money=input('Enter Some Balance : ')
    mo_=bhul.m_(money)
    if mo_==1:
        print('Enter Valid Amount')
        print()
        print('\n  Wait for While...')
        time.sleep(5)
        ac()
    money=int(money)
    cow=0
    while cow<3:
        cow+=1
        print('\nAccount Type :\n "S"-for Saving    "C"-for Current Account.\n')
        ac_t=input('Make your Choice : ')
        if ac_t=='s' or ac_t=='S':
            rate=4
            ac_t='S'
            break
        elif ac_t=='c' or ac_t=='C':
            ac_t='C'
            rate=0
            break
        else:
            print('\nMake A Valid Choice... ')
        if cow==3:
            print('Soory, But We will Not Tolerate mistackes this much time... ')
            import Start
    print('\nFor Sevices...')
    print('      "Y" for Yes:\n')
    atm_c=input('Want ATM ?          : ')
    cred_c=input('Want Credit Card?   : ')
    if atm_c=='y' or atm_c=='Y':
        atm_c='Y'
    else:
        atm_c='N'
        
    if cred_c=='y' or cred_c=='Y':
        cred_c='Y'
    else:
        cred_c='N'
    print('#####Done')

ac()
