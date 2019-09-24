
whitelist = set('abcdefghijklmnopqrstuvwxyzæøå ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ')

def get_word_freqs(filename):
    words = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                word = ''.join(filter(whitelist.__contains__, word))
                word = word.lower()
                if word in words:
                    words[word] = words[word] + 1
                else:
                    words[word] = 1
    return words

def get_words_line(filename, s):
    lines = []
    line_counter = 1
    s = s.lower()
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                word = ''.join(filter(whitelist.__contains__, word))
                word = word.lower()
                if s == word and not line_counter in lines:
                    lines.append(line_counter)
            line_counter += 1
    return lines


my_list = get_word_freqs("pg5200.txt")
new_list = get_words_line("pg5200.txt", "metamorphosis")
print(new_list)
print(my_list)


