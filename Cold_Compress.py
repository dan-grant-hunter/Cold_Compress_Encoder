# Get Number of Inputs
def getInputs():
    while True:
        try:
            numberOfInputs = int(input('Enter Number of Lines: '))
            if numberOfInputs <= 0:
               print('Number must be higher than 0')
               continue
        except ValueError:
            print("Please enter numbers only")
            continue
        else:
            return numberOfInputs
            break


# Get List of Inputs
def getListOfInputs(numberOfInputs):
    listOfInputs = []
    for input_ in range(numberOfInputs):
        getInput =  input(f'Enter message {input_ + 1} to be encoded: ')
        listOfInputs.append(getInput)
    return listOfInputs


# Encode String
def getOutputList(listOfInputs):
    outputList = []
    for line in range(len(listOfInputs)):
        decodedString = []
        counter = []
        characterCount = None
        start = 0
        for char in range(len(listOfInputs[line])):
            characterCount = listOfInputs[line][char]
            if char < (len(listOfInputs[line])-1):
                if characterCount == listOfInputs[line][char+1]:
                    counter.append(characterCount)
                    continue
                else:
                    counter.append(characterCount)
                    end = 0
                    end += char + 1
                    timeRepeated = counter[start:end].count(characterCount)
                    start = char + 1
                    decodedString.append(timeRepeated)
                    decodedString.append(characterCount)
            else:
                counter.append(characterCount)
                end = char + 1
                timeRepeated = counter[start:end].count(characterCount)
                decodedString.append(timeRepeated)
                decodedString.append(characterCount)
        outputList.append(decodedString)
    return outputList


# Main Loop
def mainLoop():
    numberOfInputs = getInputs()
    listOfInputs = getListOfInputs(numberOfInputs)
    outputList = getOutputList(listOfInputs)
    for i in range(len(outputList)):
        print(f'Decoded Message {i+1}: ', " ".join(map(str, outputList[i])))


# Replay Prompt
if __name__ == '__main__':
    while True:
        mainLoop()
        while True:
            answer = input('Encode Again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            print('\nGoodbye')
            break
