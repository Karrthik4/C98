def countWordsFromFile():
    fileName = input("Enter the file name: ")
    numberOfWords = 0
    file = open(fileName,'r')
    for line in file:
        words = line.split()
        print(words)
        numberOfWords = numberOfWords+len(words)
        print(numberOfWords)
    print("Number Of Words ",numberOfWords)

countWordsFromFile()        


