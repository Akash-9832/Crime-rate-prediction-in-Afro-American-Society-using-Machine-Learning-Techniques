
l1001=[]
print("Entropy Calculation of all field")
n=1994 #int(input("Enter the number for entropy between 0 and 1994: "))

import math
import pandas as pd
df = pd.read_csv("E:\college project\Research Paper 02\Files and Papers\crime_data.csv")
#print(df)



x1 = df['population']
x01 = x1.to_list()
#print(x01)
sum01=0
for i in range(n):
    sum01=sum01+x01[i]
avg01=sum01/n
print("1.population Average: ",avg01)

'''
sum1=0
for i in range(n):
    if(x01[i]!=0):
        #x01[i]=avg01
        pi01=x01[i]/n
        #print(pi01)
        sum1+=(-(pi01*math.log10(pi01)))
        
print("1.population entropy: ",sum1)
'''

low01=0
equal01=0
high01=0
for i in range(n):
    if(x01[i]>avg01):
       high01=high01+1
    elif(x01[i]!=0 and x01[i]<avg01):
        low01=low01+1

    else:
         equal01=equal01+1

print(low01,equal01,high01)
e01=math.log10(low01/1994)
e001=math.log10(equal01/1994)
e0001=math.log10(high01/1994)
e1=-((low01/1994)*e01+(equal01/1994)*e001+(high01/1994)*e0001)
print("1.population entropy: ",e1)
l1001.append(e1)


x2 = df['householdsize']
x02 = x2.to_list()
# print(x02)
sum02=0
for i in range(n):
    sum02=sum02+x02[i]
avg02=sum02/n
print("2.householdsize Average: ",avg02)


low02=0
equal02=0
high02=0
for i in range(n):
    if(x02[i]>avg02):
       high02=high02+1
    elif(x02[i]!=0 and x02[i]<avg02):
        low02=low02+1

    else:
         equal02=equal02+1

print(low02,equal02,high02)
e02=math.log10(low02/1994)
e002=math.log10(equal02/1994)
e0002=math.log10(high02/1994)
e2=-((low02/1994)*e02+(equal02/1994)*e002+(high02/1994)*e0002)

print("2.householdsize entropy: ",e2)
l1001.append(e2)




x3 = df['racepctblack']
x03 = x3.to_list()
# print(x03)
sum03=0
for i in range(n):
    sum03=sum03+x03[i]
avg03=sum03/n
print("3.racepctblack Average: ",avg03)

low03=0
equal03=0
high03=0
for i in range(n):
    if(x03[i]>avg03):
       high03=high03+1
    elif(x03[i]!=0 and x03[i]<avg03):
        low03=low03+1

    else:
         equal03=equal03+1

print(low03,equal03,high03)
e03=math.log10(low03/1994)
e003=math.log10(equal03/1994)
e0003=math.log10(high03/1994)
e3=-((low03/1994)*e03+(equal03/1994)*e003+(high03/1994)*e0003)
        
print("3.racepctblack entropy: ",e3)
l1001.append(e3)



x4 = df['racePctWhite']
x04 = x4.to_list()
# print(x04)
sum04=0
for i in range(n):
    sum04=sum04+x04[i]
avg04=sum04/n
print("4.racePctWhite Average: ",avg04)


low04=0
equal04=0
high04=0
for i in range(n):
    if(x04[i]>avg04):
       high04=high03+1
    elif(x04[i]!=0 and x04[i]<avg04):
        low04=low04+1

    else:
         equal04=equal04+1

print(low04,equal04,high04)
e04=math.log10(low04/1994)
e004=math.log10(equal04/1994)
e0004=math.log10(high04/1994)
e4=-((low04/1994)*e04+(equal04/1994)*e004+(high03/1994)*e0004)
        
print("4.racePctWhite entropy: ",e4)
l1001.append(e4)


x5 = df['racePctAsian']
x05 = x5.to_list()
# print(x05)
sum05=0
for i in range(n):
    sum05=sum05+x05[i]
avg05=sum05/n
print("5.racePctAsian Average: ",avg05)

low05=0
equal05=0
high05=0
for i in range(n):
    if(x05[i]>avg05):
       high05=high05+1
    elif(x05[i]!=0 and x05[i]<avg05):
        low05=low05+1

    else:
         equal05=equal05+1

print(low05,equal05,high05)
e05=math.log10(low05/1994)
e005=math.log10(equal05/1994)
e0005=math.log10(high05/1994)
e5=-((low05/1994)*e05+(equal05/1994)*e005+(high05/1994)*e0005)
        
print("5.racePctAsian entropy: ",e5)
l1001.append(e5)


x6 = df['racePctHisp']
x06 = x6.to_list()
# print(x06)
sum06=0
for i in range(n):
    sum06=sum06+x06[i]
avg06=sum06/n
print("6.racePctHisp Average: ",avg06)

low06=0
equal06=0
high06=0
for i in range(n):
    if(x06[i]>avg06):
       high06=high06+1
    elif(x06[i]!=0 and x06[i]<avg06):
        low06=low06+1

    else:
         equal06=equal06+1

print(low06,equal06,high06)
e06=math.log10(low06/1994)
e006=math.log10(equal06/1994)
e0006=math.log10(high06/1994)
e6=-((low06/1994)*e06+(equal06/1994)*e006+(high06/1994)*e0006)
        
print("6.racePctHisp entropy: ",e6)
l1001.append(e6)



x7 = df['agePct12t21']
x07 = x7.to_list()
# print(x07)
sum07=0
for i in range(n):
    sum07=sum07+x07[i]
avg07=sum07/n
print("7.agePct12t21 Average: ",avg07)
low07=0
equal07=0
high07=0
for i in range(n):
    if(x07[i]>avg07):
       high07=high07+1
    elif(x07[i]!=0 and x07[i]<avg07):
        low07=low07+1

    else:
         equal07=equal07+1

print(low07,equal07,high07)
e07=math.log10(low07/1994)
e007=math.log10(equal07/1994)
e0007=math.log10(high07/1994)
e7=-((low07/1994)*e07+(equal07/1994)*e007+(high07/1994)*e0007)
        
print("7.agePct12t21 entropy: ",e7)
l1001.append(e7)


x8 = df['agePct12t29']
x08 = x8.to_list()
# print(x08)
sum08=0
for i in range(n):
    sum08=sum08+x08[i]
avg08=sum08/n
print("8.agePct12t29 Average: ",avg08)
low08=0
equal08=0
high08=0
for i in range(n):
    if(x08[i]>avg08):
       high08=high08+1
    elif(x08[i]!=0 and x08[i]<avg08):
        low08=low08+1

    else:
         equal08=equal08+1

print(low08,equal08,high08)
e08=math.log10(low08/1994)
e008=math.log10(equal08/1994)
e0008=math.log10(high08/1994)
e8=-((low08/1994)*e08+(equal08/1994)*e008+(high08/1994)*e0008)
        
print("8.agePct12t29 entropy: ",e8)
l1001.append(e8)



x9 = df['agePct16t24']
x09 = x9.to_list()
# print(x09)
sum09=0
for i in range(n):
    sum09=sum09+x09[i]
avg09=sum09/n
print("9.agePct16t24 Average: ",avg09)
low09=0
equal09=0
high09=0
for i in range(n):
    if(x09[i]>avg09):
       high09=high09+1
    elif(x09[i]!=0 and x09[i]<avg09):
        low09=low09+1

    else:
         equal09=equal09+1

print(low09,equal09,high09)
e09=math.log10(low09/1994)
e009=math.log10(equal09/1994)
e0009=math.log10(high09/1994)
e9=-((low09/1994)*e09+(equal09/1994)*e009+(high09/1994)*e0009)
        
print("9.agePct16t24 entropy: ",e9)
l1001.append(e9)


x10 = df['agePct65aup']
x010 = x10.to_list()
# print(x010)
sum010=0
for i in range(n):
    sum010=sum010+x010[i]
avg010=sum010/n
print("10.agePct65aup Average: ",avg010)
low010=0
equal010=0
high010=0
for i in range(n):
    if(x010[i]>avg010):
       high010=high010+1
    elif(x010[i]!=0 and x010[i]<avg010):
        low010=low010+1

    else:
         equal010=equal010+1

print(low010,equal010,high010)
e010=math.log10(low010/1994)
e0010=math.log10(equal010/1994)
e00010=math.log10(high010/1994)
e10=-((low010/1994)*e010+(equal010/1994)*e0010+(high010/1994)*e00010)
        
print("10.agePct65aup entropy: ",e10)
l1001.append(e10)


x11 = df['numbUrban']
x011 = x11.to_list()
# print(x011)
sum011=0
for i in range(n):
    sum011=sum011+x011[i]
avg011=sum011/n
print("11.numbUrban Average: ",avg011)
low011=0
equal011=0
high011=0
for i in range(n):
    if(x011[i]>avg011):
       high011=high011+1
    elif(x011[i]!=0 and x011[i]<avg011):
        low011=low011+1

    else:
         equal011=equal011+1

print(low011,equal011,high011)
e011=math.log10(low011/1994)
e0011=math.log10(equal011/1994)
e00011=math.log10(high011/1994)
e11=-((low011/1994)*e011+(equal011/1994)*e0011+(high011/1994)*e00011)
        
print("11.numbUrban entropy: ",e11)
l1001.append(e11)


x12 = df['medIncome']
x012 = x12.to_list()
# print(x012)
sum012=0
for i in range(n):
    sum012=sum012+x012[i]
avg012=sum012/n
print("12.medIncome Average: ",avg012)
low012=0
equal012=0
high012=0
for i in range(n):
    if(x012[i]>avg012):
       high012=high012+1
    elif(x012[i]!=0 and x012[i]<avg012):
        low012=low012+1

    else:
         equal012=equal012+1

print(low012,equal012,high012)
e012=math.log10(low012/1994)
e0012=math.log10(equal012/1994)
e00012=math.log10(high012/1994)
e12=-((low012/1994)*e012+(equal012/1994)*e0012+(high012/1994)*e00012)
        
print("12.medIncome entropy: ",e12)
l1001.append(e12)



x13 = df['pctWWage']
x013 = x13.to_list()
# print(x013)
sum013=0
for i in range(n):
    sum013=sum013+x013[i]
avg013=sum013/n
print("13.pctWWage Average: ",avg013)
low013=0
equal013=0
high013=0
for i in range(n):
    if(x013[i]>avg013):
       high013=high013+1
    elif(x013[i]!=0 and x013[i]<avg013):
        low013=low013+1

    else:
         equal013=equal013+1

print(low013,equal013,high013)
e013=math.log10(low013/1994)
e0013=math.log10(equal013/1994)
e00013=math.log10(high013/1994)
e13=-((low013/1994)*e013+(equal013/1994)*e0013+(high013/1994)*e00013)
        
print("13.pctWWage entropy: ",e13)
l1001.append(e13)


x14 = df['pctWFarmSelf']
x014 = x14.to_list()
# print(x014)
sum014=0
for i in range(n):
    sum014=sum014+x014[i]
