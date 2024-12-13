import csv

def parse_tokens_tagged(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Article Number', 'Token', 'Tag'])  # Write header

        article_number = None
        for line in infile:
            line = line.strip()
            if line.startswith("Article"):
                # Extract article number
                article_number = line.split(':')[0].replace("Article", "").strip()
            elif line:
                # Split token/tag pairs and write them
                token_tag_pairs = line.split()
                for pair in token_tag_pairs:
                    if '/' in pair:
                        token, tag = pair.rsplit('/', 1)
                        csv_writer.writerow([article_number, token, tag])

if __name__ == "__main__":
    input_file = 'tokens_tagged.pos'  # Replace with your actual file name
    output_file = 'test.csv'  # Output file name
    parse_tokens_tagged(input_file, output_file)
    print(f"Conversion complete. Output written to {output_file}")