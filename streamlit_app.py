import streamlit as st
import pandas as pd
from pydub import AudioSegment
from io import BytesIO

# Title of the app
st.title("Burdah Memorization Helper - Changes")

# Information about the Burdah poem and the app's purpose
st.subheader("About This App")
st.write("""
This app is designed to assist students in memorizing the famous **Qasidah Burdah**, a revered poem composed by **Imam al-Busiri** in praise of the Prophet Muhammad (peace be upon him). 
It is widely regarded as one of the greatest Arabic poems, known for its deep spiritual significance. This app lets you select and repeat specific verses to help you memorize effectively.
""")

# Cache the loading of audio file to avoid reloading on each interaction
@st.cache_data
def load_audio(path):
    return AudioSegment.from_mp3(path)

# Cache the loading of CSV to avoid reloading on each interaction
@st.cache_data
def load_lines(csv_path):
    return pd.read_csv(csv_path)

# Load the audio and CSV file with preprocessed lines
audio_path = 'burdah.mp3'  # Modify this to the correct path
audio = load_audio(audio_path)
df = load_lines('Burdah_Lines - Sheet3.csv')

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
1. **Select chapter and line range**: Choose the chapter and verses you want to memorize.
2. **Set repeat times**: Set how many times you'd like to repeat the selected verses.
3. **Play the audio**: Listen to the verses repeatedly to aid memorization.
""")

# Create a new column for displaying chapter and line together in a more user-friendly way


df['Chapter_Line'] = df.apply(lambda row: f"Chapter {int(row['Chapter'])} - Line {int(row['Line Number'])}", axis=1)

df['Line Number'] = df['Line Number'].astype(int)# Dropdown to select start line based on chapter and line number
start_selection = st.selectbox("Select Start Line", df['Chapter_Line'].tolist())


# Get the index of the selected start line
start_index = df[df['Chapter_Line'] == start_selection].index[0]

# Dropdown to select end line based on the selected start line's index
end_selection = st.selectbox("Select End Line", df[df.index >= start_index]['Chapter_Line'].tolist())

# Get start and end line information from the selection
start_line_data = df[df['Chapter_Line'] == start_selection].iloc[0]
end_line_data = df[df['Chapter_Line'] == end_selection].iloc[0]

# Input for repeat times
repeat_times = st.number_input("Number of times to repeat the selection", min_value=1, max_value=100, value=1)

# Extract the start and end times for the selected lines
start_time = start_line_data['Start Time'] * 1000  # Convert to milliseconds
end_time = end_line_data['End Time'] * 1000  # Convert to milliseconds

# Extract the selected clip from the audio
audio_clip = audio[start_time:end_time]

# Repeat the audio clip the specified number of times
repeated_clip = AudioSegment.silent(duration=0)
for _ in range(repeat_times):
    repeated_clip += audio_clip

# Save the repeated clip to a byte stream
output_buffer = BytesIO()
repeated_clip.export(output_buffer, format="mp3")

# Display the play button for the repeated clip
st.audio(output_buffer.getvalue())

# Footer section with additional resources
st.markdown("""
---
**Additional Resources:**

- [Read the full Burdah Poem](https://sunnah.org/2019/09/15/qasidat-al-burdah/)
- [Learn more about Imam al-Busiri](https://www.islamicfinder.org/biography/imam-busiri/)
- [Memorization Tips](https://productivemuslim.com/10-tips-memorize-quran/)
---
""")

st.subheader("Admin Section: Edit CSV Data")
password = st.text_input("Enter Admin Password", type="password")

# Define the correct password
correct_password = "qalam25"  # Change this to your actual password

if password == correct_password:
    st.success("Access granted! You can now edit the CSV data.")
    
    # Allow the user to edit the DataFrame directly
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    # Button to save changes to CSV
    if st.button("Save Changes"):
        edited_df.to_csv('Burdah_Lines - Sheet3.csv', index=False)
        st.write("CSV updated successfully!")
else:
    if password:
        st.error("Incorrect password!")
