import numpy as np
def convertLower(value):
    for i in value:
        value[value.index(i)]=i.lower()
    return value
#step1 calculate information or coourances
def calculateInfo(Feature,Label):
    label=convertLower(Label)
    feature=convertLower(Feature)
    groups,Class=checkGroups(feature)
    if Class==2:
        info=calculate_Info_Class2(feature,label,groups)
    elif Class==3:
        info=calculate_Info_Class3(feature,label,groups)
    elif Class==4:
        info=calculate_Info_Class4(feature,label,groups)
    else:
        print("Class Number out of range. \n")
    return info
def checkGroups(feature):
    Groups=[]
    count=0
    for i in feature:
        if i not in Groups:
            Groups.append(i)
            count+=1
        else:
            continue
    graph=convertLower(Groups)
    return graph,count
def calculate_Info_Class2(feature,label,groups):
    value=[0,0,0,0]
    for index,i in enumerate(feature):
        if (i==groups[0]  and  label[index] == "yes"):
            value[0] += 1
        elif (i==groups[0] and label[index] == "no"):
            value[1] += 1
        elif (i==groups[1] and label[index] == "yes"):
            value[2]+= 1
        elif (i==groups[1] and label[index] == "no"):
            value[3]+= 1
    dictionary={groups[0]:(value[0],value[1]),groups[1]:(value[2],value[3])}
    return dictionary
def calculate_Info_Class3(feature,label,groups):
    value=[0,0,0,0,0,0,0]
    for index,i in enumerate(feature):
        if (i==groups[0]  and  label[index] == "yes"):
            value[0] += 1
        elif (i==groups[0] and label[index] == "no"):
            value[1] += 1
        elif (i==groups[1] and label[index] == "yes"):
            value[2]+= 1
        elif (i==groups[1] and label[index] == "no"):
            value[3]+= 1
        elif (i==groups[2] and label[index] == "yes"):
            value[4]+= 1
        elif (i==groups[2] and label[index] == "no"):
            value[5]+= 1
    dictionary={groups[0]:(value[0],value[1]),groups[1]:(value[2],value[3]),groups[2]:(value[4],value[5])}
    return dictionary
def calculate_Info_Class4(feature, label,groups):
    value=[0,0,0,0,0,0,0,0,0]
    for index,i in enumerate(feature):
        if (i==groups[0]  and  label[index] == "yes"):
            value[0] += 1
        elif (i==groups[0] and label[index] == "no"):
            value[1] += 1
        elif (i==groups[1] and label[index] == "yes"):
            value[2]+= 1
        elif (i==groups[1] and label[index] == "no"):
            value[3]+= 1
        elif (i==groups[2] and label[index] == "yes"):
            value[4]+= 1
        elif (i==groups[2] and label[index] == "no"):
            value[5]+= 1
        elif (i == groups[3] and label[index] == "yes"):
            value[6] += 1
        elif (i == groups[3] and label[index] == "no"):
            value[7] += 1
    dictionary={groups[0]:(value[0],value[1]),groups[1]:(value[2],value[3]),groups[2]:(value[4],value[5]),groups[3]:(value[6],value[7])}
    return dictionary
def getColumn(matrix, i):
    return [row[i] for row in matrix]
#step2 calculate entropy of classes
def calculateGroupEntropy(Info):
    entropy={}
    for key ,value in Info.items():
        total=value[0]+value[1]
        if value[0] != 0:
            phase1= (value[0]/total) *np.log(value[0]/total)
        else:
            phase1=0
        if value[1] != 0:
            phase2= (value[1]/total)*np.log(value[1]/total)
        else:
            phase2=0
        total= -phase1-phase2
        entropy.update({key:total})
    return entropy

# step3 calculate entropy of column
def calculateColumnEntropy(Info, GEntropy,columName):
    entropy=0
    def Total(Info):
        total=0
        for key,value in Info.items():
            for v in value:
                total += v
        return total

    for key ,value in Info.items():
        sum = value[0] + value[1]
        v1 = sum / Total(Info)
        v2 = GEntropy[key]
        value = v1 * v2
        entropy+=value
    entroppy={columName:entropy}
    return entroppy

#step 4 Computing Info gain
def CalculateInfoGain(columnEntropy):
    Info_gain={}
    for key ,value in columnEntropy.items():
        print("Working")
        Info_gain={key:1-value}
        # Info_gain=1-Alt_TE
    return Info_gain