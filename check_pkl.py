import pickle

file_path = r'D:\CUAI_MM\transformer-image-captioning\target\vocabulary.pkl'

try:
    with open(file_path, 'rb') as f:
        vocabulary = pickle.load(f)
    print("File loaded successfully.")
    print(f"Vocabulary content (sample): {list(vocabulary.items())[:5]}")  # Display the first 5 items as a sample
except Exception as e:
    print(f"Failed to load file: {e}")