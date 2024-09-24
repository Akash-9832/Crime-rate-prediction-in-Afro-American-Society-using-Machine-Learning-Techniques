l_10_fold=[0,194,394,594,794,994,1194,1394,1594,1794]

m=int(input("Enter the fold number (between 1 and 10): "))
if(m>=1 and m<=10): 
    
    n=l_10_fold[m-1]
    print(m,"Flod")
    
    import pandas as pd
    df = pd.read_csv("D:\Debanjan Personal\Research Paper 02\Files and Papers\crime_data.csv")
    #print(df)
    
    # Tranning Part........
    
    l_00=[]
    y0 = df['ViolentCrimesPerPop']
    y00 = y0.to_list()
    for i in range(n):
        l_00.append(y00[i])
    for i in range(n+199,1994):
        l_00.append(y00[i])
    #print(len(l_00))
    
    
    y000=0
    for i in range(len(l_00)):
       if(i<len(l_00)):
           y000+=l_00[i] 
    y000/=len(l_00)
    print("**ViolentCrimesPerPop Average: ",y000)
    
    
    
    # Taking testing data from violent crime........
    l=[]
    for i in range(n,n+199):
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
    l_01=[]
    for i in range(n):
        l_01.append(x015[i])
    for i in range(n+199,1994):
        l_01.append(x015[i])
    
    
    
    sum015=0
    for i in range(len(l_01)):
        sum015=sum015+l_01[i]
    avg015=sum015/len(l_01)
    print("15.pctWInvInc Average: ",avg015)
    
    
    
    l15=[]    
    for i in range(len(l_01)):
       
       a015=l_01[i]-avg015
       b015=l_00[i]-y000
       c015=a015*a015
       d015=a015*b015
       a15=d015/c015
       l15.append(a15)
    b15=sum(l15)/len(l_01)
    
    print("15.ViolentCrimesPerPop-pctWInvInc: ",b15)
    
    
    
    
    
    x37 = df['MalePctDivorce']
    x037 = x37.to_list()
    # print(x037)
    l_02=[]
    for i in range(n):
        l_02.append(x037[i])
    for i in range(n+199,1994):
        l_02.append(x037[i])
    
    
    
    sum037=0
    for i in range(len(l_02)):
        sum037=sum037+l_02[i]
    avg037=sum037/len(l_02)
    print("37.MalePctDivorce Average: ",avg037)
    
    
    
    l37=[]    
    for i in range(len(l_02)):
       
       a037=l_02[i]-avg037
       b037=l_00[i]-y000
       c037=a037*a037
       d037=a037*b037
       a37=d037/c037
       l37.append(a37)
    b37=sum(l37)/len(l_02)
    
    print("37.ViolentCrimesPerPop-MalePctDivorce: ",b37)
    
    
    
    
    
    x39 = df['FemalePctDiv']
    x039 = x39.to_list()
    # print(x039)
    l_03=[]
    for i in range(n):
        l_03.append(x039[i])
    for i in range(n+199,1994):
        l_03.append(x039[i])
        
    
    
    sum039=0
    for i in range(len(l_03)):
        sum039=sum039+l_03[i]
    avg039=sum039/len(l_03)
    print("39.FemalePctDiv Average: ",avg039)
    
    
    
    l39=[]    
    for i in range(len(l_03)):
       
       a039=l_03[i]-avg039
       b039=l_00[i]-y000
       c039=a039*a039
       d039=a039*b039
       a39=d039/c039
       l39.append(a39)
    b39=sum(l39)/len(l_03)
    
    print("39.ViolentCrimesPerPop-FemalePctDiv: ",b39)
    
    
    
    
    
    x40 = df['TotalPctDiv']
    x040 = x40.to_list()
    # print(x040)
    l_04=[]
    for i in range(n):
        l_04.append(x040[i])
    for i in range(n+199,1994):
        l_04.append(x040[i])
        
        
    
    sum040=0
    for i in range(len(l_04)):
        sum040=sum040+l_04[i]
    avg040=sum040/len(l_04)
    print("40.TotalPctDiv Average: ",avg040)
    
    
    
    
    l40=[]    
    for i in range(len(l_04)):
       
       a040=l_04[i]-avg040
       b040=l_00[i]-y000
       c040=a040*a040
       d040=a040*b040
       a40=d040/c040
       l40.append(a40)
    b40=sum(l40)/len(l_04)
    
    print("40.ViolentCrimesPerPop-TotalPctDiv: ",b40)
    
    
    
    
    
    x71 = df['PctHousOwnOcc']
    x071 = x71.to_list()
    # print(x071)
    l_05=[]
    for i in range(n):
        l_05.append(x071[i])
    for i in range(n+199,1994):
        l_05.append(x071[i])
        
        
    
    sum071=0
    for i in range(len(l_05)):
        sum071=sum071+l_05[i]
    avg071=sum071/len(l_05)
    print("71.PctHousOwnOcc Average: ",avg071)
    
    
    
    l71=[]    
    for i in range(len(l_05)):
       
       a071=l_05[i]-avg071
       b071=l_00[i]-y000
       c071=a071*a071
       d071=a071*b071
       a71=d071/c071
       l71.append(a71)
    b71=sum(l71)/len(l_05)
    
    print("71.ViolentCrimesPerPop-PctHousOwnOcc: ",b71)
    
    
    
    
    
    x73 = df['PctVacMore6Mos']
    x073 = x73.to_list()
    # print(x073)
    l_06=[]
    for i in range(n):
        l_06.append(x073[i])
    for i in range(n+199,1994):
        l_06.append(x073[i])
        
        
    
    sum073=0
    for i in range(len(l_06)):
        sum073=sum073+l_06[i]
    avg073=sum073/len(l_06)
    print("73.PctVacMore6Mos Average: ",avg073)
    
    
    
    l73=[]    
    for i in range(len(l_06)):
       
       a073=l_06[i]-avg073
       b073=l_00[i]-y000
       c073=a073*a073
       d073=a073*b073
       a73=d073/c073
       l73.append(a73)
    b73=sum(l73)/len(l_06)
    
    print("73.ViolentCrimesPerPop-PctVacMore6Mos: ",b73)
    
    
    
    
    
    x86 = df['MedOwnCostPctInc']
    x086 = x86.to_list()
    # print(x086)
    l_07=[]
    for i in range(n):
        l_07.append(x086[i])
    for i in range(n+199,1994):
        l_07.append(x086[i])
        
        
    
    sum086=0
    for i in range(len(l_07)):
        sum086=sum086+l_07[i]
    avg086=sum086/len(l_07)
    print("86.MedOwnCostPctInc Average: ",avg086)
    
    
    
    l86=[]    
    for i in range(len(l_07)):
       
       a086=l_07[i]-avg086
       b086=l_00[i]-y000
       c086=a086*a086
       d086=a086*b086
       a86=d086/c086
       l86.append(a86)
    b86=sum(l86)/len(l_07)
    
    print("86.ViolentCrimesPerPop-MedOwnCostPctInc: ",b86)
    
    
    
    x89 = df['PctBornSameState']
    x089 = x89.to_list()
    # print(x089)
    l_08=[]
    for i in range(n):
        l_08.append(x089[i])
    for i in range(n+199,1994):
        l_08.append(x089[i])
        
        
    
    sum089=0
    for i in range(len(l_08)):
        sum089=sum089+l_08[i]
    avg089=sum089/len(l_08)
    print("89.PctBornSameState Average: ",avg089)
    
    
    
    l89=[]    
    for i in range(len(l_08)):
       
       a089=l_08[i]-avg089
       b089=l_00[i]-y000
       c089=a089*a089
       d089=a089*b089
       a89=d089/c089
       l89.append(a89)
    b89=sum(l89)/len(l_08)
    
    print("89.ViolentCrimesPerPop-PctBornSameState: ",b89)
    
    
    b0=y000-(b015*avg015+b037*avg037+b039*avg039+b040*avg040+b071*avg071+b073*avg073+b086*avg086+b89*avg089)
    print("The Corelation Coefficiant: ",b0)
    
    
    # Testing Part........
    
    e=2.718
    l118=[]
    
    for i in range(n,n+199):
        
    
        y=b0+b15*x015[i]+b37*x037[i]+b39*x039[i]+b40*x040[i]+b71*x071[i]+b73*x073[i]+b86*x086[i]+b89*x089[i]
        
        
        y0f=1+pow(e,-y)
        yf=1/y0f
        print(yf)
        if(yf>=0.2):
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
    for i in range(194):
        if(l118[i]==1 and l[i]==1):
            tp=tp+1
        elif(l118[i]==1 and l[i]==0):
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
    sen=(tp/(tp+fn))*100
    re=(tn/(tn+fp))*100
    pre=(tp/(tp+fp))*100
    f1_s=((2*sen*pre)/(sen+pre))
    print("Recall: ",sen)
    print("Precision: ",pre)
    print("F1_Score: ",f1_s)
    print("Sensitivity: ",sen)
    print("Specificity: ",re)
    
else: print("Please enter valid fold number.")