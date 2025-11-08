import re
import string

class TextProcessor:
    def clean_text(self, text):
        if not text:
            return ""
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def extract_words(self, text):
        return text.split() if text else []

    def remove_stopwords(self, words, language='fr'):
        stopwords_fr = {
            'le','la','les','un','une','des','de','du','et','ou','mais','donc',
            'or','ni','car','que','qui','quoi','dont','où','dans','par','pour',
            'avec','sans','sur','sous','ce','cet','cette','ces','mon','ton',
            'son','ma','ta','sa','mes','tes','ses','notre','votre','leur','nos',
            'vos','leurs','je','tu','il','elle','nous','vous','ils','elles',
            'à','au','aux','est','sont','être','avoir'
        }
        return [w for w in words if w not in stopwords_fr]

    def get_word_frequency(self, words):
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        return frequency
