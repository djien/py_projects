import requests
import random
rand = random.randint(1,10)

# trivia_fetch() needs to exist first before main()
def trivia_fetch(num):
  numbersapi = requests.get(f"http://numbersapi.com/{num}?json")
  translation = numbersapi.json() #this is a dictionary
  return translation

def main():
  num = int(input("Enter any number for a random fact: "))
  print(trivia_fetch(num)['text'],'\n')

if __name__ == "__main__":
  main()

print("Type extra() to play a trivia game!")

def extra():
 print("\nTrivia Time! Hint: the answer is between number [1 - 10]\n")
 quiz_dict =  trivia_fetch(rand)
 question = quiz_dict['text']  
 answer = str(quiz_dict['number']) 
 win = False
 print(question.replace(answer,"What number").replace(".","?"))

 while not win:
  response = input("Your answer: ")
  if response == answer:
   win = True
  else:
   print("Guess again.")
 print("Correct! Thank you for playing!")
