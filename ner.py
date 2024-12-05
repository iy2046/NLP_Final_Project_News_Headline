import pandas as pd
from flair.models import SequenceTagger
from flair.data import Sentence

def perform_ner(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        if "text" not in df.columns:
            print("Error: 'text' column missing in input file.")
            return

        tagger = SequenceTagger.load("ner")
        results = []

        for index, row in df.iterrows():
            text = row["text"]
            sentence = Sentence(text)
            tagger.predict(sentence)
            named_entities = [(entity.text, entity.tag) for entity in sentence.get_spans("ner")]
            results.append({"article_number": index, "text": text, "named_entities": named_entities})

        ner_df = pd.DataFrame(results)
        ner_df.to_csv(output_file, index=False)
        print(f"NER complete. Output written to {output_file}.")
    except Exception as e:
        print(f"Error during NER: {e}")

input_file = "subset_news_data.csv"
output_file = "ner_output.csv"
perform_ner(input_file, output_file)
