def num():
    print("\n\tWelcome to bosco's number list app\n")
    numlist = []
    ñ = int(input("Enter how many numbers you want on your list : "))
    for times in range(ñ): 
          numlist.append(int(input("Enter number: ")))
        

    print(f"\nThe sum of all the numbers on your list is  = {sum(numlist)}")
    print(f"\nThe highest number in your list is  = {max(numlist)}")
    print(f"\nThe lowest number in your list is = {min(numlist)}")
    
num()
