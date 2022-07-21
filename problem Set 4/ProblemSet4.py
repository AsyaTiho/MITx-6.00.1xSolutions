#Problem1solution
def getWordScore(n,word):
    score=0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if n == len(word):
        score+=50
    return score


#Problem 2solution
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for letter in word:
        if letter in new_hand:
            new_hand[letter]-=1
    return new_hand


#Problem3solution
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    check_hand = hand.copy()
    for letter in word:
        if letter not in check_hand:
            return False
        elif letter in check_hand:
            check_hand[letter]-=1
            if check_hand[letter] <0:
                return False
    return True


#Problem4solution
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    cacl_hand = hand.copy()
    return sum(cacl_hand.values())
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current Hand: ", end=" ")
        displayHand(hand)
        
        # Ask user for input
        user_input = str(input('Enter word, or a "." to indicate that you are finished:'))
        # If the input is a single period:
        if user_input == ".":
            # End the game (break out of the loop)
            break   
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(user_input, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(user_input, n)
                print("'"+user_input+"'" + " earned " + str(getWordScore(user_input, n)) + " points. Total: " + str(score) + "spoints")
                # Update the hand 
                hand = updateHand(hand, user_input)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if user_input == ".":
        print("Goodbye! Total score:" + str(score) + " points") 
    else:
        print("Run out of letters. Total score:" + str(score) + " points")


#Problem5solution        
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    HAND_SIZE = 7
    storedHand = {}
    
    while True:
        play_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if play_input == "n":
            new_hand = dealHand(HAND_SIZE)
            storedHand = new_hand
            playHand(new_hand, wordList, HAND_SIZE)
            
        elif play_input == "r":
            if storedHand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(storedHand, wordList, HAND_SIZE)
        elif play_input == "e":
            break
        else:
            print("Invalid command.")


#Problem6solution
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    storedHand = {}
    
    while True:
        play_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if play_input == "n":
            new_hand = dealHand(HAND_SIZE)
            storedHand = new_hand
            playHand(new_hand, wordList, HAND_SIZE)
            
        elif play_input == "r":
            if storedHand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(storedHand, wordList, HAND_SIZE)
        elif play_input == "e":
            break
        else:
            print("Invalid command.")


#Problem7solution
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    storedHand = {}
    while True:
        play_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if play_input == "e":
            break
        elif play_input == "r":
            if storedHand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                while True:
                    choice_input = str(input("Enter u to have yourself play, c to have the computer play: "))
                    if choice_input == "u":
                        playHand(storedHand, wordList, HAND_SIZE)
                        break
                    elif choice_input == "c":
                        compPlayHand(storedHand, wordList, HAND_SIZE)
                        break
                    elif choice_input == "e":
                        break
                    else:
                        print("Invalid command.")

        elif play_input == "n":
            while True:
                choice_input = str(input("Enter u to have yourself play, c to have the computer play: "))
                if choice_input == "u":
                    new_hand = dealHand(HAND_SIZE)
                    storedHand = new_hand
                    playHand(new_hand, wordList, HAND_SIZE)
                    break
                elif choice_input == "c":
                    new_hand = dealHand(HAND_SIZE)
                    storedHand = new_hand
                    compPlayHand(new_hand, wordList, HAND_SIZE)
                    break
                elif choice_input == "e":
                    break
                else:
                    print("Invalid command.")
        else:
            print("Invalid command.")



    


