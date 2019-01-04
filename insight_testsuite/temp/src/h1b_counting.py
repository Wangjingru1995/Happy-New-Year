import sys
if __name__ == "__main__":
    #print(sys.argv)
    input_name = sys.argv[1]
    f = open(input_name,'r')
    #print(f.readlines()[0])
    lines = f.readlines()
    temp = lines[0].split(';')
    N = len(temp)
    for i in range(0,N):
        if temp[i] == 'CASE_STATUS':
            idx_status = i
        if temp[i] == 'WORKSITE_STATE':
            idx_state = i
        if temp[i] == 'SOC_NAME':
            idx_occupation = i
    #print(temp[idx_status], temp[idx_state], temp[idx_occupation])
    dictState = {}
    dictOccupation = {}
    for line in lines:
        temp1 = line.split(';')
        if temp1[idx_status].upper() != 'CERTIFIED':
            continue
        if temp1[idx_state].strip('"').strip().strip('"') in dictState:
            dictState[temp1[idx_state].strip('"').strip().strip('"')] += 1
        else:
            dictState[temp1[idx_state].strip('"').strip().strip('"')] = 1
        if temp1[idx_occupation].strip('"').strip().strip('"') in dictOccupation:
            dictOccupation[temp1[idx_occupation].strip('"').strip().strip('"')] += 1
        else:
            dictOccupation[temp1[idx_occupation].strip('"').strip().strip('"')] = 1
    f.close()
    #print(dictState)
    #print(dictOccupation)
    # listState = [[key,value] for key, value in dictState.keys(), dictState.values()]
    # listOccupation = [[key,value] for key, value in dictOccupation.keys(),dictOccupation.values()]
    def compare(item1,item2):
        if item1[1] != item2[1]:
            return item2[1] - item1[1]
        else:
            if item1[0] < item2[0]:
                return -1
            else:
                return 1
    listState = []
    listOccupation = []
    listState = [[key, dictState[key]] for key in dictState.keys()]
    listOccupation = [[key,dictOccupation[key]] for key in dictOccupation.keys()]
    '''
    for key in dictState.keys():
        listState.append([key, dictState[key]])
    for key in dictOccupation.keys():
        listOccupation.append([key, dictOccupation[key]])
    '''
    listState.sort( cmp = compare )
    listOccupation.sort( cmp = compare )
    #print(listState)
    #print(listOccupation)

    output_name1 = sys.argv[2]
    ff = open(output_name1,'w')
    ff.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    '''
    lines2 = ff.readlines()
    line_0 =  ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    ';'.join(line_0)
    lines2[0] = line_0
    '''
    totalCertified = sum(dictOccupation.values())
    NN1 = len(listOccupation)
    n1 = min(NN1,10)
    for i in range(0,n1):
        tempLine = [listOccupation[i][0].strip('"').strip().strip('"'),
                    str(listOccupation[i][1]).strip('"').strip().strip('"'),
                    (str(round(1.0*listOccupation[i][1]*100/totalCertified, 1))+'%').strip('"').strip().strip('"')]
        newLine = ';'.join(tempLine)
        ff.write(newLine+'\n')

    output_name2 = sys.argv[3]
    ff2 = open(output_name2,'w')
    ff2.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n') 
    NN2 = len(listState)
    n2 = min(NN2,10)
    for i in range(0,n2):
        tempLine2 = [listState[i][0].strip('"').strip().strip('"'),
                    str(listState[i][1]).strip('"').strip().strip('"'),
                    (str(round(1.0*listState[i][1]*100/totalCertified, 1))+'%').strip('"').strip().strip('"')]
        newLine2 = ';'.join(tempLine2)
        ff2.write(newLine2+'\n')
    ff2.close()

