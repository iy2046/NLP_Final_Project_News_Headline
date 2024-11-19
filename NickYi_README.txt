The python program performs sentence splitting and tokenization on the Kaggle news article dataset; it processes the first 1000 articles.

The program outputs a .csv file with the structure: article_number,article_title,tokenized_sentences.
- For example: 0,hello world,“[[‘First’, ‘Sentence’, ‘.’], [‘Second’, ‘Sentence’, ‘.’]]”

Contractions are represented with quotation marks.
- For example: ['He', ""'s"", 'hoping', 'to'].
