import codecs
import nltk.classify.util
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.classify import NaiveBayesClassifier
import pickle

tokenizer = RegexpTokenizer(r'\w+')

train_set = []
test_set = []


def create_word_feature(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


def pre_processing(filename, rev_set):
    with codecs.open(filename, "r", encoding='utf-8') as fp:
        for line in fp:
            rev_features = line.split(':')
            extracted_word = tokenizer.tokenize(rev_features[1])
            rev_set.append((create_word_feature(extracted_word), rev_features[0][9]))


def post_processing():
    pre_processing('data/train.ft.txt/data', train_set)
    pre_processing('data/train.ft.txt/data', test_set)
    classifier = NaiveBayesClassifier.train(train_set)
    f = open('sentimental_classifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()
    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print('Accuracy', accuracy)


def classify_rev(rev):
    f = open('sentimental_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    extracted_words = tokenizer.tokenize(rev)
    temp = create_word_feature(extracted_words)
    return classifier.classify(temp)


post_processing()
