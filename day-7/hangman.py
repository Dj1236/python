word_list =["dhairya","joshi","niteshbhai"]
import random
choosen_word = random.choice(word_list)
print(f"the sollution is {choosen_word}.")
display =[]
wordlength= len(choosen_word)


for _ in choosen_word:
    display += "_"  # _ represents the blank spaces of word
    print(display)
endofgame = False
while not endofgame:
  guess = input("guess a letter ").lower()

  for position in range(wordlength):
    letter =choosen_word[position]
    print(F"curent position:{position} \n current letter :{letter}\nguessed letter:{guess}")
    if letter == guess:
          display[position] = letter

  print(display)

  if "_" not in display:
      endofgame = True
      print("you win")
       


    
    