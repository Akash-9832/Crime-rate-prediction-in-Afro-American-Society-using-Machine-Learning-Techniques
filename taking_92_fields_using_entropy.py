

n=int(input("Enter the dividing number of trained and test data between 0 and 1994: "))


import pandas as pd
df = pd.read_csv("D:\college project\Research Paper 02\Files and Papers\crime_data.csv")
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

# Taking testing data from violent crime........
for i in range(n,1994):
   if(y00[i]>=0.05):
       b=1
       l.append(b)
   else:
       b=0
       l.append(b)
#print(l)



x1 = df['population']
x01 = x1.to_list()
# print(x01)
sum01=0
for i in range(n):
    sum01=sum01+x01[i]
avg01=sum01/n
print("1.population Average: ",avg01)
l1=[]    
for i in range(n):
   
   a01=x01[i]-avg01
   b01=y00[i]-y000
   c01=a01*a01
   d01=a01*b01
   a1=d01/c01
   l1.append(a1)
b1=sum(l1)/n

print("1.ViolentCrimesPerPop-population: ",b1)



x2 = df['householdsize']
x02 = x2.to_list()
# print(x02)
sum02=0
for i in range(n):
    sum02=sum02+x02[i]
avg02=sum02/n
print("2.householdsize Average: ",avg02)
l2=[]    
for i in range(n):
   
   a02=x02[i]-avg02
   b02=y00[i]-y000
   c02=a02*a02
   d02=a02*b02
   a2=d02/c02
   l2.append(a2)
b2=sum(l2)/n

print("2.ViolentCrimesPerPop-householdsize: ",b2)



x3 = df['racepctblack']
x03 = x3.to_list()
# print(x03)
sum03=0
for i in range(n):
    sum03=sum03+x03[i]
avg03=sum03/n
print("3.racepctblack Average: ",avg03)
l3=[]    
for i in range(n):
   
   a03=x03[i]-avg03
   b03=y00[i]-y000
   c03=a03*a03
   d03=a03*b03
   a3=d03/c03
   l3.append(a3)
b3=sum(l3)/n

print("3.ViolentCrimesPerPop-racepctblack: ",b3)


x4 = df['racePctWhite']
x04 = x4.to_list()
# print(x04)
sum04=0
for i in range(n):
    sum04=sum04+x04[i]
avg04=sum04/n
print("4.racePctWhite Average: ",avg04)
l4=[]    
for i in range(n):
   
   a04=x04[i]-avg04
   b04=y00[i]-y000
   c04=a04*a04
   d04=a04*b04
   a4=d04/c04
   l4.append(a4)
b4=sum(l4)/n

print("4.ViolentCrimesPerPop-racePctWhite: ",b4)



x5 = df['racePctAsian']
x05 = x5.to_list()
# print(x05)
sum05=0
for i in range(n):
    sum05=sum05+x05[i]
avg05=sum05/n
print("5.racePctAsian Average: ",avg05)
l5=[]    
for i in range(n):
   
   a05=x05[i]-avg05
   b05=y00[i]-y000
   c05=a05*a05
   d05=a05*b05
   a5=d05/c05
   l5.append(a5)
b5=sum(l5)/n

print("5.ViolentCrimesPerPop-racePctAsian: ",b5)


x6 = df['racePctHisp']
x06 = x6.to_list()
# print(x06)
sum06=0
for i in range(n):
    sum06=sum06+x06[i]
avg06=sum06/n
print("6.racePctHisp Average: ",avg06)
l6=[]    
for i in range(n):
   
   a06=x06[i]-avg06
   b06=y00[i]-y000
   c06=a06*a06
   d06=a06*b06
   a6=d06/c06
   l6.append(a6)
b6=sum(l6)/n

print("6.ViolentCrimesPerPop-racePctHisp: ",b6)



x7 = df['agePct12t21']
x07 = x7.to_list()
# print(x07)
sum07=0
for i in range(n):
    sum07=sum07+x07[i]
avg07=sum07/n
print("7.agePct12t21 Average: ",avg07)
l7=[]    
for i in range(n):
   
   a07=x07[i]-avg07
   b07=y00[i]-y000
   c07=a07*a07
   d07=a07*b07
   a7=d07/c07
   l7.append(a7)
b7=sum(l7)/n

print("7.ViolentCrimesPerPop-agePct12t21: ",b7)



x8 = df['agePct12t29']
x08 = x8.to_list()
# print(x08)
sum08=0
for i in range(n):
    sum08=sum08+x08[i]
avg08=sum08/n
print("8.agePct12t29 Average: ",avg08)
l8=[]    
for i in range(n):
   
   a08=x08[i]-avg08
   b08=y00[i]-y000
   c08=a08*a08
   d08=a08*b08
   a8=d08/c08
   l8.append(a8)
b8=sum(l8)/n

print("8.ViolentCrimesPerPop-agePct12t29: ",b8)



x9 = df['agePct16t24']
x09 = x9.to_list()
# print(x09)
sum09=0
for i in range(n):
    sum09=sum09+x09[i]
avg09=sum09/n
print("9.agePct16t24 Average: ",avg09)
l9=[]    
for i in range(n):
   
   a09=x09[i]-avg09
   b09=y00[i]-y000
   c09=a09*a09
   d09=a09*b09
   a9=d09/c09
   l9.append(a9)
b9=sum(l9)/n

print("9.ViolentCrimesPerPop-agePct16t24: ",b9)



x10 = df['agePct65aup']
x010 = x10.to_list()
# print(x010)
sum010=0
for i in range(n):
    sum010=sum010+x010[i]
avg010=sum010/n
print("10.agePct65aup Average: ",avg010)
l10=[]    
for i in range(n):
   
   a010=x010[i]-avg010
   b010=y00[i]-y000
   c010=a010*a010
   d010=a010*b010
   a10=d010/c010
   l10.append(a10)
b10=sum(l10)/n

print("10.ViolentCrimesPerPop-agePct65aup: ",b10)



x11 = df['numbUrban']
x011 = x11.to_list()
# print(x011)
sum011=0
for i in range(n):
    sum011=sum011+x011[i]
avg011=sum011/n
print("11.numbUrban Average: ",avg011)
l11=[]    
for i in range(n):
   
   a011=x011[i]-avg011
   b011=y00[i]-y000
   c011=a011*a011
   d011=a011*b011
   a11=d011/c011
   l11.append(a11)
b11=sum(l11)/n

print("11.ViolentCrimesPerPop-numbUrban: ",b11)



