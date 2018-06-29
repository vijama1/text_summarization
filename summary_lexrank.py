from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
 #We're choosing Lexrank, other algorithms are also built in
from sumy.parsers.html import HtmlParser
LANGUAGE = "english"
# file = "plain_text.txt" #name of the plain-text file
# parser = PlaintextParser.from_file(file, Tokenizer("english"))
url = "https://rare-technologies.com/text-summarization-in-python-extractive-vs-abstractive-techniques-revisited/"
parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 10) #Summarize the document with 5 sentences

for sentence in summary:
    print(sentence)
