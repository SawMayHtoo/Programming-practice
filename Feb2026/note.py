while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input ("Choose:")

    if choice == "1":
        note = input("Write your note: ")

        with open("savednotes.txt", "a") as f:
            f.write(note + "\n")

        print("Note saved")

    elif choice == "2":
        try: 
            with open("savednotes.txt", "r") as R:
                content = R.read()
                print("\n Saved Notes:" )
                print (content)
        except FileNotFoundError:
            print("No notes saved yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else: 
        print("Invalid choice.")
