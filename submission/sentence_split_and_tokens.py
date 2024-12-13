# @author Nick Yi
# NLP Final Project - Group 20

# Sentence Splitting and Tokenization
# Date: 11/19/2024

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

#splits article text into sentences; tokenizes each word in each sentence
#also handles NaN/non-string values that might come up in text
def process_article_text(article_text):

    #check if the text is valid
    if not isinstance(article_text, str):
        return []
    
    #split into sentences
    sentences = sent_tokenize(article_text)

    #tokenize each sentence
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    return tokenized_sentences

#reads a CSV file as input
#performs sentence splitting and tokenization on the article text
#write the output to a new CSV file
def process_csv(input_file, output_file):

    try:
        #read the input CSV file
        df = pd.read_csv(input_file)

        #rename columns (to match the expected names)
        df.rename(columns={"title": "article_title", "text": "article_text"}, inplace=True)

        #adding an article_number column when it does not exist
        #original data does not have this column
        if "article_number" not in df.columns:

            #using row index as article_number (so, the first sentence starts from 0)
            df["article_number"] = df.index

        #check if all required columns are here
        if "article_title" not in df.columns or "article_text" not in df.columns:
            print("Error: Missing required columns in the input CSV.")
            return

        #list to save processed data
        processed_data = []

        #process each row
        for index, row in df.iterrows():
            article_number = row["article_number"]
            article_title = row["article_title"]
            article_text = row["article_text"]

            #process the article text
            tokenized_data = process_article_text(article_text)

            #add processed information to the list
            processed_data.append({
                "article_number": article_number,
                "article_title": article_title,
                "tokenized_sentences": tokenized_data
            })

        #convert processed data into a DataFrame
        processed_df = pd.DataFrame(processed_data)

        #write the output to a new CSV file
        processed_df.to_csv(output_file, index=False)
        print(f"Output written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

#manage input and output file

# input_file = "training_news_articles.csv"
# output_file = "sentence_split_and_tokenized.csv"

# input_file = "development_news_articles.csv"
# output_file = "sentence_split_and_tokenized.csv"

input_file = "testing_news_articles.csv"
output_file = "sentence_split_and_tokenized.csv"

#program run
process_csv(input_file, output_file)