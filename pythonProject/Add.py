from Open import lstData
AddN = -3                                     #Значение поправки
Hlv1 = ['=01', '=1','= 1']
dels = ['=','(','ЭЭЭ']
HLv7 = ['=7', '=07']
HLv8 = ['=8', '=08']
HLv9 = ['=9', '=09']
Sha = ['-', '/', 'Щ']
for i in range(0,len(lstData),1):
    if str(lstData[i]) in Hlv1:
        if str(lstData[i+1]) and lstData[i+7] not in Sha:
            lstData[i+7] = lstData[i+7] + AddN
    if str(lstData[i]) in HLv8:
        for x in range(2,5,2):
            if str(lstData[i+x]) not in Sha:
                lstData[i+x] = lstData[i+x] + AddN
    if str(lstData[i]) in HLv9:
        for x in range(2,9,2):
            if str(lstData[i+x]) not in Sha:
                lstData[i+x] = lstData[i+x] + AddN
    if str(lstData[i]) in HLv7:
        k = i + 1
        while str(lstData[k])[0] not in dels:
            if type(lstData[k]) == int:
                lstData[k] = lstData[k] + AddN
            k = k + 1
        lstData[i+18] = '\n' + str(lstData[i+18])
    if len(str(lstData[i])) > 0 and str(lstData[i])[0] in dels:
        lstData[i] = '\n' + str(lstData[i])

