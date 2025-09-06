import string 

def text_analyzer(text):
    # Character Count
    char_count = len(text)

    # Word Count
    words = text.split()
    word_count = len(words)

    # Sentence Count 
    sentences = 0
    for char in text:
        if char in ".!?":
            sentences += 1

    # Remove punctuation from text
    clean_text = text.lower()
    for p in string.punctuation:
        clean_text = clean_text.replace(p, '')
    clean_words = clean_text.split()

    # Unique Words
    unique_words = set(clean_words)
    unique_count = len(unique_words)

    # Word Frequency
    word_freq = {}
    for word in clean_words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Most Frequent Word
    most_frequent = max(word_freq, key=word_freq.get) if word_freq else None

    # Result
    print('\n ------- Welcome to Text Analyzer ------- ')
    print(f'Character Count: {char_count}')
    print(f'Word Count: {word_count}')
    print(f'Sentence Count: {sentences}')
    print(f'Unique Words: {unique_count}')
    if most_frequent:
        print(f"🏆 Most Frequent Word: '{most_frequent}' ({word_freq[most_frequent]} times)")

# Loop
while True:
    user_text = input('Enter text to analyze (or type "exit" to quit): ')
    if user_text.lower() == 'exit':
        print('👋 Exiting Text Analyzer. Goodbye!')
        break
    text_analyzer(user_text)
  