score = 81
behavior = 'not good'

if score >= 80 and behavior == 'good':
   print("Congratulations! You got an A and have behaved well.")
   print("Keep it up!")
elif score >= 80 and behavior != 'good':
   print("You got an A, but your behavior is not good.")
   print("Please improve!")
else:
   print("Let's study harder!")


# ternary
passed = True
print("Congratulations!") if passed else print("Try again.")

# ternary tuple
passed = False
result_message = ("Try again, you haven't passed.", "Congratulations, you've passed!")[passed]
print(result_message)

