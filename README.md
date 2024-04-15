# Celeb_Sentiment_Analysis
 
## Project Completed: 12/4/2024

# Project Description: 
- Developed machine learning pipelines with pre-processing, utilizing a Twitter dataset labelled for positive/negative sentiment.
- Employed trained NLP models, including Naive Bayes Classifier & Support Vector Machines, to identify celebrities with the highest percentage of positive tweets referencing them.
- Implemented advanced hyperparameter tuning techniques to optimize model performance and enhance generalization.


Crucial Note for this project! (celeb_df and twitter_df)
# 0 = Negative Tweet
# 1 = Positive Tweet

# List of Celebreties:
Fifteen celebrities were chosen to include a mixture of individuals associated with controversy in headlines or currently trending on social media, as well as celebrities with both positive and negative reputations for contrast:

Donald Trump 
Joe Biden 
Anthony Albanese 
Harley Reid 
Miley Cyrus 
Jake Paul 
Taylor Swift 
Lebron James 
Billie Eilish 
Kim Kardashian 
Christiano Ronaldo 
Jimmy Kimmel 
Elon Musk 
Andrew Tate 
Dwayne Johnson 


## Dataset (twitter.csv modified from:)
https://www.kaggle.com/datasets/kazanova/sentiment140

## Project navigation
Celebrity Data
    celeb_data.py - Contains the raw data, of each celebrity's 50 most recent tweets.
    celeb_predit.csv - Updated celeb_tweets.csv file with addition of NB,SVM predictions for side by side comparison.

CSV_files
    celeb_tweets.csv - 50 Tweets x 15 Celebrities
    twitter.csv - 40k Samples: twitter account and tweet used for training ML models.

ml_workflow.ipynb - Model building and training for NB and SVM, includes preprocessing, hyperparameter tuning, evaluation and visualisations.
preprocess.py - Initial preprocessing to convert raw data from celeb_data.py into structured csv file + Simplification of twitter.csv.