# sum_1_to_50.py

def sum_integers_1_to_50():
    total = 0
    for i in range(1, 51):
        total += i
    print(f"The sum of integers from 1 to 50 is: {total}")

if __name__ == "__main__":
    sum_integers_1_to_50()
