#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# For example, if the dataset is in a CSV file named 'housing.csv'
# df = pd.read_csv('housing.csv')

# Creating a sample DataFrame based on the dataset variables
data = {
    'CRIM': [0.00632, 0.02731, 0.02729, 0.03237, 0.06905],
    'ZN': [18.0, 0.0, 0.0, 0.0, 0.0],
    'INDUS': [2.31, 7.07, 7.07, 2.18, 2.18],
    'CHAS': [0, 0, 0, 0, 0],
    'NOX': [0.538, 0.469, 0.469, 0.458, 0.458],
    'RM': [6.575, 6.421, 7.185, 6.998, 7.147],
    'AGE': [65.2, 78.9, 61.1, 45.8, 54.2],
    'DIS': [4.09, 4.9671, 4.9671, 6.0622, 6.0622],
    'RAD': [1, 2, 2, 3, 3],
    'TAX': [296, 242, 242, 222, 222],
    'PTRATIO': [15.3, 17.8, 17.8, 18.7, 18.7],
    'LSTAT': [4.98, 9.14, 4.03, 2.94, 5.33],
    'MEDV': [24.0, 21.6, 34.7, 33.4, 36.2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the boxplot for MEDV
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['MEDV'])
plt.title('Boxplot of Median Value of Owner-Occupied Homes')
plt.ylabel('MEDV in $1000\'s')
plt.show()


# In[ ]:





# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data: Creating a DataFrame based on the dataset description
data = {
    'CRIM': [0.00632, 0.02731, 0.02729, 0.03237, 0.06905, 0.02985, 0.08829, 0.14455, 0.21124, 0.17004],
    'ZN': [18.0, 0.0, 0.0, 0.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0],
    'INDUS': [2.31, 7.07, 7.07, 2.18, 2.18, 2.18, 7.87, 7.87, 7.87, 7.87],
    'CHAS': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'NOX': [0.538, 0.469, 0.469, 0.458, 0.458, 0.458, 0.524, 0.524, 0.524, 0.524],
    'RM': [6.575, 6.421, 7.185, 6.998, 7.147, 6.430, 6.012, 6.172, 5.631, 6.004],
    'AGE': [65.2, 78.9, 61.1, 45.8, 54.2, 58.7, 66.6, 96.1, 100.0, 85.9],
    'DIS': [4.09, 4.9671, 4.9671, 6.0622, 6.0622, 6.0622, 5.5605, 5.9505, 6.0821, 6.5921],
    'RAD': [1, 2, 2, 3, 3, 3, 5, 5, 5, 5],
    'TAX': [296, 242, 242, 222, 222, 222, 311, 311, 311, 311],
    'PTRATIO': [15.3, 17.8, 17.8, 18.7, 18.7, 18.7, 15.2, 15.2, 15.2, 15.2],
    'LSTAT': [4.98, 9.14, 4.03, 2.94, 5.33, 8.77, 10.48, 8.16, 6.21, 12.43],
    'MEDV': [24.0, 21.6, 34.7, 33.4, 36.2, 28.7, 27.1, 20.3, 18.2, 19.9]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the histogram for CHAS
plt.figure(figsize=(8, 6))
sns.histplot(df['CHAS'], bins=2, discrete=True)
plt.title('Histogram of Charles River Variable (CHAS)')
plt.xlabel('CHAS')
plt.ylabel('Frequency')
plt.xticks([0, 1], ['Does not bound river', 'Bounds river'])
plt.show()


# In[ ]:





# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data: Creating a DataFrame based on the dataset description
data = {
    'CRIM': [0.00632, 0.02731, 0.02729, 0.03237, 0.06905, 0.02985, 0.08829, 0.14455, 0.21124, 0.17004],
    'ZN': [18.0, 0.0, 0.0, 0.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0],
    'INDUS': [2.31, 7.07, 7.07, 2.18, 2.18, 2.18, 7.87, 7.87, 7.87, 7.87],
    'CHAS': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'NOX': [0.538, 0.469, 0.469, 0.458, 0.458, 0.458, 0.524, 0.524, 0.524, 0.524],
    'RM': [6.575, 6.421, 7.185, 6.998, 7.147, 6.430, 6.012, 6.172, 5.631, 6.004],
    'AGE': [65.2, 78.9, 61.1, 45.8, 54.2, 58.7, 66.6, 96.1, 100.0, 85.9],
    'DIS': [4.09, 4.9671, 4.9671, 6.0622, 6.0622, 6.0622, 5.5605, 5.9505, 6.0821, 6.5921],
    'RAD': [1, 2, 2, 3, 3, 3, 5, 5, 5, 5],
    'TAX': [296, 242, 242, 222, 222, 222, 311, 311, 311, 311],
    'PTRATIO': [15.3, 17.8, 17.8, 18.7, 18.7, 18.7, 15.2, 15.2, 15.2, 15.2],
    'LSTAT': [4.98, 9.14, 4.03, 2.94, 5.33, 8.77, 10.48, 8.16, 6.21, 12.43],
    'MEDV': [24.0, 21.6, 34.7, 33.4, 36.2, 28.7, 27.1, 20.3, 18.2, 19.9]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Discretize the AGE variable into three groups
age_bins = [0, 35, 50, 100]
age_labels = ['35 years and younger', '35 to 50 years', 'Older than 50 years']
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels)

# Create the boxplot for MEDV vs AGE_GROUP
plt.figure(figsize=(10, 6))
sns.boxplot(x='AGE_GROUP', y='MEDV', data=df)
plt.title('Boxplot of Median Value of Owner-Occupied Homes (MEDV) by Age Group')
plt.xlabel('Age Group')
plt.ylabel('MEDV in $1000\'s')
plt.show()


# In[ ]:





# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data: Creating a DataFrame based on the dataset description
data = {
    'CRIM': [0.00632, 0.02731, 0.02729, 0.03237, 0.06905, 0.02985, 0.08829, 0.14455, 0.21124, 0.17004],
    'ZN': [18.0, 0.0, 0.0, 0.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0],
    'INDUS': [2.31, 7.07, 7.07, 2.18, 2.18, 2.18, 7.87, 7.87, 7.87, 7.87],
    'CHAS': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'NOX': [0.538, 0.469, 0.469, 0.458, 0.458, 0.458, 0.524, 0.524, 0.524, 0.524],
    'RM': [6.575, 6.421, 7.185, 6.998, 7.147, 6.430, 6.012, 6.172, 5.631, 6.004],
    'AGE': [65.2, 78.9, 61.1, 45.8, 54.2, 58.7, 66.6, 96.1, 100.0, 85.9],
    'DIS': [4.09, 4.9671, 4.9671, 6.0622, 6.0622, 6.0622, 5.5605, 5.9505, 6.0821, 6.5921],
    'RAD': [1, 2, 2, 3, 3, 3, 5, 5, 5, 5],
    'TAX': [296, 242, 242, 222, 222, 222, 311, 311, 311, 311],
    'PTRATIO': [15.3, 17.8, 17.8, 18.7, 18.7, 18.7, 15.2, 15.2, 15.2, 15.2],
    'LSTAT': [4.98, 9.14, 4.03, 2.94, 5.33, 8.77, 10.48, 8.16, 6.21, 12.43],
    'MEDV': [24.0, 21.6, 34.7, 33.4, 36.2, 28.7, 27.1, 20.3, 18.2, 19.9]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the scatter plot for NOX vs INDUS
plt.figure(figsize=(10, 6))
sns.scatterplot(x='INDUS', y='NOX', data=df)
plt.title('Scatter Plot of NOX vs INDUS')
plt.xlabel('Proportion of Non-Retail Business Acres (INDUS)')
plt.ylabel('Nitric Oxides Concentration (NOX)')
plt.show()


# In[ ]:





# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data: Creating a DataFrame based on the dataset description
data = {
    'CRIM': [0.00632, 0.02731, 0.02729, 0.03237, 0.06905, 0.02985, 0.08829, 0.14455, 0.21124, 0.17004],
    'ZN': [18.0, 0.0, 0.0, 0.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0],
    'INDUS': [2.31, 7.07, 7.07, 2.18, 2.18, 2.18, 7.87, 7.87, 7.87, 7.87],
    'CHAS': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'NOX': [0.538, 0.469, 0.469, 0.458, 0.458, 0.458, 0.524, 0.524, 0.524, 0.524],
    'RM': [6.575, 6.421, 7.185, 6.998, 7.147, 6.430, 6.012, 6.172, 5.631, 6.004],
    'AGE': [65.2, 78.9, 61.1, 45.8, 54.2, 58.7, 66.6, 96.1, 100.0, 85.9],
    'DIS': [4.09, 4.9671, 4.9671, 6.0622, 6.0622, 6.0622, 5.5605, 5.9505, 6.0821, 6.5921],
    'RAD': [1, 2, 2, 3, 3, 3, 5, 5, 5, 5],
    'TAX': [296, 242, 242, 222, 222, 222, 311, 311, 311, 311],
    'PTRATIO': [15.3, 17.8, 17.8, 18.7, 18.7, 18.7, 15.2, 15.2, 15.2, 15.2],
    'LSTAT': [4.98, 9.14, 4.03, 2.94, 5.33, 8.77, 10.48, 8.16, 6.21, 12.43],
    'MEDV': [24.0, 21.6, 34.7, 33.4, 36.2, 28.7, 27.1, 20.3, 18.2, 19.9]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the histogram for PTRATIO
plt.figure(figsize=(10, 6))
sns.histplot(df['PTRATIO'], bins=10, kde=False)
plt.title('Histogram of Pupil to Teacher Ratio (PTRATIO)')
plt.xlabel('Pupil to Teacher Ratio')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




