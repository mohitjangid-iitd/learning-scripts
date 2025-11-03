# abc={'apple','orange','aalu',232,'orange'}
# print(abc)
# d={}     #not a set
# e= set()       #this is the empty set
# print(type(abc),type(d),type(e))



even={2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50}
m_of_3={3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48}
print(even.union(m_of_3))
s1=even.intersection(m_of_3)
print(s1)
print(even)
# even.intersection_update(m_of_3)
# print(even)
print(even.difference(m_of_3))
print(even.symmetric_difference(m_of_3))
print(even.isdisjoint(m_of_3))
print(even.issuperset(s1))
print(s1.issubset(m_of_3))
s1.add(5762)  #.update(74398)
print(s1)
s1.remove(30)
print(s1)
s1.discard(36)
print(s1)
# s1.remove(33)          #gives Error B'cos 33 is not in s1
# print(s1)
s1.discard(33)
print(s1)
print(s1.pop())            #giving 1st no.
s1.clear()
print(s1)
# del s1
# print(s1)                #gives Error B'cos s1 is deleted