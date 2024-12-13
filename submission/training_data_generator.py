import csv

def generate_training_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Article Number', 'Article Title', 'Token', 'Tag'])  # Write header

        article_number = None
        article_title = None
        for line in infile:
            line = line.strip()
            if line.startswith("Article"):
                # Extract article number and title
                parts = line.split(':', 1)
                article_number = parts[0].replace("Article", "").strip()
                article_title = parts[1].strip() if len(parts) > 1 else None
            elif line:
                # Split token/tag pairs and write them
                token_tag_pairs = line.split()
                for pair in token_tag_pairs:
                    if '/' in pair:
                        token, tag = pair.rsplit('/', 1)
                        csv_writer.writerow([article_number, article_title, token, tag])

if __name__ == "__main__":
    input_file = 'tokens_tagged.pos'  # Replace with your actual file name
    output_file = 'training.csv'  # Output file name
    # output_file = 'testing_for_eval.csv'
    generate_training_data(input_file, output_file)
    print(f"Training data generated successfully. Output written to {output_file}")
