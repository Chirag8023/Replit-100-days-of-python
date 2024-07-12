print(''' Generation Identifier''')

gen = int ( input ('Which year you were born?: '))

if gen > 1996 and gen < 2013:
 print( 'You are a Gen Z')
elif gen >= 1980 and gen <= 1996:
 print ('You are a Millenial')
elif gen >= 2013:
 print('You are a Gen Alpha')
else:
 print ("Input correct age")