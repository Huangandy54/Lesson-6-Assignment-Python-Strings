# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

commands = ["help", "issue", "contact support"]

user_input = input("Please enter your command")
for command in commands:
    if command in user_input.lower():
        if command == "help":
            print("Lets see how we can help you with that")
        if command == "issue":
            print("Please expand on your issue so we can try to resolve it together")
        if command == "contact support":
            print("Connecting you to a customer support agent...")


# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

user_input = input("Please enter your command")

if "issue" in user_input.lower():
    if "login" in user_input.lower():
        print("Category: Login Issue")
    if "performance" in user_input.lower():
        print("Category: Performance Issue")
    if "error" in user_input.lower():
        print("Category: Error")