
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import KFold



df = pd.read_csv("D:\college project\Research Paper 02\Files and Papers\Selected_Feilds_Crime_data_Set_Main.csv")
#df = pd.read_excel(r"D:\college project\Research Paper 02\Files and Papers\Lung Cancer new.xlsx")
#print(df)

# generate 2 class dataset
#X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)
X= df.drop(columns= 'LUNG_CANCER', axis=1)
y = df['LUNG_CANCER']

#print(X)
#print(y)

X = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 4)

# Initialize KFold
kf = KFold(n_splits=10, shuffle=True, random_state=42) 

# Iterate over each fold
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    
    
    model_SVC = SVC(kernel = 'rbf', random_state = 4)
    # Convert your target variable to discrete classes if it's intended for classification.
    # Here's a simple example using a threshold to binarize the data:
    if(type(y_train)!=int):
        threshold = 0.5  # Set an appropriate threshold value
        y_train_binary = (y_train > threshold).astype(int)
    else:
        y_train_binary=y_train
    
    # Now, use the binarized target for training:
    model_SVC.fit(X_train, y_train_binary)
    y_pred_svm = model_SVC.decision_function(X_test)
    
    
    model_logistic = LogisticRegression()
    model_logistic.fit(X_train, y_train_binary)
    
    y_pred_logistic = model_logistic.decision_function(X_test)
    
    
    
    if(type(y_test)!=int):
        threshold = 0.5  # Set an appropriate threshold value
        y_test_binary = (y_test > threshold).astype(int)
    else:
        y_test_binary=y_test
    
    
    
    logistic_fpr, logistic_tpr, threshold = roc_curve(y_test_binary, y_pred_logistic)
    auc_logistic = auc(logistic_fpr, logistic_tpr)
    
    svm_fpr, svm_tpr, threshold = roc_curve(y_test_binary, y_pred_svm)
    auc_svm = auc(svm_fpr, svm_tpr)
    
    plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(svm_fpr, svm_tpr, linestyle='-', label='SVM (auc = %0.3f)' % auc_svm)
    plt.plot(logistic_fpr, logistic_tpr, marker='.', label='Logistic (auc = %0.3f)' % auc_logistic)
    
    plt.xlabel('False Positive Rate -->')
    plt.ylabel('True Positive Rate -->')
    
    plt.legend()
    
    plt.show()

