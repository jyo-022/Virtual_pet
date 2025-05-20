def is_palindrome(word):
    # Convert to lowercase for case-insensitive comparison
    word = word.lower()
    
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Direct code without main check
user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")