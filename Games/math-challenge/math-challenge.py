import random
import time

OPERATORS = ["+", "-", "*"]
min_operator = 3
max_operator = 12
total_problems = 5
wrong = 0

def generate_problem():
    left = random.randint(min_operator, max_operator)
    right = random.randint(min_operator, max_operator)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

input("Press enter to start")
print("--------------------")

start_time = time.time()

for questions in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(questions + 1) + " : " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print("--------------------")
print("Nice work! You finished in", total_time, "seconds'")
