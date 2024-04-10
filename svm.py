import pandas as pd
import matplotlib.pyplot as plt
from preprocess import twitter_df
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC



celeb_df = pd.read_csv("celeb_predict.csv")

#? Remove punct/ numbers / capitals from tweets!!
twitter_df["Tweet"] = twitter_df["Tweet"].str.replace("'", "", regex=True).str.replace(r"[^a-zA-Z']", " ", regex=True).str.lower()
celeb_df["Tweet"] = celeb_df["Tweet"].str.replace("'", "", regex=True).str.replace(r"[^a-zA-Z']", " ", regex=True).str.lower()
print() 

#? Split data into train and test sets
X = twitter_df.Tweet
y = twitter_df.Target
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=303)

#? Count Vectorizer thingo
counter = CountVectorizer(ngram_range=(1,3))
x_train_counts = counter.fit_transform(x_train)
x_test_counts = counter.transform(x_test)

#? Train LinearSVC model....
classifier = LinearSVC(dual=True)
classifier.fit(x_train_counts, y_train)

accuracy = classifier.score(x_test_counts, y_test)
print(accuracy)

#? Predicting Celebrety data now!
celeb_counts = counter.transform(celeb_df.Tweet)
predictions = classifier.predict(celeb_counts)

celeb_df["SVM_Predict"] = predictions
celeb_df.to_csv("celeb_predict.csv")
celeb_target_counts = celeb_df.groupby("Celebrity")["SVM_Predict"].value_counts()
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