avg014=sum014/n
print("14.pctWFarmSelf Average: ",avg014)
low014=0
equal014=0
high014=0
for i in range(n):
    if(x014[i]>avg014):
       high014=high014+1
    elif(x014[i]!=0 and x014[i]<avg014):
        low014=low014+1

    else:
         equal014=equal014+1

print(low014,equal014,high014)
e014=math.log10(low014/1994)
e0014=math.log10(equal014/1994)
e00014=math.log10(high014/1994)
e14=-((low014/1994)*e014+(equal014/1994)*e0014+(high014/1994)*e00014)
        
print("14.pctWFarmSelf entropy: ",e14)
l1001.append(e14)


x15 = df['pctWInvInc']
x015 = x15.to_list()
# print(x015)
sum015=0
for i in range(n):
    sum015=sum015+x015[i]
avg015=sum015/n
print("15.pctWInvInc Average: ",avg015)
low015=0
equal015=0
high015=0
for i in range(n):
    if(x015[i]>avg015):
       high015=high015+1
    elif(x015[i]!=0 and x015[i]<avg015):
        low015=low015+1

    else:
         equal015=equal015+1

print(low015,equal015,high015)
e015=math.log10(low015/1994)
e0015=math.log10(equal015/1994)
e00015=math.log10(high015/1994)
e15=-((low015/1994)*e015+(equal015/1994)*e0015+(high015/1994)*e00015)
        
print("15.pctWInvInc entropy: ",e15)
l1001.append(e15)


x16 = df['pctWSocSec']
x016 = x16.to_list()
# print(x016)
sum016=0
for i in range(n):
    sum016=sum016+x016[i]
avg016=sum016/n
print("16.pctWSocSec Average: ",avg016)
low016=0
equal016=0
high016=0
for i in range(n):
    if(x016[i]>avg016):
       high016=high016+1
    elif(x016[i]!=0 and x016[i]<avg016):
        low016=low016+1

    else:
         equal016=equal016+1

print(low016,equal016,high016)
e016=math.log10(low016/1994)
e0016=math.log10(equal016/1994)
e00016=math.log10(high016/1994)
e16=-((low016/1994)*e016+(equal016/1994)*e0016+(high016/1994)*e00016)
        
print("16.pctWSocSec entropy: ",e16)
l1001.append(e16)


x17 = df['pctWPubAsst']
x017 = x17.to_list()
# print(x017)
sum017=0
for i in range(n):
    sum017=sum017+x017[i]
avg017=sum017/n
print("17.pctWPubAsst Average: ",avg017)
low017=0
equal017=0
high017=0
for i in range(n):
    if(x017[i]>avg017):
       high017=high017+1
    elif(x017[i]!=0 and x017[i]<avg017):
        low017=low017+1

    else:
         equal017=equal017+1

print(low017,equal017,high017)
e017=math.log10(low017/1994)
e0017=math.log10(equal017/1994)
e00017=math.log10(high017/1994)
e17=-((low017/1994)*e017+(equal017/1994)*e0017+(high017/1994)*e00017)
        
print("17.pctWPubAsst entropy: ",e17)
l1001.append(e17)


x18 = df['pctWRetire']
x018 = x18.to_list()
# print(x018)
sum018=0
for i in range(n):
    sum018=sum018+x018[i]
avg018=sum018/n
print("18.pctWRetire Average: ",avg018)
low018=0
equal018=0
high018=0
for i in range(n):
    if(x018[i]>avg018):
       high018=high018+1
    elif(x018[i]!=0 and x018[i]<avg018):
        low018=low018+1

    else:
         equal018=equal018+1

print(low018,equal018,high018)
e018=math.log10(low018/1994)
e0018=math.log10(equal018/1994)
e00018=math.log10(high018/1994)
e18=-((low018/1994)*e018+(equal018/1994)*e0018+(high018/1994)*e00018)
        
print("18.pctWRetire entropy: ",e18)
l1001.append(e18)



x19 = df['medFamInc']
x019 = x19.to_list()
# print(x019)
sum019=0
for i in range(n):
    sum019=sum019+x019[i]
avg019=sum019/n
print("19.medFamInc Average: ",avg019)
low019=0
equal019=0
high019=0
for i in range(n):
    if(x019[i]>avg019):
       high019=high019+1
    elif(x019[i]!=0 and x019[i]<avg019):
        low019=low019+1

    else:
         equal019=equal019+1

print(low019,equal019,high019)
e019=math.log10(low019/1994)
e0019=math.log10(equal019/1994)
e00019=math.log10(high019/1994)
e19=-((low019/1994)*e019+(equal019/1994)*e0019+(high019/1994)*e00019)
        
print("19.medFamInc entropy: ",e19)
l1001.append(e19)




x20 = df['perCapInc']
x020 = x20.to_list()
# print(x020)
sum020=0
for i in range(n):
    sum020=sum020+x020[i]
avg020=sum020/n
print("20.perCapInc Average: ",avg020)
low020=0
equal020=0
high020=0
for i in range(n):
    if(x020[i]>avg020):
       high020=high020+1
    elif(x020[i]!=0 and x020[i]<avg020):
        low020=low020+1

    else:
         equal020=equal020+1

print(low020,equal020,high020)
e020=math.log10(low020/1994)
e0020=math.log10(equal020/1994)
e00020=math.log10(high020/1994)
e20=-((low020/1994)*e020+(equal020/1994)*e0020+(high020/1994)*e00020)
        
print("20.perCapInc entropy: ",e20)
l1001.append(e20)


x21 = df['whitePerCap']
x021 = x21.to_list()
# print(x021)
sum021=0
for i in range(n):
    sum021=sum021+x021[i]
avg021=sum021/n
print("21.whitePerCap Average: ",avg021)
low021=0
equal021=0
high021=0
for i in range(n):
    if(x021[i]>avg021):
       high021=high021+1
    elif(x021[i]!=0 and x021[i]<avg021):
        low021=low021+1

    else:
         equal021=equal021+1

print(low021,equal021,high021)
e021=math.log10(low021/1994)
e0021=math.log10(equal021/1994)
e00021=math.log10(high021/1994)
e21=-((low021/1994)*e021+(equal021/1994)*e0021+(high021/1994)*e00021)
        
print("21.whitePerCap entropy: ",e21)
l1001.append(e21)


x22 = df['blackPerCap']
x022 = x22.to_list()
# print(x022)
sum022=0
for i in range(n):
    sum022=sum022+x022[i]
avg022=sum022/n
print("22.blackPerCap Average: ",avg022)
low022=0
equal022=0
high022=0
for i in range(n):
    if(x022[i]>avg022):
       high022=high022+1
    elif(x022[i]!=0 and x022[i]<avg022):
        low022=low022+1

    else:
         equal022=equal022+1

print(low022,equal022,high022)
e022=math.log10(low022/1994)
e0022=math.log10(equal022/1994)
e00022=math.log10(high022/1994)
e22=-((low022/1994)*e022+(equal022/1994)*e0022+(high022/1994)*e00022)
        
print("22.blackPerCap entropy: ",e22)
l1001.append(e22)


x23 = df['indianPerCap']
x023 = x23.to_list()
# print(x023)
sum023=0
for i in range(n):
    sum023=sum023+x023[i]
avg023=sum023/n
print("23.indianPerCap Average: ",avg023)
low023=0
equal023=0
high023=0
for i in range(n):
    if(x023[i]>avg023):
       high023=high023+1
    elif(x023[i]!=0 and x023[i]<avg023):
        low023=low023+1

    else:
         equal023=equal023+1

print(low023,equal023,high023)
e023=math.log10(low023/1994)
e0023=math.log10(equal023/1994)
e00023=math.log10(high023/1994)
e23=-((low023/1994)*e023+(equal023/1994)*e0023+(high023/1994)*e00023)
        
print("23.indianPerCap entropy: ",e23)
l1001.append(e23)


x24 = df['AsianPerCap']
x024 = x24.to_list()
# print(x024)
sum024=0
for i in range(n):
    sum024=sum024+x024[i]
avg024=sum024/n
print("24.AsianPerCap Average: ",avg024)
low024=0
equal024=0
high024=0
for i in range(n):
    if(x024[i]>avg024):
       high024=high024+1
    elif(x024[i]!=0 and x024[i]<avg024):
        low024=low024+1

    else:
         equal024=equal024+1

print(low024,equal024,high024)
e024=math.log10(low024/1994)
e0024=math.log10(equal024/1994)
e00024=math.log10(high024/1994)
e24=-((low024/1994)*e024+(equal024/1994)*e0024+(high024/1994)*e00024)
        
print("24.AsianPerCap entropy: ",e24)
l1001.append(e24)


x25 = df['OtherPerCap']
x025 = x25.to_list()
# print(x025)
sum025=0
for i in range(n):
    sum025=sum025+x025[i]
avg025=sum025/n
print("25.OtherPerCap Average: ",avg025)
low025=0
equal025=0
high025=0
for i in range(n):
    if(x025[i]>avg025):
       high025=high025+1
    elif(x025[i]!=0 and x025[i]<avg025):
        low025=low025+1

    else:
         equal025=equal025+1

print(low025,equal025,high025)
e025=math.log10(low025/1994)
e0025=math.log10(equal025/1994)
e00025=math.log10(high025/1994)
e25=-((low025/1994)*e025+(equal025/1994)*e0025+(high025/1994)*e00025)
        
print("25.OtherPerCap entropy: ",e25)
l1001.append(e25)


x26 = df['HispPerCap']
x026 = x26.to_list()
# print(x026)
sum026=0
for i in range(n):
    sum026=sum026+x026[i]
avg026=sum026/n
print("26.HispPerCap Average: ",avg026)
low026=0
equal026=0
high026=0
for i in range(n):
    if(x026[i]>avg026):
       high026=high026+1
    elif(x026[i]!=0 and x026[i]<avg026):
        low026=low026+1

    else:
         equal026=equal026+1

print(low026,equal026,high026)
e026=math.log10(low026/1994)
e0026=math.log10(equal026/1994)
e00026=math.log10(high026/1994)
e26=-((low026/1994)*e026+(equal026/1994)*e0026+(high026/1994)*e00026)
        
print("26.HispPerCap entropy: ",e26)
l1001.append(e26)


x27 = df['PctPopUnderPov']
x027 = x27.to_list()
# print(x027)
sum027=0
for i in range(n):
    sum027=sum027+x027[i]
avg027=sum027/n
print("27.PctPopUnderPov Average: ",avg027)
low027=0
equal027=0
high027=0
for i in range(n):
    if(x027[i]>avg027):
       high027=high027+1
    elif(x027[i]!=0 and x027[i]<avg027):
        low027=low027+1

    else:
         equal027=equal027+1

print(low027,equal027,high027)
e027=math.log10(low027/1994)
e0027=math.log10(equal027/1994)
e00027=math.log10(high027/1994)
e27=-((low027/1994)*e027+(equal027/1994)*e0027+(high027/1994)*e00027)
        
print("27.PctPopUnderPov entropy: ",e27)
l1001.append(e27)


