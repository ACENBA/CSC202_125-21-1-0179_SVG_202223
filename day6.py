#Functions, Code Blocks and While Loops#Hurdle Onedef right_turn():    turn_left()    turn_left()    turn_left()def jump():    move()    turn_left()    move()    right_turn()    move()    right_turn()    move()     turn_left()for i in range(1, 7):    jump()#While LoopDay 7#Hangman Projectimport randomstages = ['''    +----+    |    |    o    |    /|\  |    / \  |         |    =======    ''', '''   +----+    |    |    o    |    /|\  |    /   |         |    =======    ''', '''   +----+    |    |    o    |    /|\  |         |         |    =======''', '''   +----+    |    |    o    |    /|   |         |         |    =======''', '''   +----+    |    |    o    |    /    |         |         |    =======''', '''   +----+    |    |    o    |         |         |         |    =======''', '''   +----+    |    |         |         |         |         |    =======''']chosen_word = random.choice(word_list)lives = 6print(f'pssst, the solution is {chosen_word}')display = []word_length= len(chosen_word)for _ in range (word_length):    display += "_"print(display)guess = input("Guess a letter: ").lower()end_of_game = Falsewhile not end_of_game:    guess = input("Guess a letter: ").lower()    for position in range(word_length):        letter = chosen_word[position]        if letter == guess:            display[position] = letter        else:            print("No match")                print(f"{' '.join(display)}")        if "_" not in display:        end_of_game = True        print("You win!")    print(stages[lives])    