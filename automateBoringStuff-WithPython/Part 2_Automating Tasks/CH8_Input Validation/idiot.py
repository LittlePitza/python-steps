import pyinputplus as pyiip

while True:
    prompt = 'What to know how keep an idiot busy for hours?\nAswered: '
    response = pyiip.inputYesNo(prompt)
    if response == 'no':
        print('Thank you, Have a nice day :)')
        break
