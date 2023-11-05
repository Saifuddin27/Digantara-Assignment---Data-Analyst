#!/usr/bin/env python
# coding: utf-8

# # Question 1
# A) Derive high level analytics from the whole data set for a single day. In other
# words, derive general analytics of the whole set of conjunction scenarios (for e.g.
# number of conjunctions among active satellites). The analytics should be intuitive
# and represented in an easily understandable format.

# In[13]:


import pandas as pd
pd.set_option('display.max_rows', None)
# Step 1: Data Retrieval and Exploration
data = pd.read_csv('sort-minRange.csv')
data.head()  # Display the first few rows to understand the data


# In[14]:


#Getting information of the check detaails like nullvalues, datatype, etc..
data.info()


# In[15]:


# Step 2: Descriptive Analytics
total_conjunctions = len(data)
active_satellites_conjunctions = len(data)
print(total_conjunctions,active_satellites_conjunctions)


# In[16]:


# Step 3: Data Visualization
import matplotlib.pyplot as plt

plt.bar(['Total Conjunctions'], [total_conjunctions])
plt.xlabel('Metric')
plt.ylabel('Count')
plt.title('Conjunction Analytics for a Single Day')
plt.show()


# # 

# B) Represent the conjunctions data of a single satellite or a satellite constellation.
# The analytics should be intuitive, represented in an easily understandable format and
# should enable decision making from a satellite operator’s point of view.

# In[19]:


#Displaying all the unique 'OBJECT_NAME_1' to select the appropriate one
data["OBJECT_NAME_1"].value_counts()


# In[20]:


# Step 1: Data Filtering
chosen_satellite = 'STARLINK-2467 [+]'  # Selecting single object in 'OBJECT_NAME_1'
chosen_data = data[data['OBJECT_NAME_1'] == chosen_satellite]
chosen_data.head()


# In[21]:


# Step 2: Descriptive Analytics
conjunctions_count = len(chosen_data)
conjunctions_count


# In[23]:


# Step 3: Data Visualization (for example, using a scatter plot)
plt.figure(figsize=(8, 6))
plt.scatter(chosen_data['TCA'], chosen_data['MAX_PROB'], c=chosen_data['MAX_PROB'], cmap='viridis', alpha=0.7)
plt.xlabel('TCA')
plt.ylabel('Maximum Probability')
plt.colorbar(label='Maximum Probability')
plt.xticks(rotation=5)
plt.title(f'Conjunctions for Satellite {chosen_satellite}')
plt.show()


# In[ ]:


# Step 4: Decision-Making Insights
# Provide insights based on the chosen satellite's conjunction data.

please help me with this part


# In[ ]:





# # 

# # Question 2
# Use the whole dataset that spans about five days. Derive analytics and visualise the
# data/analytics accounting for the evolution from the first day (for e.g. the number of
# conjunctions of the RSO having NORAD ID 12345 over 7 days of analysis)

# In[5]:


# Step 1: Data Retrieval and Aggregation
dfs = []
for day in range(1, 6):
    df = pd.read_csv('sort-minRange.csv')
    dfs.append(df)


# In[30]:


# Combine dataframes
merged_data = pd.concat(dfs, ignore_index=True)
merged_data.head()


# In[24]:


#Displaying all the unique 'NORAD_CAT_ID_1' to select the appropriate one
data["NORAD_CAT_ID_1"].value_counts()


# In[9]:


# Step 2: Temporal Analysis
norad_id = 57900   # Selecting specific 'NORAD_CAT_ID_1'
specific_data = merged_data[merged_data['NORAD_CAT_ID_1'] == norad_id]
specific_data.head()


# In[26]:


# Step 3: Data Visualization (for example, using a line plot)
plt.figure(figsize=(8, 6))
plt.plot(specific_data['TCA'], specific_data['MAX_PROB'], marker='+')
plt.xlabel('TCA')
plt.ylabel('Maximum Probability')
plt.title(f'Conjunctions for NORAD ID {norad_id} over 5 Days')
plt.xticks(rotation=10)
plt.grid(True)
plt.show()


# Step 4: Assumptions
# 
# When documenting assumptions made during the analysis, consider including the following:
# 
# 1.Data Accuracy:
# Assume that the provided data accurately represents the conjunction scenarios, taking into account any potential limitations or known inaccuracies.
# 
# 2.Conjunction Definition:
# Specify that conjunctions are defined based on predefined criteria, which may include minimum separation distance, relative speed, and maximum probability of collision.
# 
# 3.Active Satellites:
# Assume that "active satellites" refer to operational satellites that are currently in use, excluding decommissioned or non-functional satellites from the analysis.
# 
# 4.Orbital Dynamics:
# Assume that the orbital dynamics of the satellites follow established laws of celestial mechanics and that no significant perturbing forces are acting on them during the analysis.
# 
# 5.Response Time:
# Assume a predetermined response time for satellite operators to take action after being alerted about a potential conjunction. This response time can be based on industry standards or organizational policies.
# 
# 6.Risk Tolerance:
# Specify that there are predefined risk tolerance levels or thresholds that guide decision-making in conjunction scenarios. These thresholds may be based on industry best practices or specific organizational policies.
# 
# 7.External Factors:
# Consider and account for any external factors, such as space weather conditions or communication delays, that may impact conjunction assessments.

# In[ ]:




