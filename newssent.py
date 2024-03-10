# Import libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary resources (run only the first time)
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text, keywords):
  """
  Analyzes the sentiment of a press release text and identifies keywords.

  Args:
      text: The text of the press release.
      keywords: A dictionary where keys are categories and values are lists of keywords.

  Returns:
      A dictionary containing sentiment scores (compound, positive, neutral, negative)
      and a list of identified keywords with their categories.
  """
  scores = analyzer.polarity_scores(text)
  identified_keywords = []

  # Loop through categories and keywords
  for category, keyword_list in keywords.items():
    for keyword in keyword_list:
      if keyword.lower() in text.lower():
        identified_keywords.append((category, keyword))

  return scores, identified_keywords

def main():
  """
  Prompts user for press release text and performs analysis.
  """
  # Get press release text from user
  press_release_text = input("Enter the press release text: ")

  keywords = {
    "Financial Performance": ["earnings", "revenue", "profit"],
    "Expansion": ["expand", "growth", "market"],
    "FDA": ["approval", "clearance", "grant"],
  }

  sentiment_scores, identified_keywords = analyze_sentiment(press_release_text, keywords)

  print("Sentiment Scores:")
  print(sentiment_scores)

  print("Identified Keywords:")
  for category, keyword in identified_keywords:
    print(f"- {category}: {keyword}")

if __name__ == "__main__":
  main()
