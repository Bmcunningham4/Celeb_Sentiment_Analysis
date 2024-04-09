import pandas as pd
import re
from preprocess import twitter_df

from sklearn.feature_extraction.text import CountVectorizer

#? ML ideas: Naive Bayes classifier, Support Vector machines .. (LDA for dimensionality reduction if I cbf)
print(twitter_df.head())
celeb_df = pd.read_csv("celeb_tweets.csv")

#? Remove punct/ numbers / capitals from tweets!!
twitter_df["Tweet"] = twitter_df["Tweet"].str.replace(r"[^a-zA-Z']", " ", regex=True).str.replace("'", "", regex=True).str.lower()
celeb_df["Tweet"] = celeb_df["Tweet"].str.replace(r"[^a-zA-Z']", " ", regex=True).str.replace("'", "", regex=True).str.lower()



#? Making count vectorizer...
counter = CountVectorizer() 


print() #todo: Have a look over that example when I'm back made some progress don't start from scratch again..