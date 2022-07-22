
def passw(idsheet,a):
        print()
        you_pass=input('Now, Enter Password : ')
        if you_pass==idsheet.loc[a].values[0]:
                                print('\n\n')
                                #print('Yes Right...')
                                print('We are moving you in Main Menu')
                                print('Wait for while...')
                                import time
                                time.sleep(2)
                                import mainmenu
                                mainmenu.imp(a)

def login_code():
        #print(idsheet)
        you_id=input('Enter Your ID carefully : ')
        #count1=-1
        import pandas as pd
        idsheet=pd.read_csv('id_password_.csv',index_col=0)
        for a in idsheet.index:
                #count1+=1
                countt=3
                coun=1
                if a==you_id:
                        countt=4
                        #coun=2
                        passw(idsheet,a)
                    
                if (countt==4):
                        if coun==1:
                                print('\n** Your Password does not match ** \n * NOTE Password is Case Sensitive')
                                print()
                                print('** WANT TO TRY AGAIN? **')
                                print()
                                choic2=input('Press "y" or "Y" to Continue : ')
                                if choic2=='y' or choic2=='Y':
                                    print('\nSo,\n Wait for a While...')
                                    import time
                                    time.sleep(5)
                                    iii=1
                                    passw(idsheet,a)
                                    while iii<4:
                                            iii+=1
                                            if iii==3:
                                                    print('\n\n ***  We are not allow this much failed attemps ***')
                                                    print('\n We are moving you to Start')
                                                    print('\n'*3)
                                                    import Start
                                                    Start.login_start()
                                            else:
                                                    print('\nSo,\n Wait for a While...')
                                                    import time
                                                    time.sleep(4)
                                                    passw(idsheet,a)
                                else:
                                        print()
                                        import Start
                                        Start.login_start()


        else:# else for "FOR LOOP"
                print()
                print('** Your ID does not in Databse **')
                print()
                print('\n* NOTE ID is Case Sensitive...Try it Again')
                print('\n ** OR ** NOT HAVE ID ?\n then choose 2nd option in Login Page : " New User " ')
                print('\n** WANT TO TRY AGAIN? **')
                choic2=input('   *Press "y" or "Y" to Continue : ')
                print()
                if choic2=='y' or choic2=='Y':
                    print('So, We are moving you to the Login Page again \n Wait for a While...')
                    import time
                    time.sleep(4)
                    #from Start import login_start
                    print()
                    login_code()
                    #login_start()
                    
                for a in range(7):
                    print()
                from Start import login_start
