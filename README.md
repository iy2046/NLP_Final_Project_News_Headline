# Automated News Headline Generation Using Natural Language Processing

## Overview
This project processes news articles using **spaCy** and generates headlines for each article. The generated headlines are evaluated using **cosine similarity** with the original article content. It is an end-to-end pipeline for processing, headline generation, and evaluation.

### Features
- Tokenization and Named Entity Recognition (NER) using **spaCy**.
- Headline generation based on syntactic and semantic importance.
- Evaluation of generated headlines using **TF-IDF** and cosine similarity.

## Project Structure
- **File Name**: `NLP_Final_Project.ipynb`
- **Contributors**:
  - Grace Li: Data preprocessing and integration of TF-IDF for evaluation.
  - Nick Yi: Implementation of tokenization and cosine similarity evaluation.
  - Golam Raiyan: Development of headline generation logic and NER functionality.

### Key Functions
1. **`process_articles(input_file)`**: Preprocesses articles by extracting token data and named entities.
2. **`generate_headlines(processed_articles)`**: Creates headlines based on article content.
3. **`calculate_cosine_similarity(original_texts, generated_headlines)`**: Evaluates the similarity of generated headlines with the original text using TF-IDF and cosine similarity.
4. **`get_average_cosine_similarity(similarities)`**: Computes the average similarity score.
5. **`main(input_file, output_file)`**: Orchestrates the entire process.

## Requirements
- **Python 3.8+**
- Libraries:
  - `spaCy`
  - `pandas`
  - `scikit-learn`

## Installation
To run this project, install the required libraries:

pip install spacy pandas scikit-learn
python -m spacy download en_core_web_md

## Running the Project

### Best Environment: Google Colab
This project is best run on **Google Colab**, which provides a pre-configured Python environment and GPU/TPU support for faster processing.

### Steps
1. Clone or upload the Python script (`NLP_Final_Project.ipynb`) to Google Colab.
2. Upload your input file (e.g., `test.csv`) to the runtime environment.
3. Run the script.
4. The output file (e.g., `headline_pipeline_results.csv`) will be generated and can be downloaded.
