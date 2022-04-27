import nltk
import collections


def basic_seo_analysis(sometext):
    count_of_symbols = len(sometext)
    count_of_symbols_without_spaces = len(sometext.replace(' ', ''))
    count_of_words = len(sometext.split())

    token = nltk.word_tokenize(sometext)
    punctuation = ['.', ',', ':', ';', '...', '!', '?', '-', '"', '(', ')', '*', '/', ]
    token_without_punc = []
    punc_from_token = []

    for elem in token:
        if elem not in punctuation:
            token_without_punc.append(elem)
        else:
            punc_from_token.append(elem)

    dict_token = collections.Counter(token_without_punc)

    once_met_word = 0
    for elem in dict_token.values():
        if elem == 1:
            once_met_word += 1
    # once met word
    stopwords = nltk.corpus.stopwords.words('english') + nltk.corpus.stopwords.words('russian')
    stack_of_stopwords = []
    for x in token:
        if x in stopwords:
            stack_of_stopwords.append(x)

    count_of_stopwords = len(stack_of_stopwords)

    water = round(float((count_of_stopwords / len(token_without_punc)) * 100), 2)
    td = collections.Counter(token_without_punc)
    countofmostpopular = float(max(td.values()))

    output = open('out.txt', 'w')
    output.write(
        "Количество символов: " + str(count_of_symbols) +'\n'+
        "Количество символов без пробелов: " + str(count_of_symbols_without_spaces) + '\n' +
        "Количество слов: " + str(count_of_words) + '\n' +
        "Количество уникальных слов: " + str(once_met_word) + '\n' +
        "Количество стоп-слов: " + str(count_of_stopwords) + '\n' +
        "Вода: " + str(water) + ' %'+'\n' +
        "Классическая тошнота документа: " + str((round(countofmostpopular**0.5, 3))) + '\n\n'

    )
    output.close()
    pass


def semantic_kernel(sometext):
    token = nltk.word_tokenize(sometext)
    punctuation = ['``',"''",'.', ',', ':', ';', '...', '!', '?', '-', '"', '(', ')', '*', '/', ]
    token_without_punc = []
    stopwords = nltk.corpus.stopwords.words('english') + nltk.corpus.stopwords.words('russian')

    for elem in token:
        if elem not in punctuation:
            if elem not in stopwords:
                token_without_punc.append(elem)
    stemmer = nltk.stem.PorterStemmer()
    stemmed_token = []
    for word in token_without_punc:
        stemmed_token.append(stemmer.stem(word))


    dict_token = collections.Counter(stemmed_token)
    dict_token = collections.OrderedDict(dict_token.most_common())
    file = open('out.txt', 'a')
    i = 1
    for key, value in dict_token.items():
        if value != 1:
            file.write(
                str(i) + '. ' + str(key) + '    ' +str(value) + '\n'
            )

            i +=1

    file.close()
    pass


def stop_words(sometext):
    token = nltk.word_tokenize(sometext)
    stopwords = nltk.corpus.stopwords.words('english') + nltk.corpus.stopwords.words('russian')
    only_stop = []
    for elem in token:
        if elem in stopwords:
            only_stop.append(elem)

    dict_stop = collections.Counter(only_stop)
    dict_stop = collections.OrderedDict(dict_stop.most_common())


    file = open('out.txt', 'a')
    file.write("\nСТОП СЛОВА И ИХ КОЛИЧЕСТВО В ТЕКСТЕ\n")
    i = 1
    for key, value in dict_stop.items():
        file.write(
            str(i) + '. ' + str(key) + '    ' + str(value) + '\n'
        )

        i += 1

    file.close()
    pass


file = open('Война и мир.txt', 'r' )
text = file.read()

basic_seo_analysis(text)
print(type(text))
print(len(text.split()))
t = nltk.word_tokenize(text)
td = collections.Counter(t)
print(td)
print(max(td.values()))
print(4**0.5)
semantic_kernel(text)
stop_words(text)