x28 = df['PctLess9thGrade']
x028 = x28.to_list()
# print(x028)
sum028=0
for i in range(n):
    sum028=sum028+x028[i]
avg028=sum028/n
print("28.PctLess9thGrade Average: ",avg028)
low028=0
equal028=0
high028=0
for i in range(n):
    if(x028[i]>avg028):
       high028=high028+1
    elif(x028[i]!=0 and x028[i]<avg028):
        low028=low028+1

    else:
         equal028=equal028+1

print(low028,equal028,high028)
e028=math.log10(low028/1994)
e0028=math.log10(equal028/1994)
e00028=math.log10(high028/1994)
e28=-((low028/1994)*e028+(equal028/1994)*e0028+(high028/1994)*e00028)
        
print("28.PctLess9thGrade entropy: ",e28)
l1001.append(e28)


x29 = df['PctNotHSGrad']
x029 = x29.to_list()
# print(x029)
sum029=0
for i in range(n):
    sum029=sum029+x029[i]
avg029=sum029/n
print("29.PctNotHSGrad Average: ",avg029)
low029=0
equal029=0
high029=0
for i in range(n):
    if(x029[i]>avg029):
       high029=high029+1
    elif(x029[i]!=0 and x029[i]<avg029):
        low029=low029+1

    else:
         equal029=equal029+1

print(low029,equal029,high029)
e029=math.log10(low029/1994)
e0029=math.log10(equal029/1994)
e00029=math.log10(high029/1994)
e29=-((low029/1994)*e029+(equal029/1994)*e0029+(high029/1994)*e00029)
        
print("29.PctNotHSGrad entropy: ",e29)
l1001.append(e29)


x30 = df['PctBSorMore']
x030 = x30.to_list()
# print(x030)
sum030=0
for i in range(n):
    sum030=sum030+x030[i]
avg030=sum030/n
print("30.PctBSorMore Average: ",avg030)
low030=0
equal030=0
high030=0
for i in range(n):
    if(x030[i]>avg030):
       high030=high030+1
    elif(x030[i]!=0 and x030[i]<avg030):
        low030=low030+1

    else:
         equal030=equal030+1

print(low030,equal030,high030)
e030=math.log10(low030/1994)
e0030=math.log10(equal030/1994)
e00030=math.log10(high030/1994)
e30=-((low030/1994)*e030+(equal030/1994)*e0030+(high030/1994)*e00030)
        
print("30.PctBSorMore entropy: ",e30)
l1001.append(e30)


x31 = df['PctUnemployed']
x031 = x31.to_list()
# print(x031)
sum031=0
for i in range(n):
    sum031=sum031+x031[i]
avg031=sum031/n
print("31.PctUnemployed Average: ",avg031)
low031=0
equal031=0
high031=0
for i in range(n):
    if(x031[i]>avg031):
       high031=high031+1
    elif(x031[i]!=0 and x031[i]<avg031):
        low031=low031+1

    else:
         equal031=equal031+1

print(low031,equal031,high031)
e031=math.log10(low031/1994)
e0031=math.log10(equal031/1994)
e00031=math.log10(high031/1994)
e31=-((low031/1994)*e031+(equal031/1994)*e0031+(high031/1994)*e00031)
        
print("31.PctUnemployed entropy: ",e31)
l1001.append(e31)


x32 = df['PctEmploy']
x032 = x32.to_list()
# print(x032)
sum032=0
for i in range(n):
    sum032=sum032+x032[i]
avg032=sum032/n
print("32.PctEmploy Average: ",avg032)
low032=0
equal032=0
high032=0
for i in range(n):
    if(x032[i]>avg032):
       high032=high032+1
    elif(x032[i]!=0 and x032[i]<avg032):
        low032=low032+1

    else:
         equal032=equal032+1

print(low032,equal032,high032)
e032=math.log10(low032/1994)
e0032=math.log10(equal032/1994)
e00032=math.log10(high032/1994)
e32=-((low032/1994)*e032+(equal032/1994)*e0032+(high032/1994)*e00032)
        
print("32.PctEmploy entropy: ",e32)
l1001.append(e32)


x33 = df['PctEmplManu']
x033 = x33.to_list()
# print(x033)
sum033=0
for i in range(n):
    sum033=sum033+x033[i]
avg033=sum033/n
print("33.PctEmplManu Average: ",avg033)
low033=0
equal033=0
high033=0
for i in range(n):
    if(x033[i]>avg033):
       high033=high033+1
    elif(x033[i]!=0 and x033[i]<avg033):
        low033=low033+1

    else:
         equal033=equal033+1

print(low033,equal033,high033)
e033=math.log10(low033/1994)
e0033=math.log10(equal033/1994)
e00033=math.log10(high033/1994)
e33=-((low033/1994)*e033+(equal033/1994)*e0033+(high033/1994)*e00033)
        
print("33.PctEmplManu entropy: ",e33)
l1001.append(e33)



x34 = df['PctEmplProfServ']
x034 = x34.to_list()
# print(x034)
sum034=0
for i in range(n):
    sum034=sum034+x034[i]
avg034=sum034/n
print("34.PctEmplProfServ Average: ",avg034)
low034=0
equal034=0
high034=0
for i in range(n):
    if(x034[i]>avg034):
       high034=high034+1
    elif(x034[i]!=0 and x034[i]<avg034):
        low034=low034+1

    else:
        equal034=equal034+1

print(low034,equal034,high034)
e034=math.log10(low034/1994)
e0034=math.log10(equal034/1994)
e00034=math.log10(high034/1994)
e34=-((low034/1994)*e034+(equal034/1994)*e0034+(high034/1994)*e00034)
        
print("34.PctEmplProfServ entropy: ",e34)
l1001.append(e34)



x35 = df['PctOccupManu']
x035 = x35.to_list()
# print(x035)
sum035=0
for i in range(n):
    sum035=sum035+x035[i]
avg035=sum035/n
print("35.PctOccupManu Average: ",avg035)
low035=0
equal035=0
high035=0
for i in range(n):
    if(x035[i]>avg035):
       high035=high035+1
    elif(x035[i]!=0 and x035[i]<avg035):
        low035=low035+1

    else:
         equal035=equal035+1

print(low035,equal035,high035)
e035=math.log10(low035/1994)
e0035=math.log10(equal035/1994)
e00035=math.log10(high035/1994)
e35=-((low035/1994)*e035+(equal035/1994)*e0035+(high035/1994)*e00035)
        
print("35.PctOccupManu entropy: ",e35)
l1001.append(e35)


x36 = df['PctOccupMgmtProf']
x036 = x36.to_list()
# print(x036)
sum036=0
for i in range(n):
    sum036=sum036+x036[i]
avg036=sum036/n
print("36.PctOccupMgmtProf Average: ",avg036)
low036=0
equal036=0
high036=0
for i in range(n):
    if(x036[i]>avg036):
       high036=high036+1
    elif(x036[i]!=0 and x036[i]<avg036):
        low036=low036+1

    else:
         equal036=equal036+1

print(low036,equal036,high036)
e036=math.log10(low036/1994)
e0036=math.log10(equal036/1994)
e00036=math.log10(high036/1994)
e36=-((low036/1994)*e036+(equal036/1994)*e0036+(high036/1994)*e00036)
        
print("36.PctOccupMgmtProf entropy: ",e36)
l1001.append(e36)


x37 = df['MalePctDivorce']
x037 = x37.to_list()
# print(x037)
sum037=0
for i in range(n):
    sum037=sum037+x037[i]
avg037=sum037/n
print("37.MalePctDivorce Average: ",avg037)
low037=0
equal037=0
high037=0
for i in range(n):
    if(x037[i]>avg037):
       high037=high037+1
    elif(x037[i]!=0 and x037[i]<avg037):
        low037=low037+1

    else:
         equal037=equal037+1

print(low037,equal037,high037)
e037=math.log10(low037/1994)
e0037=math.log10(equal037/1994)
e00037=math.log10(high037/1994)
e37=-((low037/1994)*e037+(equal037/1994)*e0037+(high037/1994)*e00037)
        
print("37.MalePctDivorce entropy: ",e37)
l1001.append(e37)


x38 = df['MalePctNevMarr']
x038 = x38.to_list()
# print(x038)
sum038=0
for i in range(n):
    sum038=sum038+x038[i]
avg038=sum038/n
print("38.MalePctNevMarr Average: ",avg038)
low038=0
equal038=0
high038=0
for i in range(n):
    if(x038[i]>avg038):
       high038=high038+1
    elif(x038[i]!=0 and x038[i]<avg038):
        low038=low038+1

    else:
         equal038=equal038+1

print(low038,equal038,high038)
e038=math.log10(low038/1994)
e0038=math.log10(equal038/1994)
e00038=math.log10(high038/1994)
e38=-((low038/1994)*e038+(equal038/1994)*e0038+(high038/1994)*e00038)
        
print("38.MalePctNevMarr entropy: ",e38)
l1001.append(e38)


x39 = df['FemalePctDiv']
x039 = x39.to_list()
# print(x039)
sum039=0
for i in range(n):
    sum039=sum039+x039[i]
avg039=sum039/n
print("39.FemalePctDiv Average: ",avg039)
low039=0
equal039=0
high039=0
for i in range(n):
    if(x039[i]>avg039):
       high039=high039+1
    elif(x039[i]!=0 and x039[i]<avg039):
        low039=low039+1

    else:
         equal039=equal039+1

print(low039,equal039,high039)
e039=math.log10(low039/1994)
e0039=math.log10(equal039/1994)
e00039=math.log10(high039/1994)
e39=-((low039/1994)*e039+(equal039/1994)*e0039+(high039/1994)*e00039)
        
print("39.FemalePctDiv entropy: ",e39)
l1001.append(e39)


x40 = df['TotalPctDiv']
x040 = x40.to_list()
# print(x040)
sum040=0
for i in range(n):
    sum040=sum040+x040[i]
avg040=sum040/n
print("40.TotalPctDiv Average: ",avg040)
low040=0
equal040=0
high040=0
for i in range(n):
    if(x040[i]>avg040):
       high040=high040+1
    elif(x040[i]!=0 and x040[i]<avg040):
        low040=low040+1

    else:
         equal040=equal040+1

print(low040,equal040,high040)
e040=math.log10(low040/1994)
e0040=math.log10(equal040/1994)
e00040=math.log10(high040/1994)
e40=-((low040/1994)*e040+(equal040/1994)*e0040+(high040/1994)*e00040)
        
print("40.TotalPctDiv entropy: ",e40)
l1001.append(e40)



x41 = df['PersPerFam']
x041 = x41.to_list()
# print(x041)
sum041=0
for i in range(n):
    sum041=sum041+x041[i]
avg041=sum041/n
print("41.PersPerFam Average: ",avg041)
low041=0
equal041=0
high041=0
for i in range(n):
    if(x041[i]>avg041):
       high041=high041+1
    elif(x041[i]!=0 and x041[i]<avg041):
        low041=low041+1

    else:
         equal041=equal041+1

