while True: 
    print("\n1. set my goals")
    print("2. see my goals")
    print("3. Exit")

    selection = input("Select your future: ")

    if selection == "1":
        note = input("Write your goal: ")

        with open ("mygoals.txt", "a") as file:
           file.write(note + "\n")

        print("Note saved")
       
    elif selection == "2":
       try:
           with open("mygoals.txt", "r") as G:
               GG = G.read()
               print("\nSaved Notes: \n")
               print(GG)
       except FileNotFoundError:
            print("No goals set yet.")
    
    elif selection == "3" :
         print("Goodbye!")
         break
    else:
        print("Invalid Choice")