import os


def emptytest(lst):
    for x in lst:
        if x == ' ':
            pass
        else:
            return False
    return True


def opn(file_name, path):
    os.chdir(path)
    Fl = open(file_name, "r")
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
    return lstData


def wrt(file_name, lstData, path):
    dels = ['=', '(', 'Э']
    for i in range(0, len(lstData), 1):
        if len(str(lstData[i])) > 0 and str(lstData[i])[0] in dels:
            lstData[i] = '\n' + str(lstData[i])
    os.chdir(path)
    Fl = open(file_name, 'w')
    for Data in lstData:
        Fl.write(str(Data) + ',')
