import os
import pandas as pd

def display_generated_headlines():
    try:
        # Read the subset data to get the original headlines
        original_data = pd.read_csv("subset_news_data.csv")
        # Read the generated headlines
        generated_data = pd.read_csv("generated_headlines.csv")

        if "article_number" not in generated_data.columns or "generated_headline" not in generated_data.columns:
            print("Error: Required columns missing in 'generated_headlines.csv'.")
            return
        if "title" not in original_data.columns:
            print("Error: Required column 'title' missing in 'subset_news_data.csv'.")
            return

        # Merge the original and generated headlines for comparison
        merged_data = pd.merge(
            original_data[["title"]].reset_index().rename(columns={"index": "article_number"}),
            generated_data,
            on="article_number",
            how="inner"
        )

        print("\nDisplaying original and generated headlines for the first 10 articles:")
        for _, row in merged_data.iterrows():
            print(f"Article {row['article_number']}:\nOriginal Headline: {row['title']}\nGenerated Headline: {row['generated_headline']}\n")
    except Exception as e:
        print(f"Error displaying results: {e}")

print("Starting the pipeline for the first 10 articles...")

# Step 1: Create subset of the original dataset
print("Creating a subset of 10 articles from the original dataset...")
df = pd.read_csv("subset_news_data.csv")  # Ensure this file contains the relevant data
subset = df.head(10)
subset.to_csv("subset_news_data.csv", index=False)
print("Subset saved to subset_news_data.csv.")

# Step 2: Run sentence splitting and tokenization
print("Running sentence splitting and tokenization...")
os.system("python sentence_split_tokenize.py")

# Step 3: Run POS tagging and NER
print("Running POS tagging and NER...")
os.system("python pos_tagging_ner.py")

# Step 4: Generate headlines
print("Generating headlines...")
os.system("python headline_generator_ner.py")

# Step 5: Display original and generated headlines
display_generated_headlines()
