from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

# Assuming you have preprocessed text data in X and corresponding labels in y

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create CountVectorizer and transform the text data into feature vectors
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train a LinearSVC model
svm_classifier = LinearSVC()
svm_classifier.fit(X_train_counts, y_train)

# Evaluate the model
accuracy = svm_classifier.score(X_test_counts, y_test)
print("Accuracy:", accuracy)