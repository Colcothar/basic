import math
print('Richter       Joules                  TNT')
print('1           ',(10**(1.5*1+4.8)),'     ',(10**(1.5*1+4.8))*(10**-9)/4.184)
print('5           ',(10**(1.5*5+4.8)),'     ',(10**(1.5*5+4.8))*(10**-9)/4.184)
print('9.1         ',(10**(1.5*9.1+4.8)),'  ',(10**(1.5*9.1+4.8))*(10**-9)/4.184)
print('9.2         ',(10**(1.5*9.2+4.8)),'  ',(10**(1.5*9.2+4.8))*(10**-9)/4.184)
print('9.5         ',(10**(1.5*9.5+4.8)),' ',(10**(1.5*9.5+4.8))*(10**-9)/4.184)
rich=input('Please enter a Richter scale value: ')
ric=float(rich)
print('Richter scale value:',ric)
print('Equivalence in joules : ',(10**(1.5*ric+4.8)))
print('Equivalence in tons of TNT : ',(10**(1.5*ric+4.8))*(10**-9)/4.184)


