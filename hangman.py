def get_word():
    word = input("Enter the secret word:").lower()
    while not word.isalpha():
        word = input("Enter the secret word:").lower()
    return word

def get_initial_positions(length):
    word_letters = [False]*length
    word_letters[0] = True
    word_letters[-1] = True
    return word_letters

def hide_word(word,word_positions):
    hidden_word = "-"*len(word)
    pos = 0
    for word_position in word_positions:
        if word_position:
            hidden_word = hidden_word[:pos]+word[pos]+hidden_word[pos+1:]
        pos+=1
    return hidden_word

def check_guess(word,letter,word_positions):
    new_positions = word_positions[:]
    for i in range(len(word)):
        if word[i] == letter:
            new_positions[i] = True
    return new_positions

def check_for_win(word_positions):
    for word_position in word_positions:
        if not word_position:
            return False
    return True

def play_hangman():
    word = get_word()
    lives = 5
    positions = get_initial_positions(len(word))
    hidden = hide_word(word,positions)

    print(hidden)

    while True:
        next_letter = input()
        while len(next_letter) != 1:
            next_letter = input()
        new_positions = check_guess(word,next_letter,positions)
        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1

            if lives == 0: # no more lives - break
                print('You lose!')
                break
        else:
            if check_for_win(new_positions):
                print("You win!")
                break
            else:
                print("Another letter guessed!")
                print(hide_word(word,new_positions))
                positions = new_positions

play_hangman()


