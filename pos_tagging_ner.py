import pandas as pd
from flair.data import Sentence
from flair.models import SequenceTagger

def pos_and_ner(input_file, output_file):
    try:
        # Load the input file
        df = pd.read_csv(input_file)
        tagger_pos = SequenceTagger.load("flair/pos-english")
        tagger_ner = SequenceTagger.load("flair/ner-english")

        pos_ner_combined = []

        for _, row in df.iterrows():
            tokenized_sentences = eval(row["tokenized_sentences"])
            combined_data = []

            for sentence in tokenized_sentences:
                flair_sentence = Sentence(" ".join(sentence))

                # Perform POS tagging
                tagger_pos.predict(flair_sentence)
                pos_tags = [(token.text, token.get_tag("pos").value) for token in flair_sentence]

                # Perform NER
                tagger_ner.predict(flair_sentence)
                ner_tags = [(token.text, token.get_tag("ner").value) for token in flair_sentence]

                combined_data.append({"pos_tags": pos_tags, "ner_tags": ner_tags})

            pos_ner_combined.append(combined_data)

        df["pos_ner_combined"] = pos_ner_combined
        df.to_csv(output_file, index=False)
        print(f"Combined POS tagging and NER complete. Output written to {output_file}")
    except Exception as e:
        print(f"Error during combined POS and NER: {e}")

input_file = "sentence_split_and_tokenized.csv"
output_file = "pos_tagged_output_with_ner.csv"

pos_and_ner(input_file, output_file)
