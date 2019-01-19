 # Sentiment Analysis Module - Natural Language Processing With Python and NLTK p.19

 # Now that we've got a more reliable classifier, we're ready to push forward. Here, we cover how we can convert our classifier training script to an actual sentiment analysis module.

 # We pickle everything, and create a new sentiment function, which, with a parameter of "Text" will perform a classification and return the result.

 # By pickling everything, we find that we can load this module in seconds, rather than the prior 3-5 minutes. After this, we're ready to apply this module to a live Twitter stream.

import pickle
from nltk.classify import ClassifierI
from statistics import mode, StatisticsError
from nltk.tokenize import word_tokenize

# new code
class VoteClassifier(ClassifierI):

    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        try:
            most_common_vote = mode(votes)
            return most_common_vote
        except StatisticsError:
            print ('No unique mode found, returning 1st vote')
            # TODO if no unique mode, see if classifiers with highest and second highest
            # accuracy agree. if so do that. if not, just use highest accuracy classifier
            return votes[0]

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        try:
            most_common_vote = mode(votes)
            choice_votes = votes.count(mode(votes))
            conf = choice_votes / len(votes)
            return conf
        except StatisticsError:
            print ('No unique mode found')
            return .50

def find_features(document, word_features):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

def sentiment(text):
    word_features5k_f = open("pickled_algos/word_features.pickle", "rb")
    word_features = pickle.load(word_features5k_f)
    word_features5k_f.close()
    feats = find_features(text, word_features)

    open_file = open("pickled_algos/NB_Classifier.pickle", "rb")
    NB_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/MNB_Classifier.pickle", "rb")
    MNB_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/BNB_Classifier.pickle", "rb")
    BNB_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/SGD_Classifier1.pickle", "rb")
    SGD_Classifier1 = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/SGD_Classifier2.pickle", "rb")
    SGD_Classifier2 = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/Ridge_Classifier.pickle", "rb")
    Ridge_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/Perceptron_Classifier.pickle", "rb")
    Perceptron_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/NuSVC_Classifier.pickle", "rb")
    NuSVC_Classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/Passive_Aggressive_classifier.pickle", "rb")
    Passive_Aggressive_classifier = pickle.load(open_file)
    open_file.close()

    open_file = open("pickled_algos/kNN_Classifier.pickle", "rb")
    kNN_Classifier = pickle.load(open_file)
    open_file.close()

    voted_classifier = VoteClassifier(NB_Classifier,
                                      MNB_Classifier,
                                      BNB_Classifier,
                                      SGD_Classifier1,
                                      SGD_Classifier2,
                                      Ridge_Classifier,
                                      Perceptron_Classifier,
                                      NuSVC_Classifier,
                                      Passive_Aggressive_classifier,
                                      kNN_Classifier)

    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