x12 = df['medIncome']
x012 = x12.to_list()
# print(x012)
sum012=0
for i in range(n):
    sum012=sum012+x012[i]
avg012=sum012/n
print("12.medIncome Average: ",avg012)
l12=[]    
for i in range(n):
   
   a012=x012[i]-avg012
   b012=y00[i]-y000
   c012=a012*a012
   d012=a012*b012
   a12=d012/c012
   l12.append(a12)
b12=sum(l12)/n

print("12.ViolentCrimesPerPop-medIncome: ",b12)




x13 = df['pctWWage']
x013 = x13.to_list()
# print(x013)
sum013=0
for i in range(n):
    sum013=sum013+x013[i]
avg013=sum013/n
print("13.pctWWage Average: ",avg013)
l13=[]    
for i in range(n):
   
   a013=x013[i]-avg013
   b013=y00[i]-y000
   c013=a013*a013
   d013=a013*b013
   a13=d013/c013
   l13.append(a13)
b13=sum(l13)/n

print("13.ViolentCrimesPerPop-pctWWage: ",b13)



x14 = df['pctWFarmSelf']
x014 = x14.to_list()
# print(x014)
sum014=0
for i in range(n):
    sum014=sum014+x014[i]
avg014=sum014/n
print("14.pctWFarmSelf Average: ",avg014)
l14=[]    
for i in range(n):
   
   a014=x014[i]-avg014
   b014=y00[i]-y000
   c014=a014*a014
   d014=a014*b014
   a14=d014/c014
   l14.append(a14)
b14=sum(l14)/n

print("14.ViolentCrimesPerPop-pctWFarmSelf: ",b14)



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



x16 = df['pctWSocSec']
x016 = x16.to_list()
# print(x016)
sum016=0
for i in range(n):
    sum016=sum016+x016[i]
avg016=sum016/n
print("16.pctWSocSec Average: ",avg016)
l16=[]    
for i in range(n):
   
   a016=x016[i]-avg016
   b016=y00[i]-y000
   c016=a016*a016
   d016=a016*b016
   a16=d016/c016
   l16.append(a16)
b16=sum(l16)/n

print("16.ViolentCrimesPerPop-pctWSocSec: ",b16)



x17 = df['pctWPubAsst']
x017 = x17.to_list()
# print(x017)
sum017=0
for i in range(n):
    sum017=sum017+x017[i]
avg017=sum017/n
print("17.pctWPubAsst Average: ",avg017)
l17=[]    
for i in range(n):
   
   a017=x017[i]-avg017
   b017=y00[i]-y000
   c017=a017*a017
   d017=a017*b017
   a17=d017/c017
   l17.append(a17)
b17=sum(l17)/n

print("17.ViolentCrimesPerPop-pctWPubAsst: ",b17)



x18 = df['pctWRetire']
x018 = x18.to_list()
# print(x018)
sum018=0
for i in range(n):
    sum018=sum018+x018[i]
avg018=sum018/n
print("18.pctWRetire Average: ",avg018)
l18=[]    
for i in range(n):
   
   a018=x018[i]-avg018
   b018=y00[i]-y000
   c018=a018*a018
   d018=a018*b018
   a18=d018/c018
   l18.append(a18)
b18=sum(l18)/n

print("18.ViolentCrimesPerPop-pctWRetire: ",b18)




x19 = df['medFamInc']
x019 = x19.to_list()
# print(x019)
sum019=0
for i in range(n):
    sum019=sum019+x019[i]
avg019=sum019/n
print("19.medFamInc Average: ",avg019)
l19=[]    
for i in range(n):
   
   a019=x019[i]-avg019
   b019=y00[i]-y000
   c019=a019*a019
   d019=a019*b019
   a19=d019/c019
   l19.append(a19)
b19=sum(l19)/n

print("19.ViolentCrimesPerPop-medFamInc: ",b19)





x20 = df['perCapInc']
x020 = x20.to_list()
# print(x020)
sum020=0
for i in range(n):
    sum020=sum020+x020[i]
avg020=sum020/n
print("20.perCapInc Average: ",avg020)
l20=[]    
for i in range(n):
   
   a020=x020[i]-avg020
   b020=y00[i]-y000
   c020=a020*a020
   d020=a020*b020
   a20=d020/c020
   l20.append(a20)
b20=sum(l20)/n

print("20.ViolentCrimesPerPop-perCapInc: ",b20)



x21 = df['whitePerCap']
x021 = x21.to_list()
# print(x021)
sum021=0
for i in range(n):
    sum021=sum021+x021[i]
avg021=sum021/n
print("21.whitePerCap Average: ",avg021)
l21=[]    
for i in range(n):
   
   a021=x021[i]-avg021
   b021=y00[i]-y000
   c021=a021*a021
   d021=a021*b021
   a21=d021/c021
   l21.append(a21)
b21=sum(l21)/n

print("21.ViolentCrimesPerPop-whitePerCap: ",b21)


x22 = df['blackPerCap']
x022 = x22.to_list()
# print(x022)
sum022=0
for i in range(n):
    sum022=sum022+x022[i]
avg022=sum022/n
print("22.blackPerCap Average: ",avg022)
l22=[]    
for i in range(n):
   
   a022=x022[i]-avg022
   b022=y00[i]-y000
   c022=a022*a022
   d022=a022*b022
   a22=d022/c022
   l22.append(a22)
b22=sum(l22)/n

print("22.ViolentCrimesPerPop-blackPerCap: ",b22)



x23 = df['indianPerCap']
x023 = x23.to_list()
# print(x023)
sum023=0
for i in range(n):
    sum023=sum023+x023[i]
avg023=sum023/n
print("23.indianPerCap Average: ",avg023)
l23=[]    
for i in range(n):
   
   a023=x023[i]-avg023
   b023=y00[i]-y000
   c023=a023*a023
   d023=a023*b023
   a23=d023/c023
   l23.append(a23)
b23=sum(l23)/n

print("23.ViolentCrimesPerPop-indianPerCap: ",b23)



x24 = df['AsianPerCap']
x024 = x24.to_list()
# print(x024)
sum024=0
for i in range(n):
    sum024=sum024+x024[i]
avg024=sum024/n
print("24.AsianPerCap Average: ",avg024)
l24=[]    
for i in range(n):
   
   a024=x024[i]-avg024
   b024=y00[i]-y000
   c024=a024*a024
   d024=a024*b024
   a24=d024/c024
   l24.append(a24)
b24=sum(l24)/n

print("24.ViolentCrimesPerPop-AsianPerCap: ",b24)



