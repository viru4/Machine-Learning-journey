import  numpy as np

salary = np.array([20000,25000,30000,35000,40000])
# feature scaling standardization
# z=((x-np.mean(salary))/np.std(salary) for x in salary)
z=((salary-np.mean(salary))/np.std(salary))

print(z)