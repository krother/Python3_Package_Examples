from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

print(s.polarity_scores("today is a great day to code!"))
print(s.polarity_scores("syntax errors really suck"))
