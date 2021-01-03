# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=bank_data
#Code starts here
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var.shape)

numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var.shape)

banks=bank.drop(columns='Loan_ID')

bank_mode=banks.mode()

banks=banks.replace(to_replace = np.nan, value = bank_mode)
print(banks.shape ,banks.isnull().sum().values.sum())

avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount',aggfunc='mean')



loan_approved_se=banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']=='Y')].count().max()

loan_approved_nse=banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status']=='Y')].count().max()

Loan_Status=614

percentage_se=loan_approved_se/Loan_Status*100
percentage_nse=loan_approved_nse/Loan_Status*100

print(percentage_se,percentage_nse)

loan_term=banks["Loan_Amount_Term"].apply(lambda x:x/12)

big_loan_term=len(loan_term[loan_term >= 25].index)
print(big_loan_term)

loan_groupby=banks.groupby("Loan_Status")[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values)












