import pandas as pd

def generate_pos_based_headlines(input_file, output_file):
    """
    Generate headlines based on POS tagging only.
    """
    try:
        # Read input CSV
        df = pd.read_csv(input_file)
        if "tagged_sentences" not in df.columns:
            print("Error: Required column 'tagged_sentences' missing in input file.")
            return

        generated_headlines = []

        for _, row in df.iterrows():
            article_number = row["article_number"]
            tagged_sentences = eval(row["tagged_sentences"])

            # Collect significant words based on POS tags
            important_words = []
            for sentence in tagged_sentences:
                for token, pos in sentence:
                    if pos in {"NN", "VB", "JJ"}:  # Focus on nouns, verbs, and adjectives
                        important_words.append(token)

            # Create a concise headline
            headline = " ".join(important_words[:10])  # Limit to 10 words
            generated_headlines.append({
                "article_number": article_number,
                "generated_headline": headline
            })

        # Save to output file
        output_df = pd.DataFrame(generated_headlines)
        output_df.to_csv(output_file, index=False)
        print(f"POS-based headline generation complete. Output written to {output_file}")

    except Exception as e:
        print(f"Error generating POS-based headlines: {e}")

# File paths
input_file = "pos_tagged_output_final.csv"
output_file = "generated_headlines_pos.csv"

# Run the function
generate_pos_based_headlines(input_file, output_file)