x25 = df['OtherPerCap']
x025 = x25.to_list()
# print(x025)
sum025=0
for i in range(n):
    sum025=sum025+x025[i]
avg025=sum025/n
print("25.OtherPerCap Average: ",avg025)
l25=[]    
for i in range(n):
   
   a025=x025[i]-avg025
   b025=y00[i]-y000
   c025=a025*a025
   d025=a025*b025
   a25=d025/c025
   l25.append(a25)
b25=sum(l25)/n

print("25.ViolentCrimesPerPop-OtherPerCap: ",b25)



x26 = df['HispPerCap']
x026 = x26.to_list()
# print(x026)
sum026=0
for i in range(n):
    sum026=sum026+x026[i]
avg026=sum026/n
print("26.HispPerCap Average: ",avg026)
l26=[]    
for i in range(n):
   
   a026=x026[i]-avg026
   b026=y00[i]-y000
   c026=a026*a026
   d026=a026*b026
   a26=d026/c026
   l26.append(a26)
b26=sum(l26)/n

print("26.ViolentCrimesPerPop-HispPerCap: ",b26)



x27 = df['PctPopUnderPov']
x027 = x27.to_list()
# print(x027)
sum027=0
for i in range(n):
    sum027=sum027+x027[i]
avg027=sum027/n
print("27.PctPopUnderPov Average: ",avg027)
l27=[]    
for i in range(n):
   
   a027=x027[i]-avg027
   b027=y00[i]-y000
   c027=a027*a027
   d027=a027*b027
   a27=d027/c027
   l27.append(a27)
b27=sum(l27)/n

print("27.ViolentCrimesPerPop-PctPopUnderPov: ",b27)



x28 = df['PctLess9thGrade']
x028 = x28.to_list()
# print(x028)
sum028=0
for i in range(n):
    sum028=sum028+x028[i]
avg028=sum028/n
print("28.PctLess9thGrade Average: ",avg028)
l28=[]    
for i in range(n):
   
   a028=x028[i]-avg028
   b028=y00[i]-y000
   c028=a028*a028
   d028=a028*b028
   a28=d028/c028
   l28.append(a28)
b28=sum(l28)/n

print("28.ViolentCrimesPerPop-PctLess9thGrade: ",b28)



x29 = df['PctNotHSGrad']
x029 = x29.to_list()
# print(x029)
sum029=0
for i in range(n):
    sum029=sum029+x029[i]
avg029=sum029/n
print("29.PctNotHSGrad Average: ",avg029)
l29=[]    
for i in range(n):
   
   a029=x029[i]-avg029
   b029=y00[i]-y000
   c029=a029*a029
   d029=a029*b029
   a29=d029/c029
   l29.append(a29)
b29=sum(l29)/n

print("29.ViolentCrimesPerPop-PctNotHSGrad: ",b29)



x30 = df['PctBSorMore']
x030 = x30.to_list()
# print(x030)
sum030=0
for i in range(n):
    sum030=sum030+x030[i]
avg030=sum030/n
print("30.PctBSorMore Average: ",avg030)
l30=[]    
for i in range(n):
   
   a030=x030[i]-avg030
   b030=y00[i]-y000
   c030=a030*a030
   d030=a030*b030
   a30=d030/c030
   l30.append(a30)
b30=sum(l30)/n

print("30.ViolentCrimesPerPop-PctBSorMore: ",b30)



x31 = df['PctUnemployed']
x031 = x31.to_list()
# print(x031)
sum031=0
for i in range(n):
    sum031=sum031+x031[i]
avg031=sum031/n
print("31.PctUnemployed Average: ",avg031)
l31=[]    
for i in range(n):
   
   a031=x031[i]-avg031
   b031=y00[i]-y000
   c031=a031*a031
   d031=a031*b031
   a31=d031/c031
   l31.append(a31)
b31=sum(l31)/n

print("31.ViolentCrimesPerPop-PctUnemployed: ",b31)



x32 = df['PctEmploy']
x032 = x32.to_list()
# print(x032)
sum032=0
for i in range(n):
    sum032=sum032+x032[i]
avg032=sum032/n
print("32.PctEmploy Average: ",avg032)
l32=[]    
for i in range(n):
   
   a032=x032[i]-avg032
   b032=y00[i]-y000
   c032=a032*a032
   d032=a032*b032
   a32=d032/c032
   l32.append(a32)
b32=sum(l32)/n

print("32.ViolentCrimesPerPop-PctEmploy: ",b32)



x33 = df['PctEmplManu']
x033 = x33.to_list()
# print(x033)
sum033=0
for i in range(n):
    sum033=sum033+x033[i]
avg033=sum033/n
print("33.PctEmplManu Average: ",avg033)
l33=[]    
for i in range(n):
   
   a033=x033[i]-avg033
   b033=y00[i]-y000
   c033=a033*a033
   d033=a033*b033
   a33=d033/c033
   l33.append(a33)
b33=sum(l33)/n

print("33.ViolentCrimesPerPop-PctEmplManu: ",b33)



x34 = df['PctEmplProfServ']
x034 = x34.to_list()
# print(x034)
sum034=0
for i in range(n):
    sum034=sum034+x034[i]
avg034=sum034/n
print("34.PctEmplProfServ Average: ",avg034)
l34=[]    
for i in range(n):
   
   a034=x034[i]-avg034
   b034=y00[i]-y000
   c034=a034*a034
   d034=a034*b034
   a34=d034/c034
   l34.append(a34)
b34=sum(l34)/n

print("34.ViolentCrimesPerPop-PctEmplProfServ: ",b34)




x35 = df['PctOccupManu']
x035 = x35.to_list()
# print(x035)
sum035=0
for i in range(n):
    sum035=sum035+x035[i]
avg035=sum035/n
print("35.PctOccupManu Average: ",avg035)
l35=[]    
for i in range(n):
   
   a035=x035[i]-avg035
   b035=y00[i]-y000
   c035=a035*a035
   d035=a035*b035
   a35=d035/c035
   l35.append(a35)
b35=sum(l35)/n

print("35.ViolentCrimesPerPop-PctOccupManu: ",b35)



x36 = df['PctOccupMgmtProf']
x036 = x36.to_list()
# print(x036)
sum036=0
for i in range(n):
    sum036=sum036+x036[i]
avg036=sum036/n
print("36.PctOccupMgmtProf Average: ",avg036)
l36=[]    
for i in range(n):
   
   a036=x036[i]-avg036
   b036=y00[i]-y000
   c036=a036*a036
   d036=a036*b036
   a36=d036/c036
   l36.append(a36)
b36=sum(l36)/n

