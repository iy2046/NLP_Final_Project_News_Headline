# @author Nick Yi
# NLP Final Project - Group 20

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

# Splits article text into sentences; tokenizes each word in each sentence
def process_article_text(article_text):
    if not isinstance(article_text, str):
        return []
    sentences = sent_tokenize(article_text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    return tokenized_sentences

# Reads a CSV file, performs sentence splitting and tokenization, writes output
def process_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df.rename(columns={"title": "article_title", "text": "article_text"}, inplace=True)

        if "article_number" not in df.columns:
            df["article_number"] = df.index

        if "article_title" not in df.columns or "article_text" not in df.columns:
            print("Error: Missing required columns in the input CSV.")
            return

        processed_data = []
        for index, row in df.iterrows():
            article_number = row["article_number"]
            article_title = row["article_title"]
            article_text = row["article_text"]
            tokenized_data = process_article_text(article_text)
            processed_data.append({
                "article_number": article_number,
                "article_title": article_title,
                "tokenized_sentences": tokenized_data
            })

        processed_df = pd.DataFrame(processed_data)
        processed_df.to_csv(output_file, index=False)
        print(f"Output written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output files
input_file = "subset_news_data.csv"
output_file = "sentence_split_and_tokenized.csv"

process_csv(input_file, output_file)
