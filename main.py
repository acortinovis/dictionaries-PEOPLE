#Make 3 dictionaries representing different people (their firstname, lastname, and phone number) 
#and store all three dictionaries in a list called "people".
#Loop through your list of people, printing everything you know about each person. Make sure the final output is nicely formatted and neat.

mrossi={
    'first':'Mario',
    'last':'Rossi',
    'phone':'3847984574',
}
rbianchi={
    'first':'Roby',
    'last':'Bianchi',
    'phone':'9847593757',
}

simberti={
    'first':'Simone',
    'last':'Imberti',
    'phone':'2183475030',
}

people=[mrossi,rbianchi,simberti]
counter=1
for person in people:
    print('')
    print(f'person number {counter} informations: ')
    counter+=1
    print(f'first name: {person['first']}')
    print(f'last name: {person['last']}')
    print(f'phone number: {person['phone']}')