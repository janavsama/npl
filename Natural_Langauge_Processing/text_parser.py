from collections import Counter
import string
from text_class import Textastic
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def text_parser(filename):
    """Parse text from a file, removing punctuation, counting word occurrences,
    and performing sentiment analysis."""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        words = Textastic._load_stop_words(words)
        word_count = Counter(words)
        total_word_count = sum(word_count.values())

        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(text)

    output = {
        'Article Context': filename,
        'Total word count': total_word_count,
        'Sentiment score': sentiment_scores,
        'Word count by word': word_count,
    }
    print(output)
    return {'word_count': word_count, 'sentiment_scores': sentiment_scores}
