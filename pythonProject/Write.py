import os
from Add_2 import lstData
from Open import flmne
dels = ['=', '(', 'ЭЭЭ']
for i in range(0, len(lstData), 1):
    if len(str(lstData[i])) > 0 and str(lstData[i])[0] in dels:
        lstData[i] = '\n' + str(lstData[i])
os.chdir(r'C:\BEREGWIN\VOS_2')
Fl = open(flmne, 'w')
for Data in lstData:
    Fl.write(str(Data) + ',')
