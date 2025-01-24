import re

phoneNumber_Regex = re.compile(r'(\d{3})(-)?(\d{3})(-)?(\d{4})')
mo = phoneNumber_Regex.search(input('Enter a phone number: '))

if mo:
    print('Phone number found: ' + mo.group(0))
    # Verification
    if mo.group(2) and mo.group(4):
        print(f'Phone number: {mo.group(1)}-{mo.group(3)}-{mo.group(5)}')

    else:
        print(f'Phone number: {mo.group(1)} {mo.group(3)} {mo.group(5)}')
else:
    print('No phone number found.')
