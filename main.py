# Ask the user how many questions do they want to answer
import random

numQuestions=int(input("How many questions do you want? "))
# Ask the user what the lowest number is
low=1
# Ask the user what the highest number is
high=1
# Ask them which operation they want: 1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide

# loop:
for question in range(1,numQuestions+1):
    print(f"Question {question}:")
    # - Pick two random numbers, ask the user a question
    num1 = random.randint(low,high)
    num2 = random.randint(low,high)
    num1 = num1*num2
    ans =num1//num2

    print(f"{num1} / {num2} = ?")
    userAns = int(input())
    if userAns ==ans:
        print("Yup")
    else:
        print("Nope",ans)