import enchant
import difflib

def get_suggestions(word):
    suggestions = enchant.Dict("en_US").suggest(word)
    if suggestions:
        return suggestions
    else:
        return ["No suggestions available"]

def correct_text(text):
    words = text.split()
    corrected_text = []
    for word in words:
        if enchant.Dict("en_US").check(word):
            corrected_text.append(word)
        else:
            suggestions = get_suggestions(word)
            corrected_word = input(f"Word '{word}' not found. Suggestions: {suggestions}\nEnter corrected word (or press enter to keep): ")
            if corrected_word:
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)
    return ' '.join(corrected_text)

if __name__ == "__main__":
    input_text = input("Enter text to correct: ")
    corrected_text = correct_text(input_text)
    print("Corrected text:")
    print(corrected_text)
