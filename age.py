driving = input('Have you drive: ')
age = input('How old are you: ')
age = int(age)
if driving == 'YES':
    if age >= 18:
        print('You pass the test.')
    else:
        print('How dare you.')
elif driving == 'NO':
    if age >= 18:
        print('Why don\'t you get the lisence?')
    else:
        print('Wait for you grow up.')
else:
    print('Enter the YES or NO.')