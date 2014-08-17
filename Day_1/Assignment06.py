from math import pow
print('This program can convert octave/pitchclass pairs into their appropriate Hertz values. It uses the tempered scale conversions.')
p=input('Give me an octave value: ')
p1=float(p)
o=input('Give me a pitch class: ')
o1=float(o)
pitch=p1-4
octave=o1-9
freq=440*pow(2,(pitch+(octave/12)))
print(int(p1),' . ',int(o1),' equals ',freq)
print('\n \n Lets do that again shall we ')
p=input('Give me an octave value: ')
p1=float(p)
o=input('Give me a  pitch class: ')
o1=float(o)
pitch=p1-4
octave=o1-9
freq=440*pow(2,(pitch+(octave/12)))
print(int(p1),' . ',int(o1),' equals ',freq)
print('\n\n One more time ')
p=input('Give me an octave value: ')
p1=float(p)
o=input('Give me a pitch class: ')
o1=float(o)
pitch=p1-4
octave=o1-9
freq=440*pow(2,(pitch+(octave/12)))
print(int(p1),' . ',int(o1),' equals ',freq)
print('Thanks for using my program')

