n=int(input("Enter the dividing number of trained and test data between 0 and 1994: "))

import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
df = pd.read_csv("D:\college project\Research Paper 02\Files and Papers\crime_data - Copy.csv")
#print(df)

# Tranning Part........

l=[]
y0 = df['ViolentCrimesPerPop']
y00 = y0.to_list()
y000=0
for i in range(n):
   if(i<n):
       y000+=y00[i]
  
y000/=n

print("**ViolentCrimesPerPop Average: ",y000)

# To get Standerd Deviation....
sd_sum00=0
for i in range(n):
    z=(y00[i]-y000)*(y00[i]-y000)
    sd_sum00=sd_sum00+z
sd00=math.sqrt(sd_sum00/n)
print("**ViolentCrimesPerPop Standerd Deviation: ",sd00)


# Taking testing data from violent crime........
for i in range(n,1994):
   if(y00[i]>=0.2):
       b=1
       l.append(b)
   else:
       b=0
       l.append(b)
#print(l)




x15 = df['pctWInvInc']
x015 = x15.to_list()
# print(x015)
sum015=0
for i in range(n):
    sum015=sum015+x015[i]
avg015=sum015/n
print("15.pctWInvInc Average: ",avg015)
l15=[]    
for i in range(n):
   
   a015=x015[i]-avg015
   b015=y00[i]-y000
   c015=a015*a015
   d015=a015*b015
   a15=d015/c015
   l15.append(a15)
b15=sum(l15)/n

print("15.ViolentCrimesPerPop-pctWInvInc: ",b15)
# To get Standerd Deviation....
sd_sum01=0
for i in range(n):
    z=(x015[i]-avg015)*(x015[i]-avg015)
    sd_sum01=sd_sum01+z
sd01=math.sqrt(sd_sum01/n)
print("15.pctWInvInc Standerd Deviation: ",sd01)



x37 = df['MalePctDivorce']
x037 = x37.to_list()
# print(x037)
sum037=0
for i in range(n):
    sum037=sum037+x037[i]
avg037=sum037/n
print("37.MalePctDivorce Average: ",avg037)
l37=[]    
for i in range(n):
   
   a037=x037[i]-avg037
   b037=y00[i]-y000
   c037=a037*a037
   d037=a037*b037
   a37=d037/c037
   l37.append(a37)
b37=sum(l37)/n

print("37.ViolentCrimesPerPop-MalePctDivorce: ",b37)
# To get Standerd Deviation....
sd_sum02=0
for i in range(n):
    z=(x037[i]-avg037)*(x037[i]-avg037)
    sd_sum02=sd_sum02+z
sd02=math.sqrt(sd_sum02/n)
print("37.MalePctDivorce Standerd Deviation: ",sd02)





x39 = df['FemalePctDiv']
x039 = x39.to_list()
# print(x039)
sum039=0
for i in range(n):
    sum039=sum039+x039[i]
avg039=sum039/n
print("39.FemalePctDiv Average: ",avg039)
l39=[]    
for i in range(n):
   
   a039=x039[i]-avg039
   b039=y00[i]-y000
   c039=a039*a039
   d039=a039*b039
   a39=d039/c039
   l39.append(a39)
b39=sum(l39)/n

print("39.ViolentCrimesPerPop-FemalePctDiv: ",b39)
# To get Standerd Deviation....
sd_sum03=0
for i in range(n):
    z=(x039[i]-avg039)*(x039[i]-avg039)
    sd_sum03=sd_sum03+z
sd03=math.sqrt(sd_sum03/n)
print("39.FemalePctDiv Standerd Deviation: ",sd03)





x40 = df['TotalPctDiv']
x040 = x40.to_list()
# print(x040)
sum040=0
for i in range(n):
    sum040=sum040+x040[i]
avg040=sum040/n
print("40.TotalPctDiv Average: ",avg040)
l40=[]    
for i in range(n):
   
   a040=x040[i]-avg040
   b040=y00[i]-y000
   c040=a040*a040
   d040=a040*b040
   a40=d040/c040
   l40.append(a40)
b40=sum(l40)/n

print("40.ViolentCrimesPerPop-TotalPctDiv: ",b40)
# To get Standerd Deviation....
sd_sum04=0
for i in range(n):
    z=(x040[i]-avg040)*(x040[i]-avg040)
    sd_sum04=sd_sum04+z
sd04=math.sqrt(sd_sum04/n)
print("40.TotalPctDiv Standerd Deviation: ",sd04)




x71 = df['PctHousOwnOcc']
x071 = x71.to_list()
# print(x071)
sum071=0
for i in range(n):
    sum071=sum071+x071[i]
avg071=sum071/n
print("71.PctHousOwnOcc Average: ",avg071)
l71=[]    
for i in range(n):
   
   a071=x071[i]-avg071
   b071=y00[i]-y000
   c071=a071*a071
   d071=a071*b071
   a71=d071/c071
   l71.append(a71)
