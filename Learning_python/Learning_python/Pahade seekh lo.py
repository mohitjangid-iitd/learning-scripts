a=int(input('start table from:'))
b=int(input('end:'))
number=range(a,b+1)
for n in number:
    multiple=range(1,11)
    print('\n')        #alag-alag karne ke liye
    for m in multiple:
        print(n, 'X', m , '=',n*m) #make parsentable
        
        #while
        
# c=int(input('table of:'))
# d=1
# while(d<=10):
#     print(c,'X',d,'=',c*d)
#     d=d+1