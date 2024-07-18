#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import os


# In[3]:


os.chdir("C:\\Users\\s\\Desktop")


# In[5]:


#Q1. part4

import pandas as pd
import numpy as np 
import os


# In[6]:


os.chdir("C:\\Users\\s\\Desktop")


# In[9]:


Variable_name = pd.read_csv("Dentistry Dataset.csv")


# In[21]:


missing_values = Variable_name.isnull().sum()
print("Missing values before handling:")
print(missing_values)

Variable_name_dropped = Variable_name.dropna()

Variable_name_filled = Variable_name.fillna(Variable_name.mean())

missing_values_after = Variable_name_dropped.isnull().sum()

print("Missing values after handling:")
print(missing_values_after)


# In[14]:


#2



import pandas as pd                                         
import numpy as np                                           
import matplotlib.pyplot as plt 	       
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import os


# In[15]:


os.chdir("C:\\Users\\s\\Desktop")


# In[17]:


Variable_name = pd.read_csv("Dentistry Dataset.csv")


# In[20]:


Variable_name = pd.read_csv("Dentistry Dataset.csv")

categorical_cols = Variable_name.select_dtypes(include=['object']).columns
print("Categorical columns:", categorical_cols)


label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    Variable_name[col] = le.fit_transform(Variable_name[col])
    label_encoders[col] = le

print(Variable_name.head())


# In[6]:


os.chdir("C:\\Users\\s\\Desktop")


# In[8]:


Variable_name = pd.read_csv("Dentistry Dataset.csv")


# In[19]:


#3



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

file_path = 'Dentistry Dataset.csv'
df = pd.read_csv(file_path)

print(df.head())

Y = df['inter canine distance intraoral']

X = df.drop(columns=['inter canine distance intraoral', 'Sl No', 'Sample ID'])

le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])

print("Independent Variables (X):")
print(X.head())

print("Dependent Variable (Y):")
print(Y.head())


# In[16]:


Variable_name = pd.read_csv("Dentistry Dataset.csv")


# In[20]:


#4


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, Normalizer

file_path = 'Dentistry Dataset.csv'
df = pd.read_csv(file_path)

print(df.head())

Y = df['inter canine distance intraoral']

X = df.drop(columns=['inter canine distance intraoral', 'Sl No', 'Sample ID'])

le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])

normalizer = Normalizer()
X_normalized = normalizer.fit_transform(X)

X_normalized = pd.DataFrame(X_normalized, columns=X.columns)

print("Normalized Independent Variables (X):")
print(X_normalized.head())

print("Dependent Variable (Y):")
print(Y.head())


# In[22]:


#part 5 (1)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Dentistry Dataset.csv'
df = pd.read_csv(file_path)

Y = df['inter canine distance intraoral']

X = df.drop(columns=['inter canine distance intraoral', 'Sl No', 'Sample ID'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])

df_combined = X.copy()
df_combined['inter canine distance intraoral'] = Y

corr_matrix = df_combined.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()



# In[2]:


import pandas as pd                                         
import numpy as np                                           
import matplotlib.pyplot as plt 	       
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import os


# In[3]:


os.chdir("C:\\Users\\s\\Desktop")


# In[4]:


pd.read_csv("Dentistry Dataset.csv")


# In[9]:


import pandas as pd


# In[10]:


data = pd.read_csv("Dentistry Dataset.csv")


# In[11]:


data


# In[16]:


data = data[["Sample ID","Age","Gender"]]


# In[17]:


data


# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = '/mnt/data/Dentistry_Dataset[1].csv'
data = pd.read_csv(file_path)

# Drop unwanted columns
data_cleaned = data.drop(columns=['Sl No', 'Sample ID'])

# Define the independent variables (X) and the dependent variable (y)
# Assuming 'Age' is the dependent variable for this example
X = data_cleaned.drop(columns=['Age'])
y = data_cleaned['Age']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shape of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = 'Dentistry.csv'
data = pd.read_csv(file_path)

# Assuming the target variable is 'intercanine distance casts' (please replace it if it's different)
target = 'intercanine distance casts'
features = data.drop(columns=['Sl No', 'Sample ID', 'Gender', target])

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, data[target], test_size=0.2, random_state=42)

# Display the shapes of the resulting sets
print(f"Training features: {X_train.shape}")
print(f"Test features: {X_test.shape}")
print(f"Training labels: {y_train.shape}")
print(f"Test labels: {y_test.shape}")


# In[ ]:




