import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words=["big","red","family"]
    print(numbers)
    append_random_numbers(numbers,)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)



def  append_random_numbers(numlist,quantity=1):
  for _ in range(quantity):
        num=random.uniform(0,100)
        num=round(num,1)
        numlist.append(num)

if __name__ == "__main__":
    main()
