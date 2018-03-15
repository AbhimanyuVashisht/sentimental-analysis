from aylienapiclient import textapi

client = textapi.Client("fdbff911", "1e688502a577d490966a666a8d3bf46f")


def classify_review(review):
    sentiment = client.Sentiment({'text': review})
    return sentiment['polarity']
