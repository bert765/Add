import os


def emptytest(lst):
    for x in lst:
        if x == ' ':
            pass
        else:
            return False
    return True


os.chdir(r'C:\BEREGWIN\VOS')
flmne = "MPO89004.191"
Fl = open(flmne, "r")
strFile = Fl.read()
lstLines = strFile.splitlines()
lstData = []
for i in lstLines:
    lstData = lstData+i.split(',')         # Splitting by ','
for i in lstData:
    if emptytest(i):              # Delete empty values
        lstData.remove(i)
for i in range(0, len(lstData), 1):        # Change str to int if possible
    try:
        lstData[i] = int(lstData[i])
    except Exception:
        pass