print(low041,equal041,high041)
e041=math.log10(low041/1994)
e0041=math.log10(equal041/1994)
e00041=math.log10(high041/1994)
e41=-((low041/1994)*e041+(equal041/1994)*e0041+(high041/1994)*e00041)
        
print("41.PersPerFam entropy: ",e41)
l1001.append(e41)


x42 = df['PctFam2Par']
x042 = x42.to_list()
# print(x042)
sum042=0
for i in range(n):
    sum042=sum042+x042[i]
avg042=sum042/n
print("42.PctFam2Par Average: ",avg042)
low042=0
equal042=0
high042=0
for i in range(n):
    if(x042[i]>avg042):
       high042=high042+1
    elif(x042[i]!=0 and x042[i]<avg042):
        low042=low042+1

    else:
         equal042=equal042+1

print(low042,equal042,high042)
e042=math.log10(low042/1994)
e0042=math.log10(equal042/1994)
e00042=math.log10(high042/1994)
e42=-((low042/1994)*e042+(equal042/1994)*e0042+(high042/1994)*e00042)
        
print("42.PctFam2Par entropy: ",e42)
l1001.append(e42)



x43 = df['PctKids2Par']
x043 = x43.to_list()
# print(x043)
sum043=0
for i in range(n):
    sum043=sum043+x043[i]
avg043=sum043/n
print("43.PctKids2Par Average: ",avg043)
low043=0
equal043=0
high043=0
for i in range(n):
    if(x043[i]>avg043):
       high043=high043+1
    elif(x043[i]!=0 and x043[i]<avg043):
        low043=low043+1

    else:
         equal043=equal043+1

print(low043,equal043,high043)
e043=math.log10(low043/1994)
e0043=math.log10(equal043/1994)
e00043=math.log10(high043/1994)
e43=-((low043/1994)*e043+(equal043/1994)*e0043+(high043/1994)*e00043)
        
print("43.PctKids2Par entropy: ",e43)
l1001.append(e43)


x44 = df['PctYoungKids2Par']
x044 = x44.to_list()
# print(x044)
sum044=0
for i in range(n):
    sum044=sum044+x044[i]
avg044=sum044/n
print("44.PctYoungKids2Par Average: ",avg044)
low044=0
equal044=0
high044=0
for i in range(n):
    if(x044[i]>avg044):
       high044=high044+1
    elif(x044[i]!=0 and x044[i]<avg044):
        low044=low044+1

    else:
         equal044=equal044+1

print(low044,equal044,high044)
e044=math.log10(low044/1994)
e0044=math.log10(equal044/1994)
e00044=math.log10(high044/1994)
e44=-((low044/1994)*e044+(equal044/1994)*e0044+(high044/1994)*e00044)
        
print("44.PctYoungKids2Par entropy: ",e44)
l1001.append(e44)



x45 = df['PctTeen2Par']
x045 = x45.to_list()
# print(x045)
sum045=0
for i in range(n):
    sum045=sum045+x045[i]
avg045=sum045/n
print("45.PctTeen2Par Average: ",avg045)
low045=0
equal045=0
high045=0
for i in range(n):
    if(x045[i]>avg045):
       high045=high045+1
    elif(x045[i]!=0 and x045[i]<avg045):
        low045=low045+1

    else:
         equal045=equal045+1

print(low045,equal045,high045)
e045=math.log10(low045/1994)
e0045=math.log10(equal045/1994)
e00045=math.log10(high045/1994)
e45=-((low045/1994)*e045+(equal045/1994)*e0045+(high045/1994)*e00045)
        
print("45.PctTeen2Par entropy: ",e45)
l1001.append(e45)



x46 = df['PctWorkMomYoungKids']
x046 = x46.to_list()
# print(x046)
sum046=0
for i in range(n):
    sum046=sum046+x046[i]
avg046=sum046/n
print("46.PctWorkMomYoungKids Average: ",avg046)
low046=0
equal046=0
high046=0
for i in range(n):
    if(x046[i]>avg046):
       high046=high046+1
    elif(x046[i]!=0 and x046[i]<avg046):
        low046=low046+1

    else:
         equal046=equal046+1

print(low046,equal046,high046)
e046=math.log10(low046/1994)
e0046=math.log10(equal046/1994)
e00046=math.log10(high046/1994)
e46=-((low046/1994)*e046+(equal046/1994)*e0046+(high046/1994)*e00046)
        
print("46.PctWorkMomYoungKids entropy: ",e46)
l1001.append(e46)



x47 = df['PctWorkMom']
x047 = x47.to_list()
# print(x047)
sum047=0
for i in range(n):
    sum047=sum047+x047[i]
avg047=sum047/n
print("47.PctWorkMom Average: ",avg047)
low047=0
equal047=0
high047=0
for i in range(n):
    if(x047[i]>avg047):
       high047=high047+1
    elif(x047[i]!=0 and x047[i]<avg047):
        low047=low047+1

    else:
         equal047=equal047+1

print(low047,equal047,high047)
e047=math.log10(low047/1994)
e0047=math.log10(equal047/1994)
e00047=math.log10(high047/1994)
e47=-((low047/1994)*e047+(equal047/1994)*e0047+(high047/1994)*e00047)
        
print("47.PctWorkMom entropy: ",e47)
l1001.append(e47)


x48 = df['NumIlleg']
x048 = x48.to_list()
# print(x048)
sum048=0
for i in range(n):
    sum048=sum048+x048[i]
avg048=sum048/n
print("48.NumIlleg Average: ",avg048)
low048=0
equal048=0
high048=0
for i in range(n):
    if(x048[i]>avg048):
       high048=high048+1
    elif(x048[i]!=0 and x048[i]<avg048):
        low048=low048+1

    else:
         equal048=equal048+1

print(low048,equal048,high048)
e048=math.log10(low048/1994)
e0048=math.log10(equal048/1994)
e00048=math.log10(high048/1994)
e48=-((low048/1994)*e048+(equal048/1994)*e0048+(high048/1994)*e00048)
        
print("48.NumIlleg entropy: ",e48)
l1001.append(e48)



x49 = df['PctIlleg']
x049 = x49.to_list()
# print(x049)
sum049=0
for i in range(n):
    sum049=sum049+x049[i]
avg049=sum049/n
print("49.PctIlleg Average: ",avg049)
low049=0
equal049=0
high049=0
for i in range(n):
    if(x049[i]>avg049):
       high049=high049+1
    elif(x049[i]!=0 and x049[i]<avg049):
        low049=low049+1

    else:
         equal049=equal049+1

print(low049,equal049,high049)
e049=math.log10(low049/1994)
e0049=math.log10(equal049/1994)
e00049=math.log10(high049/1994)
e49=-((low049/1994)*e049+(equal049/1994)*e0049+(high049/1994)*e00049)
        
print("49.PctIlleg entropy: ",e49)
l1001.append(e49)


x50 = df['NumImmig']
x050 = x50.to_list()
# print(x050)
sum050=0
for i in range(n):
    sum050=sum050+x050[i]
avg050=sum050/n
print("50.NumImmig Average: ",avg050)
low050=0
equal050=0
high050=0
for i in range(n):
    if(x050[i]>avg050):
       high050=high050+1
    elif(x050[i]!=0 and x050[i]<avg050):
        low050=low050+1

    else:
         equal050=equal050+1

print(low050,equal050,high050)
e050=math.log10(low050/1994)
e0050=math.log10(equal050/1994)
e00050=math.log10(high050/1994)
e50=-((low050/1994)*e050+(equal050/1994)*e0050+(high050/1994)*e00050)
        
print("50.NumImmig entropy: ",e50)
l1001.append(e50)



x51 = df['PctImmigRecent']
x051 = x51.to_list()
# print(x051)
sum051=0
for i in range(n):
    sum051=sum051+x051[i]
avg051=sum051/n
print("51.PctImmigRecent Average: ",avg051)
low051=0
equal051=0
high051=0
for i in range(n):
    if(x051[i]>avg051):
       high051=high051+1
    elif(x051[i]!=0 and x051[i]<avg051):
        low051=low051+1

    else:
         equal051=equal051+1

print(low051,equal051,high051)
e051=math.log10(low051/1994)
e0051=math.log10(equal051/1994)
e00051=math.log10(high051/1994)
e51=-((low051/1994)*e051+(equal051/1994)*e0051+(high051/1994)*e00051)
        
print("51.PctImmigRecent entropy: ",e51)
l1001.append(e51)


x52 = df['PctImmigRec5']
x052 = x52.to_list()
# print(x052)
sum052=0
for i in range(n):
    sum052=sum052+x052[i]
avg052=sum052/n
print("52.PctImmigRec5 Average: ",avg052)
low052=0
equal052=0
high052=0
for i in range(n):
    if(x052[i]>avg052):
       high052=high052+1
    elif(x052[i]!=0 and x052[i]<avg052):
        low052=low052+1

    else:
         equal052=equal052+1

print(low052,equal052,high052)
e052=math.log10(low052/1994)
e0052=math.log10(equal052/1994)
e00052=math.log10(high052/1994)
e52=-((low052/1994)*e052+(equal052/1994)*e0052+(high052/1994)*e00052)
        
print("52.PctImmigRec5 entropy: ",e52)
l1001.append(e52)



x53 = df['PctImmigRec8']
x053 = x53.to_list()
# print(x053)
sum053=0
for i in range(n):
    sum053=sum053+x053[i]
avg053=sum053/n
print("53.PctImmigRec8 Average: ",avg053)
low053=0
equal053=0
high053=0
for i in range(n):
    if(x053[i]>avg053):
       high053=high053+1
    elif(x053[i]!=0 and x053[i]<avg053):
        low053=low053+1

    else:
         equal053=equal053+1

print(low053,equal053,high053)
e053=math.log10(low053/1994)
e0053=math.log10(equal053/1994)
e00053=math.log10(high053/1994)
e53=-((low053/1994)*e053+(equal053/1994)*e0053+(high053/1994)*e00053)
        
print("53.PctImmigRec8 entropy: ",e53)
l1001.append(e53)



x54 = df['PctImmigRec10']
x054 = x54.to_list()
# print(x054)
sum054=0
for i in range(n):
    sum054=sum054+x054[i]
avg054=sum054/n
print("54.PctImmigRec10 Average: ",avg054)
low054=0
equal054=0
high054=0
for i in range(n):
    if(x054[i]>avg054):
       high054=high054+1
    elif(x054[i]!=0 and x054[i]<avg054):
        low054=low054+1

    else:
         equal054=equal054+1

print(low054,equal054,high054)
e054=math.log10(low054/1994)
e0054=math.log10(equal054/1994)
e00054=math.log10(high054/1994)
e54=-((low054/1994)*e054+(equal054/1994)*e0054+(high054/1994)*e00054)
        
print("54.PctImmigRec10 entropy: ",e54)
l1001.append(e54)



x55 = df['PctRecentImmig']
x055 = x55.to_list()
# print(x055)
sum055=0
for i in range(n):
    sum055=sum055+x055[i]
avg055=sum055/n
print("55.PctRecentImmig Average: ",avg055)
low055=0
equal055=0
high055=0
for i in range(n):
    if(x055[i]>avg055):
       high055=high055+1
    elif(x055[i]!=0 and x055[i]<avg055):
        low055=low055+1

    else:
         equal055=equal055+1

