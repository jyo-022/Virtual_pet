def count_word_frequencies(text):
    text = text.lower()
    
    # Remove punctuation manually
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for char in punctuations:
        text = text.replace(char, "")
    
    # Split text into words
    words = text.split()
    
    # Create a dictionary to store word counts
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the word frequencies
    for word, count in word_counts.items():
        print(f"{word}: {count}")

sample_text = "Python is great, and Python is easy to learn. Python is also powerful!"
count_word_frequencies(sample_text)