print("36.ViolentCrimesPerPop-PctOccupMgmtProf: ",b36)



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



x38 = df['MalePctNevMarr']
x038 = x38.to_list()
# print(x038)
sum038=0
for i in range(n):
    sum038=sum038+x038[i]
avg038=sum038/n
print("38.MalePctNevMarr Average: ",avg038)
l38=[]    
for i in range(n):
   
   a038=x038[i]-avg038
   b038=y00[i]-y000
   c038=a038*a038
   d038=a038*b038
   a38=d038/c038
   l38.append(a38)
b38=sum(l38)/n

print("38.ViolentCrimesPerPop-MalePctNevMarr: ",b38)



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




x41 = df['PersPerFam']
x041 = x41.to_list()
# print(x041)
sum041=0
for i in range(n):
    sum041=sum041+x041[i]
avg041=sum041/n
print("41.PersPerFam Average: ",avg041)
l41=[]    
for i in range(n):
   
   a041=x041[i]-avg041
   b041=y00[i]-y000
   c041=a041*a041
   d041=a041*b041
   a41=d041/c041
   l41.append(a41)
b41=sum(l41)/n

print("41.ViolentCrimesPerPop-PersPerFam: ",b41)



x42 = df['PctFam2Par']
x042 = x42.to_list()
# print(x042)
sum042=0
for i in range(n):
    sum042=sum042+x042[i]
avg042=sum042/n
print("42.PctFam2Par Average: ",avg042)
l42=[]    
for i in range(n):
   
   a042=x042[i]-avg042
   b042=y00[i]-y000
   c042=a042*a042
   d042=a042*b042
   a42=d042/c042
   l42.append(a42)
b42=sum(l42)/n

print("42.ViolentCrimesPerPop-PctFam2Par: ",b42)




x43 = df['PctKids2Par']
x043 = x43.to_list()
# print(x043)
sum043=0
for i in range(n):
    sum043=sum043+x043[i]
avg043=sum043/n
print("43.PctKids2Par Average: ",avg043)
l43=[]    
for i in range(n):
   
   a043=x043[i]-avg043
   b043=y00[i]-y000
   c043=a043*a043
   d043=a043*b043
   a43=d043/c043
   l43.append(a43)
b43=sum(l43)/n

print("43.ViolentCrimesPerPop-PctKids2Par: ",b43)



x44 = df['PctYoungKids2Par']
x044 = x44.to_list()
# print(x044)
sum044=0
for i in range(n):
    sum044=sum044+x044[i]
avg044=sum044/n
print("44.PctYoungKids2Par Average: ",avg044)
l44=[]    
for i in range(n):
   
   a044=x044[i]-avg044
   b044=y00[i]-y000
   c044=a044*a044
   d044=a044*b044
   a44=d044/c044
   l44.append(a44)
b44=sum(l44)/n

print("44.ViolentCrimesPerPop-PctYoungKids2Par: ",b44)




x45 = df['PctTeen2Par']
x045 = x45.to_list()
# print(x045)
sum045=0
for i in range(n):
    sum045=sum045+x045[i]
avg045=sum045/n
print("45.PctTeen2Par Average: ",avg045)
l45=[]    
for i in range(n):
   
   a045=x045[i]-avg045
   b045=y00[i]-y000
   c045=a045*a045
   d045=a045*b045
   a45=d045/c045
   l45.append(a45)
b45=sum(l45)/n

print("45.ViolentCrimesPerPop-PctTeen2Par: ",b45)




x46 = df['PctWorkMomYoungKids']
x046 = x46.to_list()
# print(x046)
sum046=0
for i in range(n):
    sum046=sum046+x046[i]
avg046=sum046/n
print("46.PctWorkMomYoungKids Average: ",avg046)
l46=[]    
for i in range(n):
   
   a046=x046[i]-avg046
   b046=y00[i]-y000
   c046=a046*a046
   d046=a046*b046
   a46=d046/c046
   l46.append(a46)
b46=sum(l46)/n

print("46.ViolentCrimesPerPop-PctWorkMomYoungKids: ",b46)




x47 = df['PctWorkMom']
x047 = x47.to_list()
# print(x047)
sum047=0
for i in range(n):
    sum047=sum047+x047[i]
avg047=sum047/n
print("47.PctWorkMom Average: ",avg047)
l47=[]    
for i in range(n):
   
   a047=x047[i]-avg047
   b047=y00[i]-y000
   c047=a047*a047
   d047=a047*b047
   a47=d047/c047
   l47.append(a47)
b47=sum(l47)/n

print("47.ViolentCrimesPerPop-PctWorkMom: ",b47)



x48 = df['NumIlleg']
x048 = x48.to_list()
# print(x048)
sum048=0
for i in range(n):
    sum048=sum048+x048[i]
avg048=sum048/n
print("48.NumIlleg Average: ",avg048)
l48=[]    
for i in range(n):
   
   a048=x048[i]-avg048
   b048=y00[i]-y000
   c048=a048*a048
   d048=a048*b048
   a48=d048/c048
   l48.append(a48)
b48=sum(l48)/n

print("48.ViolentCrimesPerPop-NumIlleg: ",b48)




x49 = df['PctIlleg']
x049 = x49.to_list()
# print(x049)
sum049=0
for i in range(n):
    sum049=sum049+x049[i]
avg049=sum049/n
print("49.PctIlleg Average: ",avg049)
l49=[]    
for i in range(n):
   
   a049=x049[i]-avg049
   b049=y00[i]-y000
   c049=a049*a049
   d049=a049*b049
   a49=d049/c049
   l49.append(a49)
b49=sum(l49)/n

print("49.ViolentCrimesPerPop-PctIlleg: ",b49)



x50 = df['NumImmig']
x050 = x50.to_list()
# print(x050)
sum050=0
for i in range(n):
    sum050=sum050+x050[i]
avg050=sum050/n
print("50.NumImmig Average: ",avg050)
l50=[]    
for i in range(n):
   
   a050=x050[i]-avg050
   b050=y00[i]-y000
   c050=a050*a050
   d050=a050*b050
   a50=d050/c050
   l50.append(a50)
b50=sum(l50)/n

print("50.ViolentCrimesPerPop-NumImmig: ",b50)




x51 = df['PctImmigRecent']
x051 = x51.to_list()
# print(x051)
sum051=0
for i in range(n):
    sum051=sum051+x051[i]
avg051=sum051/n
print("51.PctImmigRecent Average: ",avg051)
l51=[]    
for i in range(n):
   
   a051=x051[i]-avg051
   b051=y00[i]-y000
   c051=a051*a051
   d051=a051*b051
   a51=d051/c051
   l51.append(a51)