b71=sum(l71)/n

print("71.ViolentCrimesPerPop-PctHousOwnOcc: ",b71)
# To get Standerd Deviation....
sd_sum05=0
for i in range(n):
    z=(x071[i]-avg071)*(x071[i]-avg071)
    sd_sum05=sd_sum05+z
sd05=math.sqrt(sd_sum05/n)
print("71.PctHousOwnOcc Standerd Deviation: ",sd05)





x73 = df['PctVacMore6Mos']
x073 = x73.to_list()
# print(x073)
sum073=0
for i in range(n):
    sum073=sum073+x073[i]
avg073=sum073/n
print("73.PctVacMore6Mos Average: ",avg073)
l73=[]    
for i in range(n):
   
   a073=x073[i]-avg073
   b073=y00[i]-y000
   c073=a073*a073
   d073=a073*b073
   a73=d073/c073
   l73.append(a73)
b73=sum(l73)/n

print("73.ViolentCrimesPerPop-PctVacMore6Mos: ",b73)
# To get Standerd Deviation....
sd_sum06=0
for i in range(n):
    z=(x073[i]-avg073)*(x073[i]-avg073)
    sd_sum06=sd_sum06+z
sd06=math.sqrt(sd_sum06/n)
print("73.PctVacMore6Mos Standerd Deviation: ",sd00)




x86 = df['MedOwnCostPctInc']
x086 = x86.to_list()
# print(x086)
sum086=0
for i in range(n):
    sum086=sum086+x086[i]
avg086=sum086/n
print("86.MedOwnCostPctInc Average: ",avg086)
l86=[]    
for i in range(n):
   
   a086=x086[i]-avg086
   b086=y00[i]-y000
   c086=a086*a086
   d086=a086*b086
   a86=d086/c086
   l86.append(a86)
b86=sum(l86)/n

print("86.ViolentCrimesPerPop-MedOwnCostPctInc: ",b86)
# To get Standerd Deviation....
sd_sum07=0
for i in range(n):
    z=(x086[i]-avg086)*(x086[i]-avg086)
    sd_sum07=sd_sum07+z
sd07=math.sqrt(sd_sum07/n)
print("86.MedOwnCostPctInc Standerd Deviation: ",sd07)




x89 = df['PctBornSameState']
x089 = x89.to_list()
# print(x089)
sum089=0
for i in range(n):
    sum089=sum089+x089[i]
avg089=sum089/n
print("89.PctBornSameState Average: ",avg089)
l89=[]    
for i in range(n):
   
   a089=x089[i]-avg089
   b089=y00[i]-y000
   c089=a089*a089
   d089=a089*b089
   a89=d089/c089
   l89.append(a89)
b89=sum(l89)/n

print("89.ViolentCrimesPerPop-PctBornSameState: ",b89)
# To get Standerd Deviation....
sd_sum08=0
for i in range(n):
    z=(x089[i]-avg089)*(x089[i]-avg089)
    sd_sum08=sd_sum08+z
sd08=math.sqrt(sd_sum08/n)
print("89.PctBornSameState Standerd Deviation: ",sd08)




b0=y000-(b015*avg015+b037*avg037+b039*avg039+b040*avg040+b071*avg071+b073*avg073+b086*avg086+b89*avg089)
print("The Corelation Coefficiant: ",b0)


# Testing Part........

e=2.718
l118=[]

for i in range(n,1994):
    

    y=b0+b15*x015[i]+b37*x037[i]+b39*x039[i]+b40*x040[i]+b71*x071[i]+b73*x073[i]+b86*x086[i]+b89*x089[i]
    
    
    y0f=1+pow(e,-y)
    yf=1/y0f
    #print(yf)
    if(yf>=0.2):
       a=1
       l118.append(a)
    else:
        a=0
        l118.append(a)


print(len(l118))


tp=0
tn=0
fp=0
fn=0
for i in range(1994-n):
    if(l118[i]==1 and l[i]==1):
        tp=tp+1
    elif(l118[i]==0 and l[i]==0):
        tn=tn+1
    elif(l118[i]==1 and l[i]==0):
        fn=fn+1
    elif(l118[i]==0 and l[i]==1):
         fp=fp+1
        
print("true positive:",tp)
print("true negative:",tn)
print("false positive:",fp)
print("false negative:",fn)
accuracygood=((tp+tn)/(tp+tn+fp+fn))*100
print("The new accuracy: ",accuracygood)  
re=(tn/(tn+fp))*100
sen=(tp/(tp+fn))*100
pre=(tp/(tp+fp))*100
f1_s=((2*sen*pre)/(sen+pre))
tpr=tp/(tp+fn)
fpr=fp/(fp+tn)
print("Recall: ",sen)
print("Precision: ",pre)
print("F1_Score: ",f1_s)
print("Sensitivity: ",sen)
print("Specificity: ",re)
print("True Positive Rate: ",tpr)
print("False Positive Rate: ",fpr)

