import re

vowels = ('а, е, ё, и, о, у, ы, э, ю, я')

input_text = input('Введите текст ').lower()

clean_text = re.sub(r'[^\w\s]', '', input_text)

print(f'В введенном тексте {len(clean_text.split())} слов')

# print(str(clean_text))
# print(clean_text.split())

word_len_list = []
for word in clean_text.split():
    word_len_list.append(len(word))

print(max(word_len_list))
print(max(clean_text.split()))
