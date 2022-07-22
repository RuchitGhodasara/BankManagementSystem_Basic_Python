import bhul
import time

def create():
    import time
    print()
    print()
    f_nam=input('Enter your First Name : ')
    l_nam=input('Enter Your Last name : ')
    import bhul
    check=bhul.mistak(f_nam,l_nam)
    if (check==0):
        print()
        print('We will not allow this as Name.')
        print('IF you want to Resubmit it...')
        choic4=input('press "y" in small : ')
        if choic4=='y':
            print('Page in Progress...')
            time.sleep(3)
            create()
        else:
            import Start
            Start.login_start()

    else:
        print()
        print('SET Password Between 8 to 12 characters.')
        d_pas=input('Set your Pasword : ')
        if 7<len(d_pas)<13:
            d_pas2=input('Now confirm Password : ')
            if d_pas2==d_pas:
                print()
                print('## Now Your ID - Password Are SET...\n')
                print('To Create Your Valid Account You Have To Provide Some more Info...')
                print('We are moving to next page...')
                time.sleep(3)
                from i_nfo import ac_info
                ac_info()
                [ac_t,money,atm_c,cred_c,rate]=ac()
                print('\n\n ###  CONGRATULATION  ###')
                print('Your All Details are there...\n')
                print('We are Generating Your Unique ID...')
                print('Wait for while...')
                time.sleep(4)
                d_id=(f_nam+'_'+l_nam[0]+l_nam[2]+'@'+d_pas[0]+d_pas[4])
                print()
                print('#### NOTE YOUR ID ####')
                print(d_id)
                print()
                print('TAKE A WILE AND NOTEDOWN your ID CAREFULLY')
                print('\n*** We are Saving Your Data...')
                time.sleep(4)
                print('Wait for a while...')
                import insert
                insert.add_id(d_id,d_pas)
                insert.ac_add(d_id,f_nam,l_nam,ac_t,money,atm_c,cred_c,rate,d_pas)
                print('we will let you to login page in while...')
                import time
                time.sleep(10)
                from Start import login_start
                login_start()
            else:
                print('Pasword MUST BE SAME !!')
                print()
                print('IF you want to Resubmit it...')
                choic3=input('press "y" in small : ')
                if choic3=='y':
                    create()
        else:
            print('We will not allow you to use that password.')
            print()
            print('IF you want to Resubmit it...')
            choic3=input('press "y" in small : ')
            if choic3=='y':
                create()
    
def ac():
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
    print()
    return [ac_t,money,atm_c,cred_c,rate]
        
        
        
    

        
        
