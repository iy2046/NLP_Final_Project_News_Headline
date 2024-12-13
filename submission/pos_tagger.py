import csv
import ast
import spacy

# Load SpaCy's English model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# File paths
input_file = "sentence_split_and_tokenized.csv"
output_file = "tokens_tagged.pos"

def pos_tagger_with_ner(input_file, output_file):
    """
    Tags tokens with POS and identifies Named Entities (NER) using SpaCy.
    Chooses the most specific tag for each token, and outputs only one tag per token.
    """
    tagged_articles = []
    
    # Read the input CSV
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            article_number = row["article_number"]
            article_title = row["article_title"]
            
            # Parse tokenized_sentences field as a list of sentences
            tokenized_sentences = ast.literal_eval(row["tokenized_sentences"])
            
            # Process each sentence with SpaCy
            tagged_sentences = []
            for sentence in tokenized_sentences:
                doc = nlp(" ".join(sentence))  # Join tokens to form a sentence
                tagged_tokens = []

                for token in doc:
                    # Select the more specific tag: NER tag if available, otherwise POS tag
                    ner_tag = token.ent_type_ if token.ent_type_ else None
                    pos_tag = token.pos_
                    
                    # Determine the tag to use: NER tag is more specific than POS
                    if ner_tag:
                        final_tag = ner_tag
                    else:
                        final_tag = pos_tag
                    
                    # Only output the token with its tag once
                    tagged_tokens.append(f"{token.text}/{final_tag}")
                
                tagged_sentences.append(" ".join(tagged_tokens))
            
            # Append results with article_number and article_title for context
            tagged_articles.append({
                "article_number": article_number,
                "article_title": article_title,
                "tagged_sentences": tagged_sentences
            })
    
    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for article in tagged_articles:
            outfile.write(f"Article {article['article_number']}: {article['article_title']}\n")
            for sentence in article["tagged_sentences"]:
                outfile.write(f"{sentence}\n")
            outfile.write("\n")  # Separate articles by a newline

if __name__ == "__main__":
    pos_tagger_with_ner(input_file, output_file)
    print(f"POS tagging with NER completed. Results saved to '{output_file}'.")





# import csv
# import ast
# import spacy

# # Load SpaCy's English model
# try:
#     nlp = spacy.load("en_core_web_sm")
# except OSError:
#     import spacy.cli
#     spacy.cli.download("en_core_web_sm")
#     nlp = spacy.load("en_core_web_sm")

# # File paths
# input_file = "sentence_split_and_tokenized.csv"
# output_file = "tokens_tagged.pos"

# def pos_tagger_with_ner(input_file, output_file):
#     """
#     Tags tokens with POS and identifies Named Entities (NER) using SpaCy.
#     """
#     tagged_articles = []
    
#     # Read the input CSV
#     with open(input_file, 'r', newline='', encoding='utf-8') as infile:
#         reader = csv.DictReader(infile)
#         for row in reader:
#             article_number = row["article_number"]
#             article_title = row["article_title"]
            
#             # Parse tokenized_sentences field as a list of sentences
#             tokenized_sentences = ast.literal_eval(row["tokenized_sentences"])
            
#             # Process each sentence with SpaCy
#             tagged_sentences = []
#             for sentence in tokenized_sentences:
#                 doc = nlp(" ".join(sentence))  # Join tokens to form a sentence
#                 tagged_tokens = [(token.text, token.pos_, token.lemma_, token.ent_type_) for token in doc]
#                 tagged_sentences.append(tagged_tokens)
            
#             # Append results with article_number and article_title for context
#             tagged_articles.append({
#                 "article_number": article_number,
#                 "article_title": article_title,
#                 "tagged_sentences": tagged_sentences
#             })
    
#     # Write results to output file
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         for article in tagged_articles:
#             outfile.write(f"Article {article['article_number']}: {article['article_title']}\n")
#             for sentence in article["tagged_sentences"]:
#                 tagged_tokens = " ".join(
#                     [f"{token}/{pos}/{lemma}/{ner}" for token, pos, lemma, ner in sentence]
#                 )
#                 outfile.write(f"{tagged_tokens}\n")
#             outfile.write("\n")  # Separate articles by a newline

# if __name__ == "__main__":
#     pos_tagger_with_ner(input_file, output_file)
#     print(f"POS tagging with NER completed. Results saved to '{output_file}'.")









# import csv
# import ast
# from nltk import pos_tag
# from nltk.tokenize import word_tokenize
# from nltk.data import find

# # Ensure NLTK tagger data is available
# try:
#     find('taggers/averaged_perceptron_tagger_eng')
# except LookupError:
#     import nltk
#     nltk.download('averaged_perceptron_tagger_eng')

# # File paths
# input_file = "sentence_split_and_tokenized.csv"
# output_file = "tokens_tagged.pos"

# def pos_tagger(input_file, output_file):
#     """
#     Tags tokens with their Parts-of-Speech (POS) and saves the results.
#     """
#     tagged_articles = []
    
#     # Read the input CSV
#     with open(input_file, 'r', newline='', encoding='utf-8') as infile:
#         reader = csv.DictReader(infile)
#         for row in reader:
#             article_number = row["article_number"]
#             article_title = row["article_title"]
            
#             # Parse tokenized_sentences field as a list of sentences
#             tokenized_sentences = ast.literal_eval(row["tokenized_sentences"])
            
#             # Perform POS tagging for each sentence
#             tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
            
#             # Append results with article_number and article_title for context
#             tagged_articles.append({
#                 "article_number": article_number,
#                 "article_title": article_title,
#                 "tagged_sentences": tagged_sentences
#             })
    
#     # Write results to output file
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         for article in tagged_articles:
#             outfile.write(f"Article {article['article_number']}: {article['article_title']}\n")
#             for sentence in article["tagged_sentences"]:
#                 tagged_tokens = " ".join([f"{token}/{tag}" for token, tag in sentence])
#                 outfile.write(f"{tagged_tokens}\n")
#             outfile.write("\n")  # Separate articles by a newline

# if __name__ == "__main__":
#     pos_tagger(input_file, output_file)
#     print(f"POS tagging completed. Results saved to '{output_file}'.")
