"""
split and join with list and str
split - splits a string (list)
join - joins a string
"""
phrase = 'Look at this, interesting thing'
raw_frases_list = phrase.split(',')

list_phrases = []
for i, phrase in enumerate(raw_frases_list):
    list_phrases.append(raw_frases_list[i].strip())

print(raw_frases_list)
print(list_phrases)
united_frases = ', '.join(list_phrases)
print(united_frases)