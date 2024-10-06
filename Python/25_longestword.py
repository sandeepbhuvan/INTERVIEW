def  longestw(list):
    max=""
    for x in list:
        if(len(x) > len(max)):
            max = x
    print("Longest word is : ", max)


l = int(input("Enter no. of words: "))
print("Enter words: ")
x = [input() for _ in range(l)]
longestw(x)

