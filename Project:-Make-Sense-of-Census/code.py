# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record=np.asarray(new_record)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here

census=np.concatenate((data,new_record))
print(census.shape)
age=census[:,0]
print(age)

max_age=age.max()
min_age=age.min()
age_mean=round(np.mean(age),2)
age_std=round(np.std(age),2)
print(max_age,min_age,age_mean,age_std,sep='\n')

race=census[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]

len_0=len(race_0)
len_1=np.size(race_1)
len_2=np.size(race_2)
len_3=np.size(race_3)
len_4=np.size(race_4)

min_=[len_0,len_1,len_2,len_3,len_4]
minority_race=min_.index(min(min_))
print(minority_race)


senior_citizens=census[census[:,0]>60,:]

working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)

avg_working_hours=round(working_hours_sum/senior_citizens_len,2)

print(avg_working_hours)

education_num=census[:,1]
high=census[education_num>10,:]
low=census[education_num<=10,:]

avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])

print(round(avg_pay_high,2),round(avg_pay_low,2),avg_pay_high==avg_pay_low,sep='\n')






