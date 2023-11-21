# Exercise - question and answer system


questions = [
    {
        'Question': 'What is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Response': '4',
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Response': '25',
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Response': '5',
    },
]

qty_hits = 0
for question in questions:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    choice = input('Choose an option: ')

    got_it_right = False
    choice_int = None
    qty_options = len(options)

    if choice.isdigit():
        int_choice = int(choice)

    if int_choice is not None:
        if int_choice >= 0 and int_choice < qty_options:
            if options[int_choice] == question['Response']:
                got_it_right = True

    print()
    if got_it_right:
        qty_hits += 1
        print('You got it right 👍')
    else:
        print('Error ❌')

    print()


print('You got it right', qty_hits)
print('de', len(questions), 'questions.')