b51=sum(l51)/n

print("51.ViolentCrimesPerPop-PctImmigRecent: ",b51)



x52 = df['PctImmigRec5']
x052 = x52.to_list()
# print(x052)
sum052=0
for i in range(n):
    sum052=sum052+x052[i]
avg052=sum052/n
print("52.PctImmigRec5 Average: ",avg052)
l52=[]    
for i in range(n):
   
   a052=x052[i]-avg052
   b052=y00[i]-y000
   c052=a052*a052
   d052=a052*b052
   a52=d052/c052
   l52.append(a52)
b52=sum(l52)/n

print("52.ViolentCrimesPerPop-PctImmigRec5: ",b52)




x53 = df['PctImmigRec8']
x053 = x53.to_list()
# print(x053)
sum053=0
for i in range(n):
    sum053=sum053+x053[i]
avg053=sum053/n
print("53.PctImmigRec8 Average: ",avg053)
l53=[]    
for i in range(n):
   
   a053=x053[i]-avg053
   b053=y00[i]-y000
   c053=a053*a053
   d053=a053*b053
   a53=d053/c053
   l53.append(a53)
b53=sum(l53)/n

print("53.ViolentCrimesPerPop-PctImmigRec8: ",b53)




x54 = df['PctImmigRec10']
x054 = x54.to_list()
# print(x054)
sum054=0
for i in range(n):
    sum054=sum054+x054[i]
avg054=sum054/n
print("54.PctImmigRec10 Average: ",avg054)
l54=[]    
for i in range(n):
   
   a054=x054[i]-avg054
   b054=y00[i]-y000
   c054=a054*a054
   d054=a054*b054
   a54=d054/c054
   l54.append(a54)
b54=sum(l54)/n

print("54.ViolentCrimesPerPop-PctImmigRec10: ",b54)




x55 = df['PctRecentImmig']
x055 = x55.to_list()
# print(x055)
sum055=0
for i in range(n):
    sum055=sum055+x055[i]
avg055=sum055/n
print("55.PctRecentImmig Average: ",avg055)
l55=[]    
for i in range(n):
   
   a055=x055[i]-avg055
   b055=y00[i]-y000
   c055=a055*a055
   d055=a055*b055
   a55=d055/c055
   l55.append(a55)
b55=sum(l55)/n

print("55.ViolentCrimesPerPop-PctRecentImmig: ",b55)




x56 = df['PctRecImmig5']
x056 = x56.to_list()
# print(x056)
sum056=0
for i in range(n):
    sum056=sum056+x056[i]
avg056=sum056/n
print("56.PctRecImmig5 Average: ",avg056)
l56=[]    
for i in range(n):
   
   a056=x056[i]-avg056
   b056=y00[i]-y000
   c056=a056*a056
   d056=a056*b056
   a56=d056/c056
   l56.append(a56)
b56=sum(l56)/n

print("56.ViolentCrimesPerPop-PctRecImmig5: ",b56)




x57 = df['PctRecImmig8']
x057 = x57.to_list()
# print(x057)
sum057=0
for i in range(n):
    sum057=sum057+x057[i]
avg057=sum057/n
print("57.PctRecImmig8 Average: ",avg057)
l57=[]    
for i in range(n):
   
   a057=x057[i]-avg057
   b057=y00[i]-y000
   c057=a057*a057
   d057=a057*b057
   a57=d057/c057
   l57.append(a57)
b57=sum(l57)/n

print("57.ViolentCrimesPerPop-PctRecImmig8: ",b57)



x58 = df['PctRecImmig10']
x058 = x58.to_list()
# print(x058)
sum058=0
for i in range(n):
    sum058=sum058+x058[i]
avg058=sum058/n
print("58.PctRecImmig10 Average: ",avg058)
l58=[]    
for i in range(n):
   
   a058=x058[i]-avg058
   b058=y00[i]-y000
   c058=a058*a058
   d058=a058*b058
   a58=d058/c058
   l58.append(a58)
b58=sum(l58)/n

print("58.ViolentCrimesPerPop-PctRecImmig10: ",b58)



x59 = df['PctSpeakEnglOnly']
x059 = x59.to_list()
# print(x059)
sum059=0
for i in range(n):
    sum059=sum059+x059[i]
avg059=sum059/n
print("59.PctSpeakEnglOnly Average: ",avg059)
l59=[]    
for i in range(n):
   
   a059=x059[i]-avg059
   b059=y00[i]-y000
   c059=a059*a059
   d059=a059*b059
   a59=d059/c059
   l59.append(a59)
b59=sum(l59)/n

print("59.ViolentCrimesPerPop-PctSpeakEnglOnly: ",b59)




x60 = df['PctNotSpeakEnglWell']
x060 = x60.to_list()
# print(x060)
sum060=0
for i in range(n):
    sum060=sum060+x060[i]
avg060=sum060/n
print("60.PctNotSpeakEnglWell Average: ",avg060)
l60=[]    
for i in range(n):
   
   a060=x060[i]-avg060
   b060=y00[i]-y000
   c060=a060*a060
   d060=a060*b060
   a60=d060/c060
   l60.append(a60)
b60=sum(l60)/n

print("60.ViolentCrimesPerPop-PctNotSpeakEnglWell: ",b60)




x61 = df['PctLargHouseFam']
x061 = x61.to_list()
# print(x061)
sum061=0
for i in range(n):
    sum061=sum061+x061[i]
avg061=sum061/n
print("61.PctLargHouseFam Average: ",avg061)
l61=[]    
for i in range(n):
   
   a061=x061[i]-avg061
   b061=y00[i]-y000
   c061=a061*a061
   d061=a061*b061
   a61=d061/c061
   l61.append(a61)
b61=sum(l61)/n

print("61.ViolentCrimesPerPop-PctLargHouseFam: ",b61)



x62 = df['PctLargHouseOccup']
x062 = x62.to_list()
# print(x062)
sum062=0
for i in range(n):
    sum062=sum062+x062[i]
avg062=sum062/n
print("62.PctLargHouseOccup Average: ",avg062)
l62=[]    
for i in range(n):
   
   a062=x062[i]-avg062
   b062=y00[i]-y000
   c062=a062*a062
   d062=a062*b062
   a62=d062/c062
   l62.append(a62)
b62=sum(l62)/n

print("62.ViolentCrimesPerPop-PctLargHouseOccup: ",b62)




x63 = df['PersPerOccupHous']
x063 = x63.to_list()
# print(x063)
sum063=0
for i in range(n):
    sum063=sum063+x063[i]
