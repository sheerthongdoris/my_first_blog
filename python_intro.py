print("Hello, Django girls.")
if(3 > 2):
    print('It s works!')
name ='Sonja'
if name == 'sonja':
    print('Hey sonja')
elif name =='Sonja':
    print('Hey Sonja')
else:
    print('Hey anonymous!')

def hi():
    print('Hi there!')
    print('How are you ?')

hi()

def hi(name):
    print('Hi ' + name + ' !') 
hi('Ola')

girls=['Rechel','Monica','Phebe','Ola','You']
for name in girls:
    hi(name)
    print('next girl')