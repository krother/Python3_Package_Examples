from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

texta = "today is a great day to code!"
textb = "syntax errors really suck"

print(texta, s.polarity_scores(texta))
print(textb, s.polarity_scores(textb))
