from string import punctuation

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

input_text = input('Введите текст ').lower()

for p in punctuation:
    if p in input_text:
        input_text = input_text.replace(p, ' ')

word_list = input_text.split()

max_len = 0
count_dict = {}
for word in word_list:
    if len(word) > max_len:
        longest = word
        max_len = len(word)
    if count_dict.get(word, None):
        count_dict[word] += 1
    else:
        count_dict[word] = 1

letter_count = 0
for letter in input_text:
    if letter in vowels:
        letter_count += 1

print(f'1. В введенном тексте {len(word_list)} слов')

print(f'2.а) Самое длинное слово: {longest}')

print(f'2.б) Через max {max(word_list, key=len)}')

print(f'3. Содержит {letter_count} гласных')

print(f'4. Словарь повторений {count_dict}')