print(low055,equal055,high055)
e055=math.log10(low055/1994)
e0055=math.log10(equal055/1994)
e00055=math.log10(high055/1994)
e55=-((low055/1994)*e055+(equal055/1994)*e0055+(high055/1994)*e00055)
        
print("55.PctRecentImmig entropy: ",e55)
l1001.append(e55)



x56 = df['PctRecImmig5']
x056 = x56.to_list()
# print(x056)
sum056=0
for i in range(n):
    sum056=sum056+x056[i]
avg056=sum056/n
print("56.PctRecImmig5 Average: ",avg056)
low056=0
equal056=0
high056=0
for i in range(n):
    if(x056[i]>avg056):
       high056=high056+1
    elif(x056[i]!=0 and x056[i]<avg056):
        low056=low056+1

    else:
         equal056=equal056+1

print(low056,equal056,high056)
e056=math.log10(low056/1994)
e0056=math.log10(equal056/1994)
e00056=math.log10(high056/1994)
e56=-((low056/1994)*e056+(equal056/1994)*e0056+(high056/1994)*e00056)
        
print("56.PctRecImmig5 entropy: ",e56)
l1001.append(e56)



x57 = df['PctRecImmig8']
x057 = x57.to_list()
# print(x057)
sum057=0
for i in range(n):
    sum057=sum057+x057[i]
avg057=sum057/n
print("57.PctRecImmig8 Average: ",avg057)
low057=0
equal057=0
high057=0
for i in range(n):
    if(x057[i]>avg057):
       high057=high057+1
    elif(x057[i]!=0 and x057[i]<avg057):
        low057=low057+1

    else:
         equal057=equal057+1

print(low057,equal057,high057)
e057=math.log10(low057/1994)
e0057=math.log10(equal057/1994)
e00057=math.log10(high057/1994)
e57=-((low057/1994)*e057+(equal057/1994)*e0057+(high057/1994)*e00057)
        
print("57.PctRecImmig8 entropy: ",e57)
l1001.append(e57)


x58 = df['PctRecImmig10']
x058 = x58.to_list()
# print(x058)
sum058=0
for i in range(n):
    sum058=sum058+x058[i]
avg058=sum058/n
print("58.PctRecImmig10 Average: ",avg058)
low058=0
equal058=0
high058=0
for i in range(n):
    if(x058[i]>avg058):
       high058=high058+1
    elif(x058[i]!=0 and x058[i]<avg058):
        low058=low058+1

    else:
         equal058=equal058+1

print(low058,equal058,high058)
e058=math.log10(low058/1994)
e0058=math.log10(equal058/1994)
e00058=math.log10(high058/1994)
e58=-((low058/1994)*e058+(equal058/1994)*e0058+(high058/1994)*e00058)
        
print("58.PctRecImmig10 entropy: ",e58)
l1001.append(e58)


x59 = df['PctSpeakEnglOnly']
x059 = x59.to_list()
# print(x059)
sum059=0
for i in range(n):
    sum059=sum059+x059[i]
avg059=sum059/n
print("59.PctSpeakEnglOnly Average: ",avg059)
low059=0
equal059=0
high059=0
for i in range(n):
    if(x059[i]>avg059):
       high059=high059+1
    elif(x059[i]!=0 and x059[i]<avg059):
        low059=low059+1

    else:
         equal059=equal059+1

print(low059,equal059,high059)
e059=math.log10(low059/1994)
e0059=math.log10(equal059/1994)
e00059=math.log10(high059/1994)
e59=-((low059/1994)*e059+(equal059/1994)*e0059+(high059/1994)*e00059)
        
print("59.PctSpeakEnglOnly entropy: ",e59)
l1001.append(e59)



x60 = df['PctNotSpeakEnglWell']
x060 = x60.to_list()
# print(x060)
sum060=0
for i in range(n):
    sum060=sum060+x060[i]
avg060=sum060/n
print("60.PctNotSpeakEnglWell Average: ",avg060)
low060=0
equal060=0
high060=0
for i in range(n):
    if(x060[i]>avg060):
       high060=high060+1
    elif(x060[i]!=0 and x060[i]<avg060):
        low060=low060+1

    else:
         equal060=equal060+1

print(low060,equal060,high060)
e060=math.log10(low060/1994)
e0060=math.log10(equal060/1994)
e00060=math.log10(high060/1994)
e60=-((low060/1994)*e060+(equal060/1994)*e0060+(high060/1994)*e00060)
        
print("60.PctNotSpeakEnglWell entropy: ",e60)
l1001.append(e60)



x61 = df['PctLargHouseFam']
x061 = x61.to_list()
# print(x061)
sum061=0
for i in range(n):
    sum061=sum061+x061[i]
avg061=sum061/n
print("61.PctLargHouseFam Average: ",avg061)
low061=0
equal061=0
high061=0
for i in range(n):
    if(x061[i]>avg061):
       high061=high061+1
    elif(x061[i]!=0 and x061[i]<avg061):
        low061=low061+1

    else:
         equal061=equal061+1

print(low061,equal061,high061)
e061=math.log10(low061/1994)
e0061=math.log10(equal061/1994)
e00061=math.log10(high061/1994)
e61=-((low061/1994)*e061+(equal061/1994)*e0061+(high061/1994)*e00061)
        
print("61.PctLargHouseFam entropy: ",e61)
l1001.append(e61)


x62 = df['PctLargHouseOccup']
x062 = x62.to_list()
# print(x062)
sum062=0
for i in range(n):
    sum062=sum062+x062[i]
avg062=sum062/n
print("62.PctLargHouseOccup Average: ",avg062)
low062=0
equal062=0
high062=0
for i in range(n):
    if(x062[i]>avg062):
       high062=high062+1
    elif(x062[i]!=0 and x062[i]<avg062):
        low062=low062+1

    else:
         equal062=equal062+1

print(low062,equal062,high062)
e062=math.log10(low062/1994)
e0062=math.log10(equal062/1994)
e00062=math.log10(high062/1994)
e62=-((low062/1994)*e062+(equal062/1994)*e0062+(high062/1994)*e00062)
        
print("62.PctLargHouseOccup entropy: ",e62)
l1001.append(e62)



x63 = df['PersPerOccupHous']
x063 = x63.to_list()
# print(x063)
sum063=0
for i in range(n):
    sum063=sum063+x063[i]
avg063=sum063/n
print("63.PersPerOccupHous Average: ",avg063)
low063=0
equal063=0
high063=0
for i in range(n):
    if(x063[i]>avg063):
       high063=high063+1
    elif(x063[i]!=0 and x063[i]<avg063):
        low063=low063+1

    else:
         equal063=equal063+1

print(low063,equal063,high063)
e063=math.log10(low063/1994)
e0063=math.log10(equal063/1994)
e00063=math.log10(high063/1994)
e63=-((low063/1994)*e063+(equal063/1994)*e0063+(high063/1994)*e00063)
        
print("63.PersPerOccupHous entropy: ",e63)
l1001.append(e63)


x64 = df['PersPerOwnOccHous']
x064 = x64.to_list()
# print(x064)
sum064=0
for i in range(n):
    sum064=sum064+x064[i]
avg064=sum064/n
print("64.PersPerOwnOccHous Average: ",avg064)
low064=0
equal064=0
high064=0
for i in range(n):
    if(x064[i]>avg064):
       high064=high064+1
    elif(x064[i]!=0 and x064[i]<avg064):
        low064=low064+1

    else:
         equal064=equal064+1

print(low064,equal064,high064)
e064=math.log10(low064/1994)
e0064=math.log10(equal064/1994)
e00064=math.log10(high064/1994)
e64=-((low064/1994)*e064+(equal064/1994)*e0064+(high064/1994)*e00064)
        
print("64.PersPerOwnOccHous entropy: ",e64)
l1001.append(e64)



x65 = df['PersPerRentOccHous']
x065 = x65.to_list()
# print(x065)
sum065=0
for i in range(n):
    sum065=sum065+x065[i]
avg065=sum065/n
print("65.PersPerRentOccHous Average: ",avg065)
low065=0
equal065=0
high065=0
for i in range(n):
    if(x065[i]>avg065):
       high065=high065+1
    elif(x065[i]!=0 and x065[i]<avg065):
        low065=low065+1

    else:
         equal065=equal065+1

print(low065,equal065,high065)
e065=math.log10(low065/1994)
e0065=math.log10(equal065/1994)
e00065=math.log10(high065/1994)
e65=-((low065/1994)*e065+(equal065/1994)*e0065+(high065/1994)*e00065)
        
print("65.PersPerRentOccHous entropy: ",e65)
l1001.append(e65)



x66 = df['PctPersOwnOccup']
x066 = x66.to_list()
# print(x066)
sum066=0
for i in range(n):
    sum066=sum066+x066[i]
avg066=sum066/n
print("66.PctPersOwnOccup Average: ",avg066)
low066=0
equal066=0
high066=0
for i in range(n):
    if(x066[i]>avg066):
       high066=high066+1
    elif(x066[i]!=0 and x066[i]<avg066):
        low066=low066+1

    else:
         equal066=equal066+1

print(low066,equal066,high066)
e066=math.log10(low066/1994)
e0066=math.log10(equal066/1994)
e00066=math.log10(high066/1994)
e66=-((low066/1994)*e066+(equal066/1994)*e0066+(high066/1994)*e00066)
        
print("66.PctPersOwnOccup entropy: ",e66)
l1001.append(e66)



x67 = df['PctPersDenseHous']
x067 = x67.to_list()
# print(x067)
sum067=0
for i in range(n):
    sum067=sum067+x067[i]
avg067=sum067/n
print("67.PctPersDenseHous Average: ",avg067)
low067=0
equal067=0
high067=0
for i in range(n):
    if(x067[i]>avg067):
       high067=high067+1
    elif(x067[i]!=0 and x067[i]<avg067):
        low067=low067+1

    else:
         equal067=equal067+1

print(low067,equal067,high067)
e067=math.log10(low067/1994)
e0067=math.log10(equal067/1994)
e00067=math.log10(high067/1994)
e67=-((low067/1994)*e067+(equal067/1994)*e0067+(high067/1994)*e00067)
        
print("67.PctPersDenseHous entropy: ",e67)
l1001.append(e67)


x68 = df['PctHousLess3BR']
x068 = x68.to_list()
# print(x068)
sum068=0
for i in range(n):
    sum068=sum068+x068[i]
avg068=sum068/n
print("68.PctHousLess3BR Average: ",avg068)
low068=0
equal068=0
high068=0
for i in range(n):
    if(x068[i]>avg068):
       high068=high068+1
    elif(x068[i]!=0 and x068[i]<avg068):
        low068=low068+1

    else:
         equal068=equal068+1

print(low068,equal068,high068)
e068=math.log10(low068/1994)
e0068=math.log10(equal068/1994)
e00068=math.log10(high068/1994)
e68=-((low068/1994)*e068+(equal068/1994)*e0068+(high068/1994)*e00068)
        
