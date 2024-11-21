import pandas as pd

# Generates a headline from POS-tagged sentences
def generate_headline(pos_tagged_sentences):
    try:
        nouns_and_verbs = [word for sentence in pos_tagged_sentences 
                           for word, tag in sentence if tag.startswith("NN") or tag.startswith("VB")]
        return " ".join(nouns_and_verbs[:10])  # Limit to 10 words for brevity
    except Exception:
        return ""

# Reads CSV, generates headlines, writes output
def process_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        if "pos_tagged_sentences" not in df.columns:
            print("Error: 'pos_tagged_sentences' column not found in input file.")
            return

        df["pos_tagged_sentences"] = df["pos_tagged_sentences"].apply(eval)
        df["generated_headline"] = df["pos_tagged_sentences"].apply(generate_headline)
        df.to_csv(output_file, index=False)
        print(f"Headline generation completed. Output written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output files
input_file = "pos_tagged_output_final.csv"
output_file = "headlines_generated_final.csv"

process_csv(input_file, output_file)
