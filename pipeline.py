import os

# Run sentence splitting and tokenization
print("Starting sentence splitting and tokenization...")
os.system("python sentence_split_tokenize.py")

# Run POS tagging
print("Starting POS tagging...")
os.system("python pos_tagging.py")

# Run headline generation
print("Starting headline generation...")
os.system("python headline_generator_pos.py")

print("Pipeline completed successfully.")
