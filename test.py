fname = input('enter your file name with extension')


def openfile(file_name):
    try:
        file = open(file_name)
        print('file opened')
    except:
        file = open('words.txt')
        print('file not found - default opened instead')
    return file


opened_file = openfile(fname)
di = dict()
wds = []
for line in opened_file:
    line = line.strip()
    wds.extend(line.split())
for word in wds:
    di[word] = di.get(word, 0)+1

print(di)


def find_most_common_word(dictionary):
    largest = -1
    most_common_word = None

    for k, v in dictionary.items():
        if v > largest:
            largest = v
            most_common_word = k

    print('\"', most_common_word, '\"', 'appears', largest, 'times in the text')

find_most_common_word(di)
def number_unique_words(dictionary):
    return len(dictionary)

def word_count(wds):
    return len(wds)

print(number_unique_words(di), 'unique words used in the book')


