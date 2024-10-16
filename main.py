import os
from time import sleep
"""
    CREATE A PROGRAM THAT DISPLAYS THE GRADE AND THE CLASSIFICATION
"""
grade = {
    "prelim": int(input("Prelim: ")),
    "midterm": int(input("Midterm: ")),
    "final": int(input("Final: ")),
}

sum = ((grade.get("prelim") * 0.3) + (grade.get("midterm") * 0.3) + (grade.get("final") * 0.4))

os.system("clear")

for i in range(1, 3 ,1):
    print("wait a second.")
    sleep(2)
    os.system("clear")
    print("wait a second..")
    sleep(2)
    os.system("clear")
    print("wait a second...")
    sleep(2)
    os.system("clear")

if sum >= 89 and sum < 100:
    print(f"THIS IS YOUR FUCKING GRADE: {sum:.2f}")
    print("You are fucking passed")
elif sum >= 75 and sum < 89:
    print(f"THIS IS YOUR FUCKING GRADE: {sum:.2f}")
    print("You are just passed")
elif sum < 75:
    print(f"THIS IS YOUR FUCKING GRADE: {sum:.2f}")
    print("You are medyo okay")
else:
    print(f"THIS IS YOUR FUCKING GRADE: {sum:.2f}")
    print("ano ka bang klasing tao?")

sleep(2)
print("pakyu")
sleep(1)

