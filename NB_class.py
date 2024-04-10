import pandas as pd
import matplotlib.pyplot as plt
from preprocess import twitter_df
# import re ---- Delete this at end if all ok but might need..

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#? ML ideas: Naive Bayes classifier, Support Vector machines .. (LDA for dimensionality reduction if I cbf)
print(twitter_df.head())
celeb_df = pd.read_csv("celeb_tweets.csv")

#? Remove punct/ numbers / capitals from tweets!!
twitter_df["Tweet"] = twitter_df["Tweet"].str.replace("'", "", regex=True).str.replace(r"[^a-zA-Z']", " ", regex=True).str.lower()
celeb_df["Tweet"] = celeb_df["Tweet"].str.replace("'", "", regex=True).str.replace(r"[^a-zA-Z']", " ", regex=True).str.lower()
print() 

#? Split data into train and test sets
X = twitter_df.Tweet
y = twitter_df.Target
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=303)

#? Making count vectorizer and fitting etc...
counter = CountVectorizer(ngram_range=(1,3)) #* Woahhh included bigram and trigram models!!
x_train_counts = counter.fit_transform(x_train)
x_test_counts = counter.transform(x_test)

#? Now we use MultinomialNB classifier 
classifier = MultinomialNB()
classifier.fit(x_train_counts, y_train)

x_test_counts = counter.transform(x_test)

#? Accuracy bby
accuracy = classifier.score(x_test_counts, y_test)
print(accuracy) # Not bad eh

# x_test_array = x_test_counts.toarray()
# print(x_test_array)
# print(counter.vocabulary_)

#? Predicting Celebrety data now!
celeb_counts = counter.transform(celeb_df.Tweet)
predictions = classifier.predict(celeb_counts)
# print(predictions) Yewwww that looks good now I just need to write to CSV file!

#? Rewriting to CSV with calcs
celeb_df["NB_Predict"] = predictions
celeb_df.to_csv("celeb_predict.csv")
celeb_target_counts = celeb_df.groupby("Celebrity")["NB_Predict"].value_counts()
print(celeb_target_counts)

#? Graphing!
positive_counts = celeb_target_counts.unstack().get(1, 0).sort_values() * 2 # So they are a percentage
negative_counts = 100 - positive_counts 
plt.bar(positive_counts.index, negative_counts, color='red')
plt.bar(positive_counts.index, positive_counts, bottom=negative_counts, color='blue')


plt.xlabel('Celebrity')
plt.ylabel('Percentage of Positive Tweets')
plt.title('Percentage of Positive Tweets for Each Celebrity')
plt.legend(['Negative', 'Positive'], loc='upper right')
plt.xticks(rotation=45, ha='right')
# plt.axhline(y=50, color='black', linestyle='--')
plt.grid(True)
plt.show()



#* Notes for ben to be aware of:
"""
Accuracy:
unigram - 0.757
bigram - 0.764
trigram - 0.765

# Perform hyperparameter tuning ----------------  Diff option to replace
param_grid = {'alpha': [0.1, 0.5, 1.0]}  # Define the grid of parameters to search
grid_search = GridSearchCV(MultinomialNB(), param_grid, cv=5)  # 5-fold cross-validation
grid_search.fit(x_train_counts, y_train)

# Print the best parameters found
print("Best parameters:", grid_search.best_params_)

# Train Multinomial Naive Bayes classifier with the best parameters
classifier = grid_search.best_estimator_
classifier.fit(x_train_counts, y_train)
---------------

"""