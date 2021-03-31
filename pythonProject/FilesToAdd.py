import os
from Open_Write import opn, wrt
from Add_2 import adding


# Пути для чтения и записи файлов
fp_op = r"C:\BEREGWIN\VOS"
fp_wr = r"C:\BEREGWIN\VOS_2"
for filename in os.listdir(fp_op):
    Data = opn(filename, fp_op)
    Data = adding(Data)
    wrt(filename, Data, fp_wr)
