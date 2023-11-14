phrase = 'aaaooo'

i = 0
qty_appeared_more_times = 0
lyrics_appeared_more_times = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1
        continue

    qty_appeared_more_times_current = phrase.count(current_letter)

    if qty_appeared_more_times < qty_appeared_more_times_current:
        qty_appeared_more_times = qty_appeared_more_times_current
        lyrics_appeared_more_times = current_letter

    i += 1

print(
    'The letter that appeared most often was '
    f'"{lyrics_appeared_more_times}" that appeared '
    f'{qty_appeared_more_times}x'
)