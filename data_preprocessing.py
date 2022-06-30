from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

arr = ["Car was cleaned by Jack",
	"Jack was cleaned by car."]

# If you want to take into account just term frequencies:
vectorizer = CountVectorizer(ngram_range=(2,2))
# The ngram range specifies your ngram configuration.

X = vectorizer.fit_transform(arr)
# Testing the ngram generation:
print(vectorizer.get_feature_names())

print(X.toarray())

## And now testing TFIDF vectorizer:
vectorizer = TfidfVectorizer(ngram_range=(2,2)) # You can still specify n-grams here.
X = vectorizer.fit_transform(arr)

# Testing the TFIDF value + ngrams:
print(X.toarray())

## Testing TFIDF vectorizer without normalization:
vectorizer = TfidfVectorizer(ngram_range=(2,2), norm=None) # You can still specify n-grams here.
X = vectorizer.fit_transform(arr)

# Testing TFIDF value before normalization:
print(X.toarray())
