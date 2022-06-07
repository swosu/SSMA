#Let's import the random module
import random

#our first function would be to display the intro:
def display():
  title = 'Math Quiz!!'
  print('*' * len(title))
  print(title)
  print('*' * len(title))
  
#We will now create a function that displays a menu
def display_menu():
  menu = ["1. Division" , "2. Subtraction" , "3. Addition", "4. Multiplication"]
  print(menu[0])
  print(menu[1])
  print(menu[2])
  print(menu[3])
  
#Let's create a function that gets the user input
def get_user_input():
  #convert user input to integer value
  user_input = int(input("What's your choice: "))
  while user_input >  5 or user_input <= 0 :
    print("That isn't part of the menu options")
    user_input = int(input("Please try a different option: "))
  else:
    return user_input

#Write a function that gets the users solution to a problem:
def get_solution(problem):
  print('Enter your answer: ')
  print(problem, end = '')
  result  = int(input('='))
  return result

#Write a function that checks the user's solution
def check_solution(users_solution, actual_solution, count):
  if users_solution == actual_solution:
    count += 1
    print("Correct answer!")
    return count
  else:
    print("Wrong answer")
    return count

#Create a function that creates problems for each of the menu options
def menu_option(index, count):
  #the random numbers are in range of 1 to a 100
  num1 = random.randrange(1, 101)
  num2 = random.randrange(1, 101)
  #if the index is 1, create a division problem
  if index is 1:
    #create a division problem
    problem  = str(num1) + ' // ' + str(num2)
    solution = num1 // num2
    user_solution = get_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count
  elif index is 2:
    #create a subtraction problem
    problem  = str(num1) + ' - ' + str(num2)
    solution = num1 - num2
    user_solution = get_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count
  elif index is 3:
    #create an addition problem
    problem = str(num1) + ' + ' + str(num2)
    solution = num1 + num2
    user_solution = get_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count
  else:
    #create a multiplication problem
    problem = str(num1) + ' * ' + str(num2)
    solution = num1 * num2
    user_solution = get_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count

#create a function that displays the total questions and the correct answers
def result(total, correct):
  #if the total is greater than 0
  if total > 0:
    result = correct / total
    percentage = round((result * 100), 2)
  if total == 0:
    percentage = 0
  print(f'You answered {total} questions with {correct} correct answers')
  print(f'Your score is {percentage}%. Thank you for playing!', sep = '')
  
#putting it all together
def main():
  display()
  display_menu()

  option = get_user_input()
  total = 0
  correct = 0
  while option != 5:
    total += 1
    correct = menu_option(option, correct)
    option = get_user_input()
  
  print("Exit the quiz.")
  result(total, correct)

main()

