import csv
import spacy

# Load spaCy's NER model
nlp = spacy.load("en_core_web_sm")

def load_training_data(file_path):
    """Loads training data and organizes it by Article Number."""
    training_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            article_number = int(row['Article Number'])
            if article_number not in training_data:
                training_data[article_number] = {'title': row.get('Article Title'), 'tokens': []}
            training_data[article_number]['tokens'].append((row['Token'], row['Tag']))
    return training_data

def generate_headline(entities, title=None):
    """Generates a headline based on entities and optional training title."""
    key_entities = [ent.text for ent in entities if ent.label_ in ['PERSON', 'ORG', 'GPE', 'NORP']]
    headline = " ".join(key_entities[:5])  # Use the first 5 key entities.
    if title:
        # return f"{headline} - Inspired by: {title}"
        return f"{headline}"
    return headline

def process_articles(input_file, output_file, training_titles=None):
    """Processes articles to generate headlines."""
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Article Number', 'Generated Headline'])

        current_article = None
        tokens = []
        for row in reader:
            article_number = int(row['Article Number'])
            if current_article is None:
                current_article = article_number

            if article_number != current_article:
                # Process the previous article
                text = " ".join(token for token, _ in tokens)
                doc = nlp(text)
                headline = generate_headline(doc.ents, training_titles.get(current_article) if training_titles else None)
                writer.writerow([current_article, headline])

                # Reset for the new article
                current_article = article_number
                tokens = []

            tokens.append((row['Token'], row['Tag']))

        # Process the last article
        if tokens:
            text = " ".join(token for token, _ in tokens)
            doc = nlp(text)
            headline = generate_headline(doc.ents, training_titles.get(current_article) if training_titles else None)
            writer.writerow([current_article, headline])

if __name__ == "__main__":
    training_file = 'training.csv'
    input_file = 'test.csv'  # Replace with 'test.csv' for testing
    output_file = 'headlines_generated_spacy.csv'

    print("Loading training data...")
    training_data = load_training_data(training_file)

    print("Generating headlines...")
    training_titles = {key: value['title'] for key, value in training_data.items() if value['title']}
    process_articles(input_file, output_file, training_titles)

    print(f"Headlines generated successfully! Output saved to {output_file}")
