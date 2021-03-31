import os
from Add_2 import lstData
from FilesToAdd import fp_wr


def wrt(file_name):
    dels = ['=', '(', 'ЭЭЭ']
    for i in range(0, len(lstData), 1):
        if len(str(lstData[i])) > 0 and str(lstData[i])[0] in dels:
            lstData[i] = '\n' + str(lstData[i])
    os.chdir(fp_wr)
    Fl = open(file_name, 'w')
    for Data in lstData:
        Fl.write(str(Data) + ',')