avg063=sum063/n
print("63.PersPerOccupHous Average: ",avg063)
l63=[]    
for i in range(n):
   
   a063=x063[i]-avg063
   b063=y00[i]-y000
   c063=a063*a063
   d063=a063*b063
   a63=d063/c063
   l63.append(a63)
b63=sum(l63)/n

print("63.ViolentCrimesPerPop-PersPerOccupHous: ",b63)



x64 = df['PersPerOwnOccHous']
x064 = x64.to_list()
# print(x064)
sum064=0
for i in range(n):
    sum064=sum064+x064[i]
avg064=sum064/n
print("64.PersPerOwnOccHous Average: ",avg064)
l64=[]    
for i in range(n):
   
   a064=x064[i]-avg064
   b064=y00[i]-y000
   c064=a064*a064
   d064=a064*b064
   a64=d064/c064
   l64.append(a64)
b64=sum(l64)/n

print("64.ViolentCrimesPerPop-PersPerOwnOccHous: ",b64)




x65 = df['PersPerRentOccHous']
x065 = x65.to_list()
# print(x065)
sum065=0
for i in range(n):
    sum065=sum065+x065[i]
avg065=sum065/n
print("65.PersPerRentOccHous Average: ",avg065)
l65=[]    
for i in range(n):
   
   a065=x065[i]-avg065
   b065=y00[i]-y000
   c065=a065*a065
   d065=a065*b065
   a65=d065/c065
   l65.append(a65)
b65=sum(l65)/n

print("65.ViolentCrimesPerPop-PersPerRentOccHous: ",b65)



x66 = df['PctPersOwnOccup']
x066 = x66.to_list()
# print(x066)
sum066=0
for i in range(n):
    sum066=sum066+x066[i]
avg066=sum066/n
print("66.PctPersOwnOccup Average: ",avg066)
l66=[]    
for i in range(n):
   
   a066=x066[i]-avg066
   b066=y00[i]-y000
   c066=a066*a066
   d066=a066*b066
   a66=d066/c066
   l66.append(a66)
b66=sum(l66)/n

print("66.ViolentCrimesPerPop-PctPersOwnOccup: ",b66)




x67 = df['PctPersDenseHous']
x067 = x67.to_list()
# print(x067)
sum067=0
for i in range(n):
    sum067=sum067+x067[i]
avg067=sum067/n
print("67.PctPersDenseHous Average: ",avg067)
l67=[]    
for i in range(n):
   
   a067=x067[i]-avg067
   b067=y00[i]-y000
   c067=a067*a067
   d067=a067*b067
   a67=d067/c067
   l67.append(a67)
b67=sum(l67)/n

print("67.ViolentCrimesPerPop-PctPersDenseHous: ",b67)



x68 = df['PctHousLess3BR']
x068 = x68.to_list()
# print(x068)
sum068=0
for i in range(n):
    sum068=sum068+x068[i]
avg068=sum068/n
print("68.PctHousLess3BR Average: ",avg068)
l68=[]    
for i in range(n):
   
   a068=x068[i]-avg068
   b068=y00[i]-y000
   c068=a068*a068
   d068=a068*b068
   a68=d068/c068
   l68.append(a68)
b68=sum(l68)/n

print("68.ViolentCrimesPerPop-PctHousLess3BR: ",b68)




x69 = df['HousVacant']
x069 = x69.to_list()
# print(x069)
sum069=0
for i in range(n):
    sum069=sum069+x069[i]
avg069=sum069/n
print("69.HousVacant Average: ",avg069)
l69=[]    
for i in range(n):
   
   a069=x069[i]-avg069
   b069=y00[i]-y000
   c069=a069*a069
   d069=a069*b069
   a69=d069/c069
   l69.append(a69)
b69=sum(l69)/n

print("69.ViolentCrimesPerPop-HousVacant: ",b69)



x70 = df['PctHousOccup']
x070 = x70.to_list()
# print(x070)
sum070=0
for i in range(n):
    sum070=sum070+x070[i]
avg070=sum070/n
print("70.PctHousOccup Average: ",avg070)
l70=[]    
for i in range(n):
   
   a070=x070[i]-avg070
   b070=y00[i]-y000
   c070=a070*a070
   d070=a070*b070
   a70=d070/c070
   l70.append(a70)
b70=sum(l70)/n

print("70.ViolentCrimesPerPop-PctHousOccup: ",b70)




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



x72 = df['PctVacantBoarded']
x072 = x72.to_list()
# print(x072)
sum072=0
for i in range(n):
    sum072=sum072+x072[i]
avg072=sum072/n
print("72.PctVacantBoarded Average: ",avg072)
l72=[]    
for i in range(n):
   
   a072=x072[i]-avg072
   b072=y00[i]-y000
   c072=a072*a072
   d072=a072*b072
   a72=d072/c072
   l72.append(a72)
b72=sum(l72)/n

print("72.ViolentCrimesPerPop-PctVacantBoarded: ",b72)




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



x74 = df['MedYrHousBuilt']
x074 = x74.to_list()
# print(x074)
sum074=0
for i in range(n):
    sum074=sum074+x074[i]
avg074=sum074/n
print("74.MedYrHousBuilt Average: ",avg074)
l74=[]    
for i in range(n):
   
   a074=x074[i]-avg074
   b074=y00[i]-y000
   c074=a074*a074
   d074=a074*b074
   a74=d074/c074
   l74.append(a74)
b74=sum(l74)/n

print("74.ViolentCrimesPerPop-MedYrHousBuilt: ",b74)



x75 = df['PctHousNoPhone']
x075 = x75.to_list()
# print(x075)
sum075=0
for i in range(n):
    sum075=sum075+x075[i]
avg075=sum075/n
print("75.PctHousNoPhone Average: ",avg075)
l75=[]    
for i in range(n):
   
   a075=x075[i]-avg075
   b075=y00[i]-y000
   c075=a075*a075
   d075=a075*b075
   a75=d075/c075
   l75.append(a75)
b75=sum(l75)/n

print("75.ViolentCrimesPerPop-PctHousNoPhone: ",b75)



x76 = df['PctWOFullPlumb']
x076 = x76.to_list()
# print(x076)
sum076=0
for i in range(n):
    sum076=sum076+x076[i]
avg076=sum076/n
print("76.PctWOFullPlumb Average: ",avg076)
l76=[]    
for i in range(n):
   
   a076=x076[i]-avg076
   b076=y00[i]-y000
   c076=a076*a076
   d076=a076*b076
   a76=d076/c076
   l76.append(a76)