print("68.PctHousLess3BR entropy: ",e68)
l1001.append(e68)


x69 = df['HousVacant']
x069 = x69.to_list()
# print(x069)
sum069=0
for i in range(n):
    sum069=sum069+x069[i]
avg069=sum069/n
print("69.HousVacant Average: ",avg069)
low069=0
equal069=0
high069=0
for i in range(n):
    if(x069[i]>avg069):
       high069=high069+1
    elif(x069[i]!=0 and x069[i]<avg069):
        low069=low069+1

    else:
         equal069=equal069+1

print(low069,equal069,high069)
e069=math.log10(low069/1994)
e0069=math.log10(equal069/1994)
e00069=math.log10(high069/1994)
e69=-((low069/1994)*e069+(equal069/1994)*e0069+(high069/1994)*e00069)
        
print("69.HousVacant entropy: ",e69)
l1001.append(e69)



x70 = df['PctHousOccup']
x070 = x70.to_list()
# print(x070)
sum070=0
for i in range(n):
    sum070=sum070+x070[i]
avg070=sum070/n
print("70.PctHousOccup Average: ",avg070)
low070=0
equal070=0
high070=0
for i in range(n):
    if(x070[i]>avg070):
       high070=high070+1
    elif(x070[i]!=0 and x070[i]<avg070):
        low070=low070+1

    else:
         equal070=equal070+1

print(low070,equal070,high070)
e070=math.log10(low070/1994)
e0070=math.log10(equal070/1994)
e00070=math.log10(high070/1994)
e70=-((low070/1994)*e070+(equal070/1994)*e0070+(high070/1994)*e00070)
        
print("70.PctHousOccup entropy: ",e70)
l1001.append(e70)



x71 = df['PctHousOwnOcc']
x071 = x71.to_list()
# print(x071)
sum071=0
for i in range(n):
    sum071=sum071+x071[i]
avg071=sum071/n
print("71.PctHousOwnOcc Average: ",avg071)
low071=0
equal071=0
high071=0
for i in range(n):
    if(x071[i]>avg071):
       high071=high071+1
    elif(x071[i]!=0 and x071[i]<avg071):
        low071=low071+1

    else:
         equal071=equal071+1

print(low071,equal071,high071)
e071=math.log10(low071/1994)
e0071=math.log10(equal071/1994)
e00071=math.log10(high071/1994)
e71=-((low071/1994)*e071+(equal071/1994)*e0071+(high071/1994)*e00071)
        
print("71.PctHousOwnOcc entropy: ",e71)
l1001.append(e71)



x72 = df['PctVacantBoarded']
x072 = x72.to_list()
# print(x072)
sum072=0
for i in range(n):
    sum072=sum072+x072[i]
avg072=sum072/n
print("72.PctVacantBoarded Average: ",avg072)
low072=0
equal072=0
high072=0
for i in range(n):
    if(x072[i]>avg072):
       high072=high072+1
    elif(x072[i]!=0 and x072[i]<avg072):
        low072=low072+1

    else:
         equal072=equal072+1

print(low072,equal072,high072)
e072=math.log10(low072/1994)
e0072=math.log10(equal072/1994)
e00072=math.log10(high072/1994)
e72=-((low072/1994)*e072+(equal072/1994)*e0072+(high072/1994)*e00072)
        
print("72.PctVacantBoarded entropy: ",e72)
l1001.append(e72)



x73 = df['PctVacMore6Mos']
x073 = x73.to_list()
# print(x073)
sum073=0
for i in range(n):
    sum073=sum073+x073[i]
avg073=sum073/n
print("73.PctVacMore6Mos Average: ",avg073)
low073=0
equal073=0
high073=0
for i in range(n):
    if(x073[i]>avg073):
       high073=high073+1
    elif(x073[i]!=0 and x073[i]<avg073):
        low073=low073+1

    else:
         equal073=equal073+1

print(low073,equal073,high073)
e073=math.log10(low073/1994)
e0073=math.log10(equal073/1994)
e00073=math.log10(high073/1994)
e73=-((low073/1994)*e073+(equal073/1994)*e0073+(high073/1994)*e00073)
        
print("73.PctVacMore6Mos entropy: ",e73)
l1001.append(e73)


x74 = df['MedYrHousBuilt']
x074 = x74.to_list()
# print(x074)
sum074=0
for i in range(n):
    sum074=sum074+x074[i]
avg074=sum074/n
print("74.MedYrHousBuilt Average: ",avg074)
low074=0
equal074=0
high074=0
for i in range(n):
    if(x074[i]>avg074):
       high074=high074+1
    elif(x074[i]!=0 and x074[i]<avg074):
        low074=low074+1

    else:
         equal074=equal074+1

print(low074,equal074,high074)
e074=math.log10(low074/1994)
e0074=math.log10(equal074/1994)
e00074=math.log10(high074/1994)
e74=-((low074/1994)*e074+(equal074/1994)*e0074+(high074/1994)*e00074)
        
print("74.MedYrHousBuilt entropy: ",e74)
l1001.append(e74)



x75 = df['PctHousNoPhone']
x075 = x75.to_list()
# print(x075)
sum075=0
for i in range(n):
    sum075=sum075+x075[i]
avg075=sum075/n
print("75.PctHousNoPhone Average: ",avg075)
low075=0
equal075=0
high075=0
for i in range(n):
    if(x075[i]>avg075):
       high075=high075+1
    elif(x075[i]!=0 and x075[i]<avg075):
        low075=low075+1

    else:
         equal075=equal075+1

print(low075,equal075,high075)
e075=math.log10(low075/1994)
e0075=math.log10(equal075/1994)
e00075=math.log10(high075/1994)
e75=-((low075/1994)*e075+(equal075/1994)*e0075+(high075/1994)*e00075)
        
print("75.PctHousNoPhone entropy: ",e75)
l1001.append(e75)


x76 = df['PctWOFullPlumb']
x076 = x76.to_list()
# print(x076)
sum076=0
for i in range(n):
    sum076=sum076+x076[i]
avg076=sum076/n
print("76.PctWOFullPlumb Average: ",avg076)
low076=0
equal076=0
high076=0
for i in range(n):
    if(x076[i]>avg076):
       high076=high076+1
    elif(x076[i]!=0 and x076[i]<avg076):
        low076=low076+1

    else:
         equal076=equal076+1

print(low076,equal076,high076)
e076=math.log10(low076/1994)
e0076=math.log10(equal076/1994)
e00076=math.log10(high076/1994)
e76=-((low076/1994)*e076+(equal076/1994)*e0076+(high076/1994)*e00076)
        
print("76.PctWOFullPlumb entropy: ",e76)
l1001.append(e76)



x77 = df['OwnOccLowQuart']
x077 = x77.to_list()
# print(x077)
sum077=0
for i in range(n):
    sum077=sum077+x077[i]
avg077=sum077/n
print("77.OwnOccLowQuart Average: ",avg077)
low077=0
equal077=0
high077=0
for i in range(n):
    if(x077[i]>avg077):
       high077=high077+1
    elif(x077[i]!=0 and x077[i]<avg077):
        low077=low077+1

    else:
         equal077=equal077+1

print(low077,equal077,high077)
e077=math.log10(low077/1994)
e0077=math.log10(equal077/1994)
e00077=math.log10(high077/1994)
e77=-((low077/1994)*e077+(equal077/1994)*e0077+(high077/1994)*e00077)
        
print("77.OwnOccLowQuart entropy: ",e77)
l1001.append(e77)


x78 = df['OwnOccMedVal']
x078 = x78.to_list()
# print(x078)
sum078=0
for i in range(n):
    sum078=sum078+x078[i]
avg078=sum078/n
print("78.OwnOccMedVal Average: ",avg078)
low078=0
equal078=0
high078=0
for i in range(n):
    if(x078[i]>avg078):
       high078=high078+1
    elif(x078[i]!=0 and x078[i]<avg078):
        low078=low078+1

    else:
         equal078=equal078+1

print(low078,equal078,high078)
e078=math.log10(low078/1994)
e0078=math.log10(equal078/1994)
e00078=math.log10(high078/1994)
e78=-((low078/1994)*e078+(equal078/1994)*e0078+(high078/1994)*e00078)
        
print("78.OwnOccMedVal entropy: ",e78)
l1001.append(e78)



x79 = df['OwnOccHiQuart']
x079 = x79.to_list()
# print(x079)
sum079=0
for i in range(n):
    sum079=sum079+x079[i]
avg079=sum079/n
print("79.OwnOccHiQuart Average: ",avg079)
low079=0
equal079=0
high079=0
for i in range(n):
    if(x079[i]>avg079):
       high079=high079+1
    elif(x079[i]!=0 and x079[i]<avg079):
        low079=low079+1

    else:
         equal079=equal079+1

print(low079,equal079,high079)
e079=math.log10(low079/1994)
e0079=math.log10(equal079/1994)
e00079=math.log10(high079/1994)
e79=-((low079/1994)*e079+(equal079/1994)*e0079+(high079/1994)*e00079)
        
print("79.OwnOccHiQuart entropy: ",e79)
l1001.append(e79)


x80 = df['RentLowQ']
x080 = x80.to_list()
# print(x080)
sum080=0
for i in range(n):
    sum080=sum080+x080[i]
avg080=sum080/n
print("80.RentLowQ Average: ",avg080)
low080=0
equal080=0
high080=0
for i in range(n):
    if(x080[i]>avg080):
       high080=high080+1
    elif(x080[i]!=0 and x080[i]<avg080):
        low080=low080+1

    else:
         equal080=equal080+1

print(low080,equal080,high080)
e080=math.log10(low080/1994)
e0080=math.log10(equal080/1994)
e00080=math.log10(high080/1994)
e80=-((low080/1994)*e080+(equal080/1994)*e0080+(high080/1994)*e00080)
        
print("80.RentLowQ entropy: ",e80)
l1001.append(e80)


x81 = df['RentMedian']
x081 = x81.to_list()
# print(x081)
sum081=0
for i in range(n):
    sum081=sum081+x081[i]
avg081=sum081/n
print("81.RentMedian Average: ",avg081)
low081=0
equal081=0
high081=0
for i in range(n):
    if(x081[i]>avg081):
       high081=high081+1
    elif(x081[i]!=0 and x081[i]<avg081):
        low081=low081+1

    else:
         equal081=equal081+1

print(low081,equal081,high081)
e081=math.log10(low081/1994)
e0081=math.log10(equal081/1994)
e00081=math.log10(high081/1994)
e81=-((low081/1994)*e081+(equal081/1994)*e0081+(high081/1994)*e00081)
        
print("81.RentMedian entropy: ",e81)
l1001.append(e81)


x82 = df['RentMedian']
x082 = x82.to_list()
# print(x082)
sum082=0
for i in range(n):
    sum082=sum082+x082[i]
avg082=sum082/n
print("82.RentMedian Average: ",avg082)
low082=0
equal082=0
high082=0
for i in range(n):
    if(x082[i]>avg082):
       high082=high082+1
    elif(x082[i]!=0 and x082[i]<avg082):
        low082=low082+1

    else:
         equal082=equal082+1

