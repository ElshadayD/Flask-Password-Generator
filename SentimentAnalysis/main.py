import nltk
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Download NLTK data (if not already downloaded)
nltk.download("movie_reviews")
nltk.download("stopwords")

# Load movie reviews dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)

# Define stop words
stop_words = set(stopwords.words('english'))

# Preprocess the data
all_words = []
for w in movie_reviews.words():
    if w.lower() not in stop_words and w.isalpha():
        all_words.append(w.lower())

# Create a frequency distribution of words
all_words_freq = FreqDist(all_words)

# Select the most frequent words as features
word_features = list(all_words_freq.keys())[:3000]

# Define a function to extract features from a document
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[f'contains({word})'] = (word in document_words)
    return features

# Extract features from the documents
featuresets = [(document_features(d), c) for (d,c) in documents]

# Split the data into training and testing sets
train_set, test_set = train_test_split(featuresets, test_size=0.25, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.train(train_set)

# Make predictions on the test set
predictions = [classifier.classify(test[0]) for test in test_set]

# Calculate accuracy
accuracy = accuracy_score([test[1] for test in test_set], predictions)
print(f"Accuracy: {accuracy:.2f}")

