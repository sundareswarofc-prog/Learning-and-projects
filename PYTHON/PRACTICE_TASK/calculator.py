def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

while True:
    print("\nOperations: +  -  *  /   (or 'q' to quit)")
    op = input("Choose an operation: ").strip()

    if op=="q":
        print("stopped")
        break
    if op not in operations:
        print("Invalid operation.")
        continue
    try:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the Second number: "))

    except ValueError:
        print("Enter a valid number")
        continue

    result=operations[op](a,b)
    print(result,"result")
