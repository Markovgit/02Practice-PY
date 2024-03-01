import enchant

def spell_check(text):
    # Create an instance of the English dictionary
    d = enchant.Dict("en_US")
    
    # Split the text into words
    words = text.split()
    
    # List to store misspelled words
    misspelled_words = []
    
    # Iterate through each word
    for word in words:
        # Check if the word is misspelled
        if not d.check(word):
            misspelled_words.append(word)
    
    return misspelled_words

if __name__ == "__main__":
    input_text = input("Enter text to spell check: ")
    misspelled = spell_check(input_text)
    if misspelled:
        print("Misspelled words:")
        for word in misspelled:
            print(word)
    else:
        print("No misspelled words found.")
