# print(' Q1: What is the capatel city of Indai?','\n','(a) Indor','\n','(b) Panipath','\n','(c) New Delhi','\n','(d) Siliguri')
# ans=input('Write your choice:')
# if ans=='c':
#     p=100
#     print('Your answer is correct','\n','You won',p,'points','\n','Aap ka total score h',p)
#     Next=input('Kya aap 200 points ke liye agla sawal solve karna chahenge?\n(1)Yes or (2)No\n')
#     if Next=='1':
#         print(' Q2: Which city is known as paris of india','\n','(a) Darjiling','\n','(b) Jaipur','\n','(c) Kolkata','\n','(d) Chandigar')
#         ans=input('Write your choosen option:')
#         if ans=='b':
#             q=200
#             print('Your answer is correct','\n','You won',q,'points','\n','Aap ka total score h',p+q)
#             Next=input('Kya aap 500 points ke liye agla sawal solve karna chahenge?\n(1)Yes or (2)No\n')
#             if Next=='1':
#                 print('Q3: Who is the honrable prisedent of India \n (a) Mahatna gandhi \n (b) Narandra modi \n (c) Indra gandhi \n (d) Dropadi moormu')
#                 ans=input('What is your choice:')
#                 if ans=='d':
#                     r=500
#                     print('Aap jeet gaye h SASTA KBC aur aap ko milate h 500 points','\n','Aap ka total score h',p+q+r)
#                 else:
#                     print('Aapka safar yahi samapt hota h','\n','Dhanyawad','\n','Aap ka total score h',p+q)
#             else:
#                 print('Aapka safar yahi samapt hota h','\n','Dhanyawad','\n','Aap ka total score h',p+q)
#         else:
#             print('Aapka safar yahi samapt hota h','\n','Dhanyawad','\n','Aap ka total score h',p)
#     else:
#         print('Aapka safar yahi samapt hota h','\n','Dhanyawad','\n','Aap ka total score h',p)
# else:
#     print('Aapka safar yahi samapt hota h','\n','Dhanyawad','\n','Aap ka total score h',0)

  
                      #Let us try

def mcq(Question,Option1,Option2,Option3,Option4,Ans):
    '''Takes a Qusetion and 4 answer options and the correct option and make a MCQ formate question 
    also match the given ans to the correct ans and tell if it matched or not'''
    print(Question)
    print('',Option1,'\n',Option2,'\n',Option3,'\n',Option4)
    ans=input('Write your choosen option:')
    if ans==Ans:
        return 'correct'
    else:
        return 'incorrect'
    
                            #return ka mahatv samjho
    
# print(mcq.__doc__)      #IMPORTANT

#Example
# Q1=mcq('What is your name:','(a) Robin','(b) David','(c) Vishwakarma','(d) Prash','c')
# print(Q1)


Q1=mcq('Q1 Question','(a)','(b)','(c)','(d)','a')
if Q1=='correct':
    print('Aapka agla sawal ye raha aap ki computer screen pe')
    Q2=mcq('Q2 Question','(a)','(b)','(c)','(d)','a')
    if Q2=='correct':
        print('Aapka agla sawal ye raha aap ki computer screen pe')
        Q3=mcq('Q3 Question','(a)','(b)','(c)','(d)','a')
        if Q3=='correct':
            print('Aapka agla sawal ye raha aap ki computer screen pe')
            mcq('Q4 Question','(a)','(b)','(c)','(d)','a')
        else:
            print('Aap ka jawab galat h','\n','Aap ka safar yahi samapt hota h')
    else:
        print('Aap ka jawab galat h','\n','Aap ka safar yahi samapt hota h')
else:
    print('Aap ka jawab galat h','\n','Aap ka safar yahi samapt hota h')
    

"""Itni khushi"""