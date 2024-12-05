import pandas as pd
from flair.models import SequenceTagger
from flair.data import Sentence

def perform_pos_tagging(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        if "text" not in df.columns:
            print("Error: 'text' column missing in input file.")
            return

        tagger = SequenceTagger.load("pos")
        results = []

        for index, row in df.iterrows():
            text = row["text"]
            sentence = Sentence(text)
            tagger.predict(sentence)
            pos_tags = [(token.text, token.get_tag("pos").value) for token in sentence]
            results.append({"article_number": index, "text": text, "pos_tags": pos_tags})

        pos_df = pd.DataFrame(results)
        pos_df.to_csv(output_file, index=False)
        print(f"POS tagging complete. Output written to {output_file}.")
    except Exception as e:
        print(f"Error during POS tagging: {e}")

input_file = "subset_news_data.csv"
output_file = "pos_tagged_output.csv"
perform_pos_tagging(input_file, output_file)
