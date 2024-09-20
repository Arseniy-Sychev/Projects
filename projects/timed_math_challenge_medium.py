import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problema = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = f"{str(left)} {str(operator)} {str(right)}"
    answer = eval(expr)

    return expr, answer

wrong = 0
input("Press enter to start!")
print("---------------------")
start_time = time.time()

for i in range(total_problema):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem number: {i + 1}: {expr} = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("---------------------")
print(f"Nice work! You finished in {total_time}, seconds!")




    
