#PROBLEM1
#def list(n, words):
#    for i in range(1, n+1):
#        words.append(input("Enter the word:"))
#    print(words)
#    count = {}
#    for c in words:
#        if c in count:
#            count[c] += 1
#        else:
#            count[c] = 1
#    print(count)
#    unique_words = set(count)
#    unique_words = len(unique_words)
#    print(unique_words)
#words = []
#n = int(input("Enter the number of element: "))
#m = list(n, words)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PROBLEM 2
#def main():
#    try:
#        n = int(input("Enter the number:"))
#        for i in range(1, n):
#            print(str(i) * i)
#    except Exception as e:
#        print(e)
#main()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PROBLEM 3
#def ispalindrome(s):
#   return s == s[::-1]
#s = input("Enter the word:")
#pali = ispalindrome(s)
#if pali:
 #   print("True")
#else:
#    print("False")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PROBLEM 4
#import random


#def rockpapersissor(n, option):
#    for i in range(n):
#        print(f"Round {i+1}:")
#        print("Rock")
#       print("Paper")
#        print("Sissor")
#        choice = input("Choice : ").lower()
#        computer_choice = random.choice(option)
#        print(f"Computer Chooses: {computer_choice}")
#        if choice == 'rock' and computer_choice == "Rock":
#            print("Its a Tie...")
#        elif choice == 'rock' and computer_choice == "Paper":
#           print("Computer Wins....")
#        elif choice == 'rock' and computer_choice == "Sissor":
#           print("YOU Win....")
#        elif choice == 'paper' and computer_choice == "Rock":
#           print("You Wins....")
#        elif choice == 'paper' and computer_choice == "Paper":
#           print("Its a Tie....")
#       elif choice == 'paper' and computer_choice == "Sissor":
#           print("Computer Wins....")
#        elif choice == 'sissor' and computer_choice == "Rock":
#            print("Computer Wins....")
#        elif choice == 'sissor' and computer_choice == "Paper":
#            print("You Wins....")
#        elif choice == 'sissor' and computer_choice == "Sissor":
#            print("Its a tie....")
#        else:
#            print("Please enter a word from the following")
#            print(option)
#option = ["Rock", "Paper", "Sissor"]
#n = int(input("Enter the number of matches you want to play:"))
#rps = rockpapersissor(n, option)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PROBLEM 5
#def camelcasing(n):
#   result = ""
#    for i in n:
#        if i.isupper():
#            result += " "
#        result += i  
#    return result.strip()  
#n = input("Enter the Word: ")
#camel = camelcasing(n)
#print(camel)