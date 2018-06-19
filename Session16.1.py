
import numpy as np 
import pandas as pd
import math 


Dataset = np.array([1550,1700, 900, 850, 1000, 950])
Mean = Dataset.mean()
print("Mean of the Value:-")
print(Mean)
N= Dataset.size
Method = lambda V: pow(abs(V-Mean),2)  
    
Df = pd.DataFrame(Dataset,columns={'X'})

Df.describe()

Df['(X - X^)2'] = Df['X'].apply(Method)
Df.head(10)
Sigma = Df['(X - X^)2'].sum()

print("Sigma  :-\n",Sigma)
variance =Sigma/N 

print("Variance for Data :\n",variance)

print("Standard Deviation :\n",math.sqrt(variance))

print("Standard Deviation using Pd.Datafame.std():\n",Df['X'].std())