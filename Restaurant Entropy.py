import csv
import Entropy
import numpy as np
with open("Restaurent.csv") as f:
    dataset1=csv.reader(f)
    retaurent=list(dataset1)
print(retaurent)

headings=retaurent[0]
features=retaurent[1:]
labels=Entropy.getColumn(features,-1)
col=Entropy.getColumn(features,-3)
print(col,labels)
Information=Entropy.calculateInfo(col,labels)
print(Information)
groupEntropy=Entropy.calculateGroupEntropy(Information)
print(groupEntropy)
columName=headings[0]
print(columName)
columnEntropy=Entropy.calculateColumnEntropy(Information,groupEntropy,columName)
print(columnEntropy)
InfoGain=Entropy.CalculateInfoGain(columnEntropy)
print(InfoGain)


# Alt_IG=InfoGain(Alt_TE)
# Bar_IG=InfoGain(Bar_TE)
# Hun_IG=InfoGain(Hun_TE)
# Rain_IG=InfoGain(Rain_TE)
# Res_IG=InfoGain(Res_TE)
# Pat_IG=InfoGain(Pat_TE)
# Price_IG=InfoGain(Price_TE)
# Type_IG=InfoGain(Type_TE)
# Est_IG=InfoGain(Est_TE)
# print("Info Gain Values:\n","\n Alt:",Alt_IG,"\n Bar:",Bar_IG,"\n Hun:",Hun_IG,"\n rain:",Rain_IG,"\n Res:",Res_IG,"\n Pat:",Pat_IG,"\n Price:",Price_IG,"\n Type:",Type_IG,"\n Est:",Est_IG)
#
