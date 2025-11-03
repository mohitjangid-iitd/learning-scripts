#with while loop cases

# a=input('What is your name:')
# while a!='end':                     #enter again and again
#     name=a.capitalize()
#     match name:
#         case 'Name_1':
#             print('NickName_1')
#         case 'Name_2':
#             print('NickName_2')
#         case 'Name_3':
#             print('NickName_3')
#         case 'Name_4':
#             print('NickName_4')
#         case 'Name_5':
#             print('NickName_5')
#         case _:
#             print('Syman go back')
#     a=input('next:')

#with dictionary

nick_name={'Name_1':'NickName_1','Name_2':'NickName_2','Name_3':'NickName_3','Name_4':'NickName_4','Name_5':'NickName_5','Name_6':'NickName_6',
           'Name_7':'NickName_7'}
a=input('What is your name:').capitalize()
while a!='Exit':
    for b in nick_name.keys():
        if b!=None:
            print(b)
        else:
            print('You are not Rejestered')
        a=input('Next:').capitalize()
        if b==a:
            print(b)
        
        else:
            print('nop')