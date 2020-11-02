#TIP: use random.randint to get a random word from the list
#comment
import random

def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    path = '/home/c4r7s3/problems/submission_001-hangman/short_words.txt'
    file_contents= open(file_name,'r')
    list_of_words= file_contents.readlines()
    return list_of_words

def select_random_word(list_of_words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_words = random.randint(0,len(list_of_words)-1)
    word = list_of_words[random_words]
    letter = random.randint(0,len(word)-1)
    space = "_"
    new_word = word[:letter]+space+word[letter+1:]
    print("Guess the word: " +new_word)
    return word

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    answer = input("Guess the missing letter: ")
    return answer

def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    list_of_words = read_file(file_name)
    new_word = select_random_word(list_of_words)
    answer = get_user_input()
    print("The word was: " +new_word)

if __name__ == "__main__":
    run_game('short_words.txt')