print(low082,equal082,high082)
e082=math.log10(low082/1994)
e0082=math.log10(equal082/1994)
e00082=math.log10(high082/1994)
e82=-((low082/1994)*e082+(equal082/1994)*e0082+(high082/1994)*e00082)
        
print("82.RentMedian entropy: ",e82)
l1001.append(e82)


x83 = df['RentHighQ']
x083 = x83.to_list()
# print(x083)
sum083=0
for i in range(n):
    sum083=sum083+x083[i]
avg083=sum083/n
print("83.RentHighQ Average: ",avg083)
low083=0
equal083=0
high083=0
for i in range(n):
    if(x083[i]>avg083):
       high083=high083+1
    elif(x083[i]!=0 and x083[i]<avg083):
        low083=low083+1

    else:
         equal083=equal083+1

print(low083,equal083,high083)
e083=math.log10(low083/1994)
e0083=math.log10(equal083/1994)
e00083=math.log10(high083/1994)
e83=-((low083/1994)*e083+(equal083/1994)*e0083+(high083/1994)*e00083)
        
print("83.RentHighQ entropy: ",e83)
l1001.append(e83)


x84 = df['MedRent']
x084 = x84.to_list()
# print(x084)
sum084=0
for i in range(n):
    sum084=sum084+x084[i]
avg084=sum084/n
print("84.MedRent Average: ",avg084)
low084=0
equal084=0
high084=0
for i in range(n):
    if(x084[i]>avg084):
       high084=high084+1
    elif(x084[i]!=0 and x084[i]<avg084):
        low084=low084+1

    else:
         equal084=equal084+1

print(low084,equal084,high084)
e084=math.log10(low084/1994)
e0084=math.log10(equal084/1994)
e00084=math.log10(high084/1994)
e84=-((low084/1994)*e084+(equal084/1994)*e0084+(high084/1994)*e00084)
        
print("84.MedRent entropy: ",e84)
l1001.append(e84)


x85 = df['MedRentPctHousInc']
x085 = x85.to_list()
# print(x085)
sum085=0
for i in range(n):
    sum085=sum085+x085[i]
avg085=sum085/n
print("85.MedRentPctHousInc Average: ",avg085)
low085=0
equal085=0
high085=0
for i in range(n):
    if(x085[i]>avg085):
       high085=high085+1
    elif(x085[i]!=0 and x085[i]<avg085):
        low085=low085+1

    else:
         equal085=equal085+1

print(low085,equal085,high085)
e085=math.log10(low085/1994)
e0085=math.log10(equal085/1994)
e00085=math.log10(high085/1994)
e85=-((low085/1994)*e085+(equal085/1994)*e0085+(high085/1994)*e00085)
        
print("85.MedRentPctHousInc entropy: ",e85)
l1001.append(e85)


x86 = df['MedOwnCostPctInc']
x086 = x86.to_list()
# print(x086)
sum086=0
for i in range(n):
    sum086=sum086+x086[i]
avg086=sum086/n
print("86.MedOwnCostPctInc Average: ",avg086)
low086=0
equal086=0
high086=0
for i in range(n):
    if(x086[i]>avg086):
       high086=high086+1
    elif(x086[i]!=0 and x086[i]<avg086):
        low086=low086+1

    else:
         equal086=equal086+1

print(low086,equal086,high086)
e086=math.log10(low086/1994)
e0086=math.log10(equal086/1994)
e00086=math.log10(high086/1994)
e86=-((low086/1994)*e086+(equal086/1994)*e0086+(high086/1994)*e00086)
        
print("86.MedOwnCostPctInc entropy: ",e86)
l1001.append(e86)


x87 = df['MedOwnCostPctIncNoMtg']
x087 = x87.to_list()
# print(x087)
sum087=0
for i in range(n):
    sum087=sum087+x087[i]
avg087=sum087/n
print("87.MedOwnCostPctIncNoMtg Average: ",avg087)
low087=0
equal087=0
high087=0
for i in range(n):
    if(x087[i]>avg087):
       high087=high087+1
    elif(x087[i]!=0 and x087[i]<avg087):
        low087=low087+1

    else:
         equal087=equal087+1

print(low087,equal087,high087)
e087=math.log10(low087/1994)
e0087=math.log10(equal087/1994)
e00087=math.log10(high087/1994)
e87=-((low087/1994)*e087+(equal087/1994)*e0087+(high087/1994)*e00087)
        
print("87.MedOwnCostPctIncNoMtg entropy: ",e87)
l1001.append(e87)


x88 = df['PctForeignBorn']
x088 = x88.to_list()
# print(x088)
sum088=0
for i in range(n):
    sum088=sum088+x088[i]
avg088=sum088/n
print("88.PctForeignBorn Average: ",avg088)
low088=0
equal088=0
high088=0
for i in range(n):
    if(x088[i]>avg088):
       high088=high088+1
    elif(x088[i]!=0 and x088[i]<avg088):
        low088=low088+1

    else:
         equal088=equal088+1

print(low088,equal088,high088)
e088=math.log10(low088/1994)
e0088=math.log10(equal088/1994)
e00088=math.log10(high088/1994)
e88=-((low088/1994)*e088+(equal088/1994)*e0088+(high088/1994)*e00088)
        
print("88.PctForeignBorn entropy: ",e88)
l1001.append(e88)


x89 = df['PctBornSameState']
x089 = x89.to_list()
# print(x089)
sum089=0
for i in range(n):
    sum089=sum089+x089[i]
avg089=sum089/n
print("89.PctBornSameState Average: ",avg089)
low089=0
equal089=0
high089=0
for i in range(n):
    if(x089[i]>avg089):
       high089=high089+1
    elif(x089[i]!=0 and x089[i]<avg089):
        low089=low089+1

    else:
         equal089=equal089+1

print(low089,equal089,high089)
e089=math.log10(low089/1994)
e0089=math.log10(equal089/1994)
e00089=math.log10(high089/1994)
e89=-((low089/1994)*e089+(equal089/1994)*e0089+(high089/1994)*e00089)
        
print("89.PctBornSameState entropy: ",e89)
l1001.append(e89)


x90 = df['PctSameHouse85']
x090 = x90.to_list()
# print(x090)
sum090=0
for i in range(n):
    sum090=sum090+x090[i]
avg090=sum090/n
print("90.PctSameHouse85 Average: ",avg090)
low090=0
equal090=0
high090=0
for i in range(n):
    if(x090[i]>avg090):
       high090=high090+1
    elif(x090[i]!=0 and x090[i]<avg090):
        low090=low090+1

    else:
         equal090=equal090+1

print(low090,equal090,high090)
e090=math.log10(low090/1994)
e0090=math.log10(equal090/1994)
e00090=math.log10(high090/1994)
e90=-((low090/1994)*e090+(equal090/1994)*e0090+(high090/1994)*e00090)
        
print("90.PctSameHouse85 entropy: ",e90)
l1001.append(e90)


x91 = df['PctSameCity85']
x091 = x91.to_list()
# print(x091)
sum091=0
for i in range(n):
    sum091=sum091+x091[i]
avg091=sum091/n
print("91.PctSameCity85 Average: ",avg091)
low091=0
equal091=0
high091=0
for i in range(n):
    if(x091[i]>avg091):
       high091=high091+1
    elif(x091[i]!=0 and x091[i]<avg091):
        low091=low091+1

    else:
         equal091=equal091+1

print(low091,equal091,high091)
e091=math.log10(low091/1994)
e0091=math.log10(equal091/1994)
e00091=math.log10(high091/1994)
e91=-((low091/1994)*e091+(equal091/1994)*e0091+(high091/1994)*e00091)
        
print("91.PctSameCity85 entropy: ",e91)
l1001.append(e91)


x92 = df['PctSameState85']
x092 = x92.to_list()
# print(x092)
sum092=0
for i in range(n):
    sum092=sum092+x092[i]
avg092=sum092/n
print("92.PctSameState85 Average: ",avg092)
low092=0
equal092=0
high092=0
for i in range(n):
    if(x092[i]>avg092):
       high092=high092+1
    elif(x092[i]!=0 and x092[i]<avg092):
        low092=low092+1

    else:
         equal092=equal092+1

print(low092,equal092,high092)
e092=math.log10(low092/1994)
e0092=math.log10(equal092/1994)
e00092=math.log10(high092/1994)
e92=-((low092/1994)*e092+(equal092/1994)*e0092+(high092/1994)*e00092)
        
print("92.PctSameState85 entropy: ",e92)
l1001.append(e92)

#print(l1001)
l1002=[]
l1003=[]
for i in range(92):
    if(l1001[i]<=0.31):
        l1002.append(l1001[i])
        l1003.append(i+1)
print(l1002,l1003)   
    