b76=sum(l76)/n

print("76.ViolentCrimesPerPop-PctWOFullPlumb: ",b76)




x77 = df['OwnOccLowQuart']
x077 = x77.to_list()
# print(x077)
sum077=0
for i in range(n):
    sum077=sum077+x077[i]
avg077=sum077/n
print("77.OwnOccLowQuart Average: ",avg077)
l77=[]    
for i in range(n):
   
   a077=x077[i]-avg077
   b077=y00[i]-y000
   c077=a077*a077
   d077=a077*b077
   a77=d077/c077
   l77.append(a77)
b77=sum(l77)/n

print("77.ViolentCrimesPerPop-OwnOccLowQuart: ",b77)



x78 = df['OwnOccMedVal']
x078 = x78.to_list()
# print(x078)
sum078=0
for i in range(n):
    sum078=sum078+x078[i]
avg078=sum078/n
print("78.OwnOccMedVal Average: ",avg078)
l78=[]    
for i in range(n):
   
   a078=x078[i]-avg078
   b078=y00[i]-y000
   c078=a078*a078
   d078=a078*b078
   a78=d078/c078
   l78.append(a78)
b78=sum(l78)/n

print("78.ViolentCrimesPerPop-OwnOccMedVal: ",b78)




x79 = df['OwnOccHiQuart']
x079 = x79.to_list()
# print(x079)
sum079=0
for i in range(n):
    sum079=sum079+x079[i]
avg079=sum079/n
print("79.OwnOccHiQuart Average: ",avg079)
l79=[]    
for i in range(n):
   
   a079=x079[i]-avg079
   b079=y00[i]-y000
   c079=a079*a079
   d079=a079*b079
   a79=d079/c079
   l79.append(a79)
b79=sum(l79)/n

print("79.ViolentCrimesPerPop-OwnOccHiQuart: ",b79)



x80 = df['RentLowQ']
x080 = x80.to_list()
# print(x080)
sum080=0
for i in range(n):
    sum080=sum080+x080[i]
avg080=sum080/n
print("80.RentLowQ Average: ",avg080)
l80=[]    
for i in range(n):
   
   a080=x080[i]-avg080
   b080=y00[i]-y000
   c080=a080*a080
   d080=a080*b080
   a80=d080/c080
   l80.append(a80)
b80=sum(l80)/n

print("80.ViolentCrimesPerPop-RentLowQ: ",b80)



x81 = df['RentMedian']
x081 = x81.to_list()
# print(x081)
sum081=0
for i in range(n):
    sum081=sum081+x081[i]
avg081=sum081/n
print("81.RentMedian Average: ",avg081)
l81=[]    
for i in range(n):
   
   a081=x081[i]-avg081
   b081=y00[i]-y000
   c081=a081*a081
   d081=a081*b081
   a81=d081/c081
   l81.append(a81)
b81=sum(l81)/n

print("81.ViolentCrimesPerPop-RentMedian: ",b81)


x82 = df['RentMedian']
x082 = x82.to_list()
# print(x082)
sum082=0
for i in range(n):
    sum082=sum082+x082[i]
avg082=sum082/n
print("82.RentMedian Average: ",avg082)
l82=[]    
for i in range(n):
   
   a082=x082[i]-avg082
   b082=y00[i]-y000
   c082=a082*a082
   d082=a082*b082
   a82=d082/c082
   l82.append(a82)
b82=sum(l82)/n

print("82.ViolentCrimesPerPop-RentMedian: ",b82)



x83 = df['RentHighQ']
x083 = x83.to_list()
# print(x083)
sum083=0
for i in range(n):
    sum083=sum083+x083[i]
avg083=sum083/n
print("83.RentHighQ Average: ",avg083)
l83=[]    
for i in range(n):
   
   a083=x083[i]-avg083
   b083=y00[i]-y000
   c083=a083*a083
   d083=a083*b083
   a83=d083/c083
   l83.append(a83)
b83=sum(l83)/n

print("83.ViolentCrimesPerPop-RentHighQ: ",b83)



x84 = df['MedRent']
x084 = x84.to_list()
# print(x084)
sum084=0
for i in range(n):
    sum084=sum084+x084[i]
avg084=sum084/n
print("84.MedRent Average: ",avg084)
l84=[]    
for i in range(n):
   
   a084=x084[i]-avg084
   b084=y00[i]-y000
   c084=a084*a084
   d084=a084*b084
   a84=d084/c084
   l84.append(a84)
b84=sum(l84)/n

print("84.ViolentCrimesPerPop-MedRent: ",b84)



x85 = df['MedRentPctHousInc']
x085 = x85.to_list()
# print(x085)
sum085=0
for i in range(n):
    sum085=sum085+x085[i]
avg085=sum085/n
print("85.MedRentPctHousInc Average: ",avg085)
l85=[]    
for i in range(n):
   
   a085=x085[i]-avg085
   b085=y00[i]-y000
   c085=a085*a085
   d085=a085*b085
   a85=d085/c085
   l85.append(a85)
b85=sum(l85)/n

print("85.ViolentCrimesPerPop-MedRentPctHousInc: ",b85)



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



x87 = df['MedOwnCostPctIncNoMtg']
x087 = x87.to_list()
# print(x087)
sum087=0
for i in range(n):
    sum087=sum087+x087[i]
avg087=sum087/n
print("87.MedOwnCostPctIncNoMtg Average: ",avg087)
l87=[]    
for i in range(n):
   
   a087=x087[i]-avg087
   b087=y00[i]-y000
   c087=a087*a087
   d087=a087*b087
   a87=d087/c087
   l87.append(a87)
b87=sum(l87)/n

print("87.ViolentCrimesPerPop-MedOwnCostPctIncNoMtg: ",b87)



x88 = df['PctForeignBorn']
x088 = x88.to_list()
# print(x088)
sum088=0
for i in range(n):
    sum088=sum088+x088[i]
avg088=sum088/n
print("88.PctForeignBorn Average: ",avg088)
l88=[]    
for i in range(n):
   
   a088=x088[i]-avg088
   b088=y00[i]-y000
   c088=a088*a088
   d088=a088*b088
   a88=d088/c088
   l88.append(a88)
b88=sum(l88)/n

print("88.ViolentCrimesPerPop-PctForeignBorn: ",b88)



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



x90 = df['PctSameHouse85']
x090 = x90.to_list()
# print(x090)
sum090=0
for i in range(n):
    sum090=sum090+x090[i]
