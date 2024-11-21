import pandas as pd
import nltk
from nltk import pos_tag

# Tags parts of speech for each tokenized sentence
def tag_pos(tokenized_sentences):
    return [pos_tag(sentence) for sentence in tokenized_sentences]

# Reads CSV, performs POS tagging, writes output
def process_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        if "tokenized_sentences" not in df.columns:
            print("Error: 'tokenized_sentences' column not found in input file.")
            return

        df["tokenized_sentences"] = df["tokenized_sentences"].apply(eval)
        df["pos_tagged_sentences"] = df["tokenized_sentences"].apply(tag_pos)
        df.to_csv(output_file, index=False)
        print(f"POS tagging completed. Output written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output files
input_file = "sentence_split_and_tokenized.csv"
output_file = "pos_tagged_output_final.csv"

process_csv(input_file, output_file)
