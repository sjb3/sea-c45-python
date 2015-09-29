f = open('/Users/sungjbyun/python2/sea-c45-python/hw/hw13/sherlock.txt', 'r')

count = {}

for line in f:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()
keys.sort()

# save the word count analysis to a file
out = open('sherlock.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'sherlock' appears " + str(count['sherlock']) + " times in the book.")




