MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 22

f = open('dictionary.txt', 'r')

words = []
for line in f:
    valid = True
    cap_line = line.upper()
    for l in cap_line:
        # filter out special characters
        # make sure right size + 1 because of new line
        if len(cap_line) > MAX_WORD_LENGTH + 1 or len(cap_line) <= MIN_WORD_LENGTH:
            valid = False
        else:
            if ((ord(l) < 65 or ord(l) > 90) and ord(l) != 10):
                valid = False

    if valid:
        # make sure to not get endline character
        words.append(cap_line[0:len(cap_line) - 1])

# write to word bank
words_file = open('words.txt', 'w')

for i in range(0, len(words)):
    words_file.write(words[i] + '\n')

words_file.close()
f.close()
