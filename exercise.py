#Accepts results from student which includes the cats cat marks and the exam marks
#if above 50 -->pass else failed

# Prompt to enter marks
catMarks = int(input("Enter your  cat marks:\t"))
examMarks = int(input("Enter your exam marks:\t\n"))

# Calculating the total
finalScore = catMarks + examMarks
msg = f'Your total mark is {finalScore}.'

# Display message
if finalScore < 50:
    print(msg + "You have FAILED.")
else:
    print(msg + "You have PASSED.")

