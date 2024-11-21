# @author: Golam Raiyan
# NLP Final Project - Group 20

# POS Tagging
# Date: 11/21/2024


import pandas as pd
from nltk import pos_tag
import ast  # To safely parse the nested string back into a list

# Function to apply POS tagging to tokenized sentences
def pos_tag_sentences(tokenized_sentences):
    if not tokenized_sentences:
        return []
    return [pos_tag(sentence) for sentence in tokenized_sentences]

# Reads a CSV file, performs POS tagging, and saves the output to a new file
def process_csv_with_pos_tagging(input_file, output_file):
    try:
        # Read the input CSV file
        df = pd.read_csv(input_file)

        # Ensure the required columns are present
        required_columns = ["article_number", "article_title", "tokenized_sentences"]
        if not all(col in df.columns for col in required_columns):
            print(f"Error: Input file is missing one or more required columns: {required_columns}")
            return

        # Process each row and perform POS tagging
        processed_data = []
        for index, row in df.iterrows():
            article_number = row["article_number"]
            article_title = row["article_title"]

            # Parse the tokenized sentences safely
            try:
                tokenized_sentences = ast.literal_eval(row["tokenized_sentences"])
            except Exception as e:
                print(f"Error parsing tokenized_sentences for article_number {article_number}: {e}")
                tokenized_sentences = []

            # Perform POS tagging on the tokenized sentences
            tagged_sentences = pos_tag_sentences(tokenized_sentences)

            # Append the processed data
            processed_data.append({
                "article_number": article_number,
                "article_title": article_title,
                "pos_tagged_sentences": tagged_sentences
            })

        # Convert processed data into a DataFrame
        processed_df = pd.DataFrame(processed_data)

        # Save the processed DataFrame to a new CSV file
        processed_df.to_csv(output_file, index=False)
        print(f"Processed data saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main script
if __name__ == "__main__":
    # Specify the input and output filenames
    input_file = "sentence_split_and_tokenized.csv"  # Input file from the tokenization step
    output_file = "pos_tagged_output_final.csv"  # Final output file with POS-tagged sentences

    # Run the processing function
    process_csv_with_pos_tagging(input_file, output_file)
