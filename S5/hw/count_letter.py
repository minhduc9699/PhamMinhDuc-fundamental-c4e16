letter_input = input('enter a sentence: ').lower()
letter_input = letter_input.replace(' ', '')
letter_count = {}

for letter in letter_input:
    letter_count[letter] = letter_input.count(letter)

letter_item = list(letter_count.items())
letter_item.sort()

letter_item = dict(letter_item)

for key, value in letter_item.items():
    print(key, value)
