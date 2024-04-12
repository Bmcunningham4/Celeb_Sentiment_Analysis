import pandas as pd
import random
from Celebrity_Data.celeb_data import extract_tweets, Donald_Trump, Joe_Biden, Anthony_Albanese, Harley_Reid, Miley_Cyrus, Jake_Paul, Taylor_Swift, Lebron_James, Billie_Eilish, Kim_Kardashian, Cristiano_Ronaldo, Jimmy_Kimmel, Elon_Musk, Andrew_Tate, Dwayne_Johnson

#! Twitter data 
# Deleted original dataset to large to store! (1.6 Million samples -> 40k)
"""df = pd.read_csv("twitter_data.csv")
new_columns = random.sample(range(df.shape[0]), 40000) # 40k try that on for size ay
shorter_df = df.iloc[new_columns]
shorter_df.to_csv("twitter.csv", index=False)
"""
twitter_df = pd.read_csv("CSV_files/twitter.csv")

#? Giving Column names
col_names = ['Target', "id's", "Timestamp", "Query", "Account_name", "Tweet"]
twitter_df.columns = col_names

#? Removing Columns
twitter_df.drop(["id's", "Timestamp", "Query", "Account_name"], axis=1, inplace=True)

#? Changing target variable values (0 = Negative, 1 = Positive) -- Dataset doesn't contain neutral tweets
twitter_df.replace({4:1}, inplace=True)


#! Celebrety Data
celeb_dict = {
    Donald_Trump: [2, "Donald Trump"], 
    Joe_Biden: [2, "Joe Biden"], 
    Anthony_Albanese: [3, "Anthony Albanese"], 
    Harley_Reid: [2, "Harley Reid"], 
    Miley_Cyrus: [2, "Myley Cyrus"], 
    Jake_Paul: [4, "Jake Paul"], 
    Taylor_Swift: [4, "Taylor Swift"], 
    Lebron_James: [4, "Lebron James"], 
    Billie_Eilish: [2, "Billie Eilish"], 
    Kim_Kardashian: [2, "Kim Kardashian"], 
    Cristiano_Ronaldo: [4, "Cristiano Ronaldo"], 
    Jimmy_Kimmel: [2, "Jimmy Kimmel"], 
    Elon_Musk: [2, "Elon Musk"], 
    Andrew_Tate: [2, "Andrew Tate"], 
    Dwayne_Johnson: [2,  "Dwayne Johnson"]
      }

#? Creating new df that stores tweets regarding each celebrety
new_data = []

for name, num in celeb_dict.items():
    tweets = extract_tweets(name, num[0])

    for tweet in tweets:
        df_format = [num[1], tweet[0], tweet[1]]
        new_data.append(df_format)

celeb_df = pd.DataFrame(new_data, columns=["Celebrity", "Twitter_Account", "Tweet"])
celeb_df.to_csv('CSV_files/celeb_tweets.csv', index=False)
    # print(len(tweets)) - Checked all equal