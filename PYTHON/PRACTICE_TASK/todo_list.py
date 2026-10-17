todos = []

while True:
    print("\n1. Add todo")
    print("2. View todos")
    print("3. Remove todo")
    print("4. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        todo = input("Enter the todo: ").strip()
        if todo:
            todos.append(todo)
            print("Added!")
        else:
            print("Enter a valid todo.")

    elif choice == "2":
        if not todos:
            print("No todos yet.")
        else:
            for i, todo in enumerate(todos, start=1):
                print(f"{i}. {todo}")

    elif choice == "3":
        if not todos:
            print("Nothing to remove.")
            continue
        try:
            number = int(input("Number to remove: "))
            removed = todos.pop(number - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1-4.")