#importing necessary modules
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import time

#which language to choose
LANGUAGE = "english"
#here sentence count represent number of sentences in the summary
SENTENCES_COUNT = 10


if __name__ == "__main__":
    #url from where we need to summarize
    url = "https://rare-technologies.com/text-summarization-in-python-extractive-vs-abstractive-techniques-revisited/"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    #print(parser)
    # or for plain text files
    #parser = PlaintextParser.from_file("/tmp/mozilla_ezioauditore0/SampleTextFile_200kb.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    # print(stemmer)
    # print(parser.document)

    summarizer = Summarizer(stemmer)
    #print(summarizer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    #print(summarizer.stop_words)
    #print(summarizer(parser.document, SENTENCES_COUNT))
    #time.sleep(5)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