'''
x93 = df['LemasSwornFT']
x093 = x93.to_list()
# print(x093)
sum093=0
for i in range(n):
    sum093=sum093+x093[i]
avg093=sum093/n
print("93.LemasSwornFT Average: ",avg093)
low093=0
equal093=0
high093=0
for i in range(n):
    if(x093[i]>avg093):
       high093=high093+1
    elif(x093[i]!=0 and x093[i]<avg093):
        low093=low093+1

    else:
         equal093=equal093+1

print(low093,equal093,high093)
e093=math.log10(low093/1994)
e0093=math.log10(equal093/1994)
e00093=math.log10(high093/1994)
e93=-((low093/1994)*e093+(equal093/1994)*e0093+(high093/1994)*e00093)
        
print("93.LemasSwornFT entropy: ",e93)



x94 = df['LemasSwFTPerPop']
x094 = x94.to_list()
# print(x094)
sum094=0
for i in range(n):
    sum094=sum094+x094[i]
avg094=sum094/n
print("94.LemasSwFTPerPop Average: ",avg094)
l94=[]    
for i in range(n):
   
   a094=x094[i]-avg094
   b094=y00[i]-y000
   c094=a094*a094
   d094=a094*b094
   a94=d094/c094
   l94.append(a94)
b94=sum(l94)/n

print("94.ViolentCrimesPerPop-LemasSwFTPerPop: ",b94)



x95 = df['LemasSwFTFieldOps']
x095 = x95.to_list()
# print(x095)
sum095=0
for i in range(n):
    sum095=sum095+x095[i]
avg095=sum095/n
print("95.LemasSwFTFieldOps Average: ",avg095)
l95=[]    
for i in range(n):
   
   a095=x095[i]-avg095
   b095=y00[i]-y000
   c095=a095*a095
   d095=a095*b095
   a95=d095/c095
   l95.append(a95)
b95=sum(l95)/n

print("95.ViolentCrimesPerPop-LemasSwFTFieldOps: ",b95)



x96 = df['LemasSwFTFieldPerPop']
x096 = x96.to_list()
# print(x096)
sum096=0
for i in range(n):
    sum096=sum096+x096[i]
avg096=sum096/n
print("96.LemasSwFTFieldPerPop Average: ",avg096)
l96=[]    
for i in range(n):
   
   a096=x096[i]-avg096
   b096=y00[i]-y000
   c096=a096*a096
   d096=a096*b096
   a96=d096/c096
   l96.append(a96)
b96=sum(l96)/n

print("96.ViolentCrimesPerPop-LemasSwFTFieldPerPop: ",b96)



x97 = df['LemasTotalReq']
x097 = x97.to_list()
# print(x097)
sum097=0
for i in range(n):
    sum097=sum097+x097[i]
avg097=sum097/n
print("97.LemasTotalReq Average: ",avg097)
l97=[]    
for i in range(n):
   
   a097=x097[i]-avg097
   b097=y00[i]-y000
   c097=a097*a097
   d097=a097*b097
   a97=d097/c097
   l97.append(a97)
b97=sum(l97)/n

print("97.ViolentCrimesPerPop-LemasTotalReq: ",b97)



x98 = df['LemasTotReqPerPop']
x098 = x98.to_list()
# print(x098)
sum098=0
for i in range(n):
    sum098=sum098+x098[i]
avg098=sum098/n
print("98.LemasTotReqPerPop Average: ",avg098)
l98=[]    
for i in range(n):
   
   a098=x098[i]-avg098
   b098=y00[i]-y000
   c098=a098*a098
   d098=a098*b098
   a98=d098/c098
   l98.append(a98)
b98=sum(l98)/n

print("98.ViolentCrimesPerPop-LemasTotReqPerPop: ",b98)



x99 = df['PolicReqPerOffic']
x099 = x99.to_list()
# print(x099)
sum099=0
for i in range(n):
    sum099=sum099+x099[i]
avg099=sum099/n
print("99.PolicReqPerOffic Average: ",avg099)
l99=[]    
for i in range(n):
   
   a099=x099[i]-avg099
   b099=y00[i]-y000
   c099=a099*a099
   d099=a099*b099
   a99=d099/c099
   l99.append(a99)
b99=sum(l99)/n

print("99.ViolentCrimesPerPop-PolicReqPerOffic: ",b99)



x100 = df['PolicPerPop']
x0100 = x100.to_list()
# print(x0100)
sum0100=0
for i in range(n):
    sum0100=sum0100+x0100[i]
avg0100=sum0100/n
print("100.PolicPerPop Average: ",avg0100)
l100=[]
for i in range(n):
   
   a0100=x0100[i]-avg0100
   b0100=y00[i]-y000
   c0100=a0100*a0100
   d0100=a0100*b0100
   a100=d0100/c0100
   l100.append(a100)
b100=sum(l100)/n

print("100.ViolentCrimesPerPop-PolicPerPop: ",b100)



x101 = df['RacialMatchCommPol']
x0101 = x101.to_list()
# print(x0101)
sum0101=0
for i in range(n):
    sum0101=sum0101+x0101[i]
avg0101=sum0101/n
print("101.RacialMatchCommPol Average: ",avg0101)
l101=[]    
for i in range(n):
   
   a0101=x0101[i]-avg0101
   b0101=y00[i]-y000
   c0101=a0101*a0101
   d0101=a0101*b0101
   a101=d0101/c0101
   l101.append(a101)
b101=sum(l101)/n

print("101.ViolentCrimesPerPop-RacialMatchCommPol: ",b101)



x102 = df['PctPolicWhite']
x0102 = x102.to_list()
# print(x0102)
sum0102=0
for i in range(n):
    sum0102=sum0102+x0102[i]
avg0102=sum0102/n
print("102.PctPolicWhite Average: ",avg0102)
l102=[]
for i in range(n):
   
   a0102=x0102[i]-avg0102
   b0102=y00[i]-y000
   c0102=a0102*a0102
   d0102=a0102*b0102
   a102=d0102/c0102
   l102.append(a102)
b102=sum(l102)/n

print("102.ViolentCrimesPerPop-PctPolicWhite: ",b102)



x103 = df['PctPolicBlack ']
x0103 = x103.to_list()
# print(x0103)
sum0103=0
for i in range(n):
    sum0103=sum0103+x0103[i]
avg0103=sum0103/n
print("103.PctPolicBlack  Average: ",avg0103)
l103=[]    
for i in range(n):
   
   a0103=x0103[i]-avg0103
   b0103=y00[i]-y000
   c0103=a0103*a0103
   d0103=a0103*b0103
   a103=d0103/c0103
   l103.append(a103)
b103=sum(l103)/n

print("103.ViolentCrimesPerPop-PctPolicBlack : ",b103)



x104 = df['PctPolicHisp']
x0104 = x104.to_list()
# print(x0104)
sum0104=0
for i in range(n):
    sum0104=sum0104+x0104[i]
avg0104=sum0104/n
print("104.PctPolicHisp Average: ",avg0104)
l104=[]
for i in range(n):
   
   a0104=x0104[i]-avg0104
   b0104=y00[i]-y000
   c0104=a0104*a0104
   d0104=a0104*b0104
   a104=d0104/c0104
   l104.append(a104)
b104=sum(l104)/n

print("104.ViolentCrimesPerPop-PctPolicHisp: ",b104)



x105 = df['PctPolicAsian']
x0105 = x105.to_list()
# print(x0105)
sum0105=0
for i in range(n):
    sum0105=sum0105+x0105[i]
avg0105=sum0105/n
print("105.PctPolicAsian Average: ",avg0105)
l105=[]    
for i in range(n):
   
   a0105=x0105[i]-avg0105
   b0105=y00[i]-y000
   c0105=a0105*a0105
   d0105=a0105*b0105
   a105=d0105/c0105
   l105.append(a105)
b105=sum(l105)/n

print("105.ViolentCrimesPerPop-PctPolicAsian: ",b105)



x106 = df['PctPolicMinor']
x0106 = x106.to_list()
# print(x0106)
sum0106=0
for i in range(n):
    sum0106=sum0106+x0106[i]
avg0106=sum0106/n
print("106.PctPolicMinor Average: ",avg0106)
l106=[]
for i in range(n):
   
   a0106=x0106[i]-avg0106
   b0106=y00[i]-y000
   c0106=a0106*a0106
   d0106=a0106*b0106
   a106=d0106/c0106
   l106.append(a106)
b106=sum(l106)/n

print("106.ViolentCrimesPerPop-PctPolicMinor: ",b106)



x107 = df['OfficAssgnDrugUnits']
x0107 = x107.to_list()
# print(x0107)
sum0107=0
for i in range(n):
    sum0107=sum0107+x0107[i]
avg0107=sum0107/n
print("107.OfficAssgnDrugUnits Average: ",avg0107)
l107=[]    
for i in range(n):
   
   a0107=x0107[i]-avg0107
   b0107=y00[i]-y000
   c0107=a0107*a0107
   d0107=a0107*b0107
   a107=d0107/c0107
   l107.append(a107)
b107=sum(l107)/n

print("107.ViolentCrimesPerPop-OfficAssgnDrugUnits: ",b107)



x108 = df['NumKindsDrugsSeiz']
x0108 = x108.to_list()
# print(x0108)
sum0108=0
for i in range(n):
    sum0108=sum0108+x0108[i]
avg0108=sum0108/n
print("108.NumKindsDrugsSeiz Average: ",avg0108)
l108=[]
for i in range(n):
   
   a0108=x0108[i]-avg0108
   b0108=y00[i]-y000
   c0108=a0108*a0108
   d0108=a0108*b0108
   a108=d0108/c0108
   l108.append(a108)
b108=sum(l108)/n

print("108.ViolentCrimesPerPop-NumKindsDrugsSeiz: ",b108)



x109 = df['PolicAveOTWorked']
x0109 = x109.to_list()
# print(x0109)
sum0109=0
for i in range(n):
    sum0109=sum0109+x0109[i]
avg0109=sum0109/n
print("109.PolicAveOTWorked Average: ",avg0109)
l109=[]    
for i in range(n):
   
   a0109=x0109[i]-avg0109
   b0109=y00[i]-y000
   c0109=a0109*a0109
   d0109=a0109*b0109
   a109=d0109/c0109
   l109.append(a109)
b109=sum(l109)/n

print("109.ViolentCrimesPerPop-PolicAveOTWorked: ",b109)



x110 = df['LandArea']
x0110 = x110.to_list()
# print(x0110)
sum0110=0
for i in range(n):
    sum0110=sum0110+x0110[i]
avg0110=sum0110/n
print("110.LandArea Average: ",avg0110)
l110=[]
for i in range(n):
   
   a0110=x0110[i]-avg0110
   b0110=y00[i]-y000
   c0110=a0110*a0110
   d0110=a0110*b0110
   a110=d0110/c0110
   l110.append(a110)
b110=sum(l110)/n

print("110.ViolentCrimesPerPop-LandArea: ",b110)



x111 = df['PopDens']
x0111 = x111.to_list()
# print(x0111)
sum0111=0
for i in range(n):
    sum0111=sum0111+x0111[i]
avg0111=sum0111/n
print("111.PopDens Average: ",avg0111)
l111=[]    
for i in range(n):
   
   a0111=x0111[i]-avg0111
   b0111=y00[i]-y000
   c0111=a0111*a0111
   d0111=a0111*b0111
   a111=d0111/c0111
   l111.append(a111)
b111=sum(l111)/n

print("111.ViolentCrimesPerPop-PopDens: ",b111)



x112 = df['PctUsePubTrans']
x0112 = x112.to_list()
# print(x0112)
sum0112=0
for i in range(n):
    sum0112=sum0112+x0112[i]
avg0112=sum0112/n
print("112.PctUsePubTrans Average: ",avg0112)
l112=[]
for i in range(n):
   
   a0112=x0112[i]-avg0112
   b0112=y00[i]-y000
   c0112=a0112*a0112
   d0112=a0112*b0112
   a112=d0112/c0112
   l112.append(a112)
b112=sum(l112)/n

print("112.ViolentCrimesPerPop-PctUsePubTrans: ",b112)



x113 = df['PolicCars']
x0113 = x113.to_list()
# print(x0113)
sum0113=0
for i in range(n):
    sum0113=sum0113+x0113[i]
avg0113=sum0113/n
print("113.PolicCars Average: ",avg0113)
l113=[]    
for i in range(n):
   
   a0113=x0113[i]-avg0113
   b0113=y00[i]-y000
   c0113=a0113*a0113
   d0113=a0113*b0113
   a113=d0113/c0113
   l113.append(a113)
b113=sum(l113)/n

print("113.ViolentCrimesPerPop-PolicCars: ",b113)



x114 = df['PolicOperBudg']
x0114 = x114.to_list()
# print(x0114)
sum0114=0
for i in range(n):
    sum0114=sum0114+x0114[i]
avg0114=sum0114/n
print("114.PolicOperBudg Average: ",avg0114)
l114=[]
for i in range(n):
   
   a0114=x0114[i]-avg0114
   b0114=y00[i]-y000
   c0114=a0114*a0114
   d0114=a0114*b0114
   a114=d0114/c0114
   l114.append(a114)
b114=sum(l114)/n

print("114.ViolentCrimesPerPop-PolicOperBudg: ",b114)

'''