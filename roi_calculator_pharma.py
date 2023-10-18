import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random

# Hardcoded sample data
sample_data = {
    "Quarters": ["Y1Q1", "Y1Q2", "Y1Q3", "Y1Q4", "Y2Q1"],
    "Submissions": [100, 180, 150, 275, 370],
    "Approvals": [50, 98, 90, 128, 185],
    "Competitor_Approvals": [65, 90, 78, 100, 128]
}

# Streamlit interface
st.title('Prior Authorizations Analytics')

# Extracting data
quarters = sample_data["Quarters"]
submissions = sample_data["Submissions"]
approvals = sample_data["Approvals"]
competitor_approvals = sample_data["Competitor_Approvals"]

# Creating the graph
fig, ax = plt.subplots()
ax.plot(quarters, submissions, label='Submissions', marker='o')
ax.plot(quarters, approvals, label='Approvals', marker='o')
ax.plot(quarters, competitor_approvals, label='Competitor Approvals', marker='o')

ax.set_xlabel('Quarters')
ax.set_ylabel('# of Prior Authorizations')
ax.set_title('Prior Authorizations over Quarters')
ax.legend()
ax.set_xticklabels(quarters, rotation=45)  # Rotate quarter labels for better visibility

# Displaying the graph in Streamlit
st.pyplot(fig)



# Hardcoded data for the Provider Analytics table
provider_analytics_data = {
    "Top Submitters": ["Amelia Thompson", "Samuel Robinson", "Olivia Martinez"],
    "Top Denials": ["Benjamin Clark", "Sophia Johnson", "Mason Williams"],
    "Top Competing Submitters": ["Ava Lewis", "Liam Wilson", "Isabella Davis"]
}

# Creating a DataFrame from the hardcoded data
df_provider_analytics = pd.DataFrame(provider_analytics_data)

# Setting the index of the DataFrame to start from 1
df_provider_analytics.index = df_provider_analytics.index + 1

# Streamlit interface for displaying the table
st.title('Provider Analytics')
st.table(df_provider_analytics)
