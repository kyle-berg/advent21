def main():
    file = open("src\day3\day3data.txt", "r")
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma = []
    epsilon = []
    line = file.readline()
    while line:
        #read line
        #count ones and zeroes in each line
        for i in range(len(line)-1):
            if line[i] == '1':
                ones[i] += 1
            else:
                zeroes[i] += 1
        line = file.readline()
    print(ones)
    print(zeroes)
    
    for i in range(len(ones)):
        if ones[i] > zeroes[i]:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(gamma)
    print(epsilon)
    
    gammaString = ""
    epsilonString = ""
    for bit in gamma:
        gammaString += str(bit)
    for bit in epsilon:
        epsilonString += str(bit)

    print(gammaString)
    print(epsilonString)
    
    gammaSum = int(gammaString, 2)
    epsilonSum = int(epsilonString, 2)

    print(gammaSum * epsilonSum)

main()
