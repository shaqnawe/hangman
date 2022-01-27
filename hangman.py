import random
def word_vault():
    word_dict = {
        'Chess': ['pawn', 'queen', 'bishop', 'enpassant', 'checkmate', 'captures', 'rook', 'knight', 'resign', 'king'],
        'Computers' : ['mouse', 'keyboard', 'usb', 'motherboard', 'camera', 'software', 'hardware', 'ethernet', 'monitor', 'mousepad'],
        'Presidents' : ['Lincoln', 'Washington', 'Jefferson', 'Jackson', 'Obama', 'Roosevelt', 'Coolidge', 'Kennedy', 'Clinton', 'Reagan']
    }
    # Randomly select a category
    # random_category = random.choice(list(word_dict.keys()))
    # User selects a category for game
    categories = input('What category would you like to pick?\nChess, Computers or Presidents? ').title()

    # Random word from user selected category is displayed
    random_word = random.choice(word_dict[categories])
    #random_word = random.choice(word_dict[random_category])
    # Execute the Hangman program by passing two positional arguments
    hangman(categories, random_word)

def hangman(categories,random_word):
    secret_word = list('_'*len(random_word))
    user_tries = 1
    user_guess = ''
    # Loop exits if user exceeds permitted attempts or correctly guesses the word
    while user_tries < 8 and "".join(secret_word) != random_word:
        # If user exceeds the permitted tries (7)
        if user_tries > 6:
            print('Sorry you\'re out of tries\nBetter luck next time. :(')
            print(f'The correct word was {random_word.title()}')
            break
        
        # Prints the secret word and updates according to correct user_guess
        print(f'Secret Word: {secret_word}')
        # Display the user selected category 
        print(f'Your category is: {categories}')
        # Takes user input to check against secret word
        user_guess = input('What is your guess? ')
        
        # Check to see if user guess is present in random_word
        # If user_guess is correct, replace '_' with user_guess
        if user_guess in random_word.lower():
            for char in range(len(random_word)):
                if random_word[char].lower() == user_guess:
                    secret_word[char] = random_word[char]
        
        # Increment user_tries by 1 if user guess is incorrect
        if user_guess not in random_word.lower():
            user_tries += 1
    
    if "".join(secret_word).lower() == random_word.lower():
        print(f'Congratulation you\'ve guessed the word! {random_word.title()}\nit took you {user_tries} tries.')

word_vault()