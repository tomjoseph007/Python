from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def filter_negative_sentences(text):
    # Initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Split the text into sentences
    sentences = text.split(' ')
    
    # Filter sentences with non-negative sentiment
    filtered_sentences = [
        sentence.strip() for sentence in sentences
        
        if analyzer.polarity_scores(sentence)['compound'] >= 0
    ]

    removed_words = [
        sentence.strip() for sentence in sentences
        if analyzer.polarity_scores(sentence)['compound'] < 0
    ]
    
    # Join the filtered sentences back into a single text
    filtered_text = ' '.join(filtered_sentences)
    
    return filtered_text, removed_words

# Example usage
text = ("I hate this terrible and disgusting day. "
        "It is so bad and awful! "
        "I really enjoy the sunny weather. "
        "The food was great today."
        "we are all dick and ass")

filtered_text, removed_words = filter_negative_sentences(text)
print("Original Text:", text)
print("Filtered Text:", filtered_text)
print("Removed words:", removed_words)