avg090=sum090/n
print("90.PctSameHouse85 Average: ",avg090)
l90=[]    
for i in range(n):
   
   a090=x090[i]-avg090
   b090=y00[i]-y000
   c090=a090*a090
   d090=a090*b090
   a90=d090/c090
   l90.append(a90)
b90=sum(l90)/n

print("90.ViolentCrimesPerPop-PctSameHouse85: ",b90)



x91 = df['PctSameCity85']
x091 = x91.to_list()
# print(x091)
sum091=0
for i in range(n):
    sum091=sum091+x091[i]
avg091=sum091/n
print("91.PctSameCity85 Average: ",avg091)
l91=[]    
for i in range(n):
   
   a091=x091[i]-avg091
   b091=y00[i]-y000
   c091=a091*a091
   d091=a091*b091
   a91=d091/c091
   l91.append(a91)
b91=sum(l91)/n

print("91.ViolentCrimesPerPop-PctSameCity85: ",b91)



x92 = df['PctSameState85']
x092 = x92.to_list()
# print(x092)
sum092=0
for i in range(n):
    sum092=sum092+x092[i]
avg092=sum092/n
print("92.PctSameState85 Average: ",avg092)
l92=[]    
for i in range(n):
   
   a092=x092[i]-avg092
   b092=y00[i]-y000
   c092=a092*a092
   d092=a092*b092
   a92=d092/c092
   l92.append(a92)
b92=sum(l92)/n

print("92.ViolentCrimesPerPop-PctSameState85: ",b92)





b01=(b1*avg01+b2*avg02+b3*avg03+b4*avg04+b5*avg05+b6*avg06+b7*avg07+b8*avg08+b9*avg09+b10*avg010+b11*avg011+b12*avg012+b13*avg013+b14*avg014+b15*avg015)
b02=(b16*avg016+b17*avg017+b18*avg018+b19*avg019+b20*avg020+b21*avg021+b22*avg022+b23*avg023+b24*avg024+b25*avg025+b26*avg026+b27*avg027+b28*avg028+b29*avg029+b30*avg030)
b03=(b31*avg031+b32*avg032+b33*avg033+b34*avg034+b35*avg035+b36*avg036+b37*avg037+b38*avg038+b39*avg039+b40*avg040+b41*avg041+b42*avg042+b43*avg043+b44*avg044+b45*avg045)
b04=(b46*avg046+b47*avg047+b48*avg048+b49*avg049+b50*avg050+b51*avg051+b52*avg052+b53*avg053+b54*avg054+b55*avg055+b56*avg056+b57*avg057+b58*avg058+b59*avg059+b60*avg060)
b05=(b61*avg061+b62*avg062+b63*avg063+b64*avg064+b65*avg065+b66*avg066+b67*avg067+b68*avg068+b69*avg069+b70*avg070+b71*avg071+b72*avg072+b73*avg073+b74*avg074+b75*avg075)
b06=(b76*avg076+b77*avg077+b78*avg078+b79*avg079+b80*avg080+b81*avg081+b82*avg082+b83*avg083+b84*avg084+b85*avg085+b86*avg086+b87*avg087+b88*avg088+b89*avg089+b90*avg090)
b07=(b91*avg091+b92*avg092)

b0=y000-(b01+b02+b03+b04+b05+b06+b07)
print("The Corelation Coefficiant: ",b0)



# Testing Part........
e=2.718
l118=[]

for i in range(n,1994):
    
    y01=b1*x01[i]+b2*x02[i]+b3*x03[i]+b4*x04[i]+b5*x05[i]+b6*x06[i]+b7*x07[i]+b8*x08[i]+b9*x09[i]+b10*x010[i]+b11*x011[i]+b12*x012[i]+b13*x013[i]+b14*x014[i]+b15*x015[i]
    y02=b16*x016[i]+b17*x017[i]+b18*x018[i]+b19*x019[i]+b20*x020[i]+b21*x021[i]+b22*x022[i]+b23*x023[i]+b24*x024[i]+b25*x025[i]+b26*x026[i]+b27*x027[i]+b28*x028[i]+b29*x029[i]+b30*x030[i]
    y03=b31*x031[i]+b32*x032[i]+b33*x033[i]+b34*x034[i]+b35*x035[i]+b36*x036[i]+b37*x037[i]+b38*x038[i]+b39*x039[i]+b40*x040[i]+b41*x041[i]+b42*x042[i]+b43*x043[i]+b44*x044[i]+b45*x045[i]
    y04=b46*x046[i]+b47*x047[i]+b48*x048[i]+b49*x049[i]+b50*x050[i]+b51*x051[i]+b52*x052[i]+b53*x053[i]+b54*x054[i]+b55*x055[i]+b56*x056[i]+b57*x057[i]+b58*x058[i]+b59*x059[i]+b60*x060[i]
    y05=b61*x061[i]+b62*x062[i]+b63*x063[i]+b64*x064[i]+b65*x065[i]+b66*x066[i]+b67*x067[i]+b68*x068[i]+b69*x069[i]+b70*x070[i]+b71*x071[i]+b72*x072[i]+b73*x073[i]+b74*x074[i]+b75*x075[i]
    y06=b76*x076[i]+b77*x077[i]+b78*x078[i]+b79*x079[i]+b80*x080[i]+b81*x081[i]+b82*x082[i]+b83*x083[i]+b84*x084[i]+b85*x085[i]+b86*x086[i]+b87*x087[i]+b88*x088[i]+b89*x089[i]+b90*x090[i]
    y07=b91*x091[i]+b92*x092[i]

    y=b0+y01+y02+y03+y04+y05+y06+y07
    
    
    y0f=1+pow(e,-y)
    yf=1/y0f
    #print(yf)
    if(yf>=0.05):
       a=1
       l118.append(a)
    else:
        a=0
        l118.append(a)


#print(l118)


tp=0
tn=0
fp=0
fn=0
for i in range(1994-n):
    if(l118[i]==l[i]==1):
        tp=tp+1
    elif(l118[i]==l[i]==0):
        tn=tn+1
    elif(l118[i]==1 & l[i]==0):
        fn=fn+1
    else:
        fp=fp+1
print("true positive:",tp)
print("true negative:",tn)
print("false positive:",fp)
print("false negative:",fn)
accuracygood=((tp+tn)/(tp+tn+fp+fn))*100
print("The new accuracy: ",accuracygood)  
re=(tp/(tp+fn))*100
pre=(tp/(tp+fp))*100
f1_s=((2*re*pre)/(re+pre))
print("Recall: ",re)
print("Precision: ",pre)
print("F1_Score: ",f1_s)


