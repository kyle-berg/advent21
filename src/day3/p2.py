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

    file.close()

    for i in range(len(ones)):
        if ones[i] > zeroes[i]:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(gamma)
    print(epsilon)
    
    # gammaString = ""
    # epsilonString = ""
    # for bit in gamma:
    #     gammaString += str(bit)
    # for bit in epsilon:
    #     epsilonString += str(bit)

    # print(gammaString)
    # print(epsilonString)
    
    # gammaSum = int(gammaString, 2)
    # epsilonSum = int(epsilonString, 2)

    # print(gammaSum * epsilonSum)

    # part 2
    print("part 2 -----------------------------------")
    oxy_list = []
    co2_list = []

    file = open("src\day3\day3data.txt", "r")
    line = file.readline()
    while line:
        oxy_list.append(line)
        line = file.readline().strip()
    print("balls")
    file.close()
    co2_list = oxy_list

    most_common = ''
    for i in range(12):
        print("fart")
        ones_count = 0
        zeroes_count = 0
        new_list = []
        for rate in oxy_list:
            if rate[i] == '1':
                ones_count += 1
            else:
                zeroes_count += 1

        if zeroes_count > ones_count:
            most_common = '0'
        else:
            most_common = '1'

        for rating in oxy_list:
            if rating[i] == most_common:
                new_list.append(rating)
        oxy_list = new_list

        if len(oxy_list) == 1:
            break

    most_common = ''
    for i in range(12):
        ones_count = 0
        zeroes_count = 0
        new_list = []
        for rate in co2_list:
            if rate[i] == '1':
                ones_count += 1
            else:
                zeroes_count += 1

        if zeroes_count > ones_count:
            most_common = '0'
        else:
            most_common = '1'

        for rating in co2_list:
            if rating[i] != most_common:
                new_list.append(rating)
        co2_list = new_list

        if len(co2_list) == 1:
            break
        
    print(oxy_list)
    print(co2_list)

    print(int(oxy_list[0], 2)*int(co2_list[0], 2))
    
main()