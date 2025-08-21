import streamlit as st
import pandas as pd
import urllib.parse

# Load your Excel file
file_path = "County-Key.xlsx"  # Make sure this is in the same folder as the script
df = pd.read_excel(file_path)
# Fix FIPS to always be 5 digits
df['County'] = df['County'].astype(str).str.zfill(5)

# Clean key just in case
df['Key'] = df['Key'].astype(str).str.strip()

st.set_page_config(page_title="County Dashboard Link Generator", page_icon="🌐")

# App title
st.title("🌐 County Sustainability Dashboard Link Generator 🌐")

# Step 1: Select State
states = sorted(df['State'].unique())
selected_state = st.selectbox("Select a State:", states)

# Step 2: Select County (filtered by state)
filtered_df = df[df['State'] == selected_state]
counties = filtered_df['County Name'].tolist()
selected_county = st.selectbox("Select a County:", counties)

# Step 3: Generate the link
if selected_county:
    county_row = filtered_df[filtered_df['County Name'] == selected_county].iloc[0]
    fips = county_row['County']
    key = county_row['Key'].strip()
    
    # URL-encode the key to handle spaces safely
    encoded_key = urllib.parse.quote(key)
    
    link = f"https://county-dashboard.uc.r.appspot.com/?county={fips}&key={encoded_key}"
    
    st.markdown("### 🔗 Generated Link:")
    st.code(link, language="text")
    
    # Move the link to a new line, with full key preserved
    st.markdown(f"\n[Click here to open the dashboard]({link})")


