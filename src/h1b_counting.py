import sys
if __name__ == "__main__":
    print(sys.argv)
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
        if temp1[idx_state] in dictState:
            dictState[temp1[idx_state]] += 1
        else:
            dictState[temp1[idx_state]] = 1
        if temp1[idx_occupation] in dictOccupation:
            dictOccupation[temp1[idx_occupation]] += 1
        else:
            dictOccupation[temp1[idx_occupation]] = 1
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
    print(listState)
    print(listOccupation)
