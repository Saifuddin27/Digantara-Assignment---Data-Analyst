#!/usr/bin/env python
# coding: utf-8

# # Question 1
# A) Derive high level analytics from the whole data set for a single day. In other
# words, derive general analytics of the whole set of conjunction scenarios (for e.g.
# number of conjunctions among active satellites). The analytics should be intuitive
# and represented in an easily understandable format.

# In[14]:


import pandas as pd
pd.set_option('display.max_rows', None)
# Step 1: Data Retrieval and Exploration
data = pd.read_csv('sort-minRange.csv')
data.head()  # Display the first few rows to understand the data


# In[15]:


# Getting information of the check detaails like nullvalues, datatype, etc..
data.info()


# In[29]:


# Checking duplicated values
data.duplicated().value_counts()


# In[31]:


# Descriptive Analytics
total_conjunctions = len(data)
active_satellites_conjunctions = len(data)


# In[32]:


# General Analytics for a Single Day
average_range = data['TCA_RANGE'].mean()
max_probability = data['MAX_PROB'].max()


# In[33]:


# Display the analytics
print(f"Total Conjunctions: {total_conjunctions}")
print(f"active satellites conjunctions: {active_satellites_conjunctions}")
print(f"Average TCA Range: {average_range}")
print(f"Maximum Probability of Collision: {max_probability}")


# In[36]:


# Data Visualization

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Create a bar chart of Total Conjunctions
plt.subplot(2, 2, 1)
plt.bar(['Total Conjunctions'], [total_conjunctions])
plt.xlabel('Metric')
plt.ylabel('Count')
plt.title('Conjunction Analytics for a Single Day')

# Create a bar chart of Maximum Probability
plt.subplot(2, 2, 2)
plt.bar(['Max Probability'], [max_probability], color='green')
plt.ylabel('Probability')
plt.title('Maximum Probability of Collision')

# Create a pie chart of Conjunction Types
conjunction_types = data['DILUTION'].value_counts()
plt.subplot(2, 2, 3)
plt.pie(conjunction_types, labels=conjunction_types.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Conjunction Types')

# Create a scatter plot of TCA Range vs Relative Speed
plt.subplot(2, 2, 4)
plt.scatter(data['TCA_RANGE'], data['TCA_RELATIVE_SPEED'], color='red', alpha=0.5)
plt.xlabel('TCA Range')
plt.ylabel('TCA Relative Speed')
plt.title('TCA Range vs TCA Relative Speed')

plt.tight_layout()


# # 

# B) Represent the conjunctions data of a single satellite or a satellite constellation.
# The analytics should be intuitive, represented in an easily understandable format and
# should enable decision making from a satellite operator’s point of view.

# In[18]:


# Displaying all the unique 'OBJECT_NAME_1' to select the appropriate one
data["OBJECT_NAME_1"].value_counts()


# In[51]:


# Data Filtering
chosen_satellite = 'STARLINK-2466 [+]'  # Selecting single object in 'OBJECT_NAME_1'
chosen_data = data[data['OBJECT_NAME_1'] == chosen_satellite]
chosen_data


# In[52]:


# Descriptive Analytics
conjunctions_count = len(chosen_data)
conjunctions_count


# In[54]:


# Step 3: Data Visualization (for example, using a scatter plot)
plt.figure(figsize=(8, 6))
plt.scatter(chosen_data['TCA'], chosen_data['MAX_PROB'], c=chosen_data['MAX_PROB'], cmap='viridis', alpha=0.7)
plt.xlabel('TCA')
plt.ylabel('Maximum Probability')
plt.colorbar(label='Maximum Probability')
plt.xticks(rotation=15)
plt.title(f'Conjunctions for Satellite {chosen_satellite}')
plt.show()


# Decision-Making Insights
# insights based on the chosen satellite's conjunction.
# 
# Risk Assessment:
# Evaluate the risk levels for each conjunction based on parameters such as MAX_PROB and DILUTION.
# Categorize conjunctions into different risk levels (e.g., low risk, moderate risk, high risk) based on predefined thresholds.
# 
# Conjunction Details:
# Analyze parameters like TCA, TCA_RANGE, and TCA_RELATIVE_SPEED to assess the severity of the conjunction scenarios.
# Identify conjunctions with critical time of closest approach and relative speed.
# 
# Mitigation Strategies:
# Recommend specific mitigation strategies based on the assessed risk levels:
# 
#     Low Risk: Routine monitoring, no immediate action required.
#     Moderate Risk: Consider minor orbital adjustments.
#     High Risk: Implement significant orbital maneuvers to ensure safe clearance.
# 
# Alert Thresholds:
# Define clear alert thresholds for each risk level. These thresholds should trigger immediate notification to satellite operators and authorities.
# 
# Historical Trends:
# Analyze historical conjunction data to identify recurring patterns or trends. Use this information to inform decision-making for future conjunction scenarios.
# 
# Communication with Operators:
# Provide guidance on how to effectively communicate conjunction scenarios to satellite operators. Include recommended actions and expected response times.

# # 

# # Question 2
# Use the whole dataset that spans about five days. Derive analytics and visualise the
# data/analytics accounting for the evolution from the first day (for e.g. the number of
# conjunctions of the RSO having NORAD ID 12345 over 7 days of analysis)

# In[55]:


# Data Retrieval and Aggregation
dfs = []
for day in range(1, 6):
    df = pd.read_csv('sort-minRange.csv')
    dfs.append(df)


# In[56]:


# Combine dataframes
merged_data = pd.concat(dfs, ignore_index=True)
merged_data.head()


# In[57]:


#Displaying all the unique 'NORAD_CAT_ID_1' to select the appropriate one
data["NORAD_CAT_ID_1"].value_counts()


# In[58]:


# Data Filtering
norad_id = 36119     # Selecting specific 'NORAD_CAT_ID_1'
specific_data = merged_data[merged_data['NORAD_CAT_ID_1'] == norad_id]
specific_data


# In[59]:


# Descriptive Analytics
conjunction_count = len(specific_data)
conjunction_count


# In[63]:


def calculate_satellite_analytics(norad_id):
    specific_data = merged_data[merged_data['NORAD_CAT_ID_1'] == norad_id]
    return specific_data

norad_id = 36119 

# Data Visualization (for example, using a line plot)
plt.figure(figsize=(8, 6))
plt.plot(specific_data['TCA'], specific_data['MAX_PROB'], marker='*',markersize=10)
plt.xlabel('TCA')
plt.ylabel('Maximum Probability')
plt.title(f'Conjunctions for NORAD ID {norad_id} over 5 Days')
plt.xticks(rotation=20)
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




