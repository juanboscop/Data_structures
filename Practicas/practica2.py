def num():
    print("\n\tWelcome to bosco's number list app\n")
    numlist = []
    ñ = int(input("Enter how many numbers you want on your list : "))
    for times in range(ñ): 
        numlist.append(int(input("Enter number: ")))

    
    for i in numlist:
        numlist.count(i)
        numlist.remove(i)
            

    print(numlist)
        

    

num()

   