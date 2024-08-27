import streamlit as st
import pandas as pd
from pydub import AudioSegment
from io import BytesIO

# Title of the app
st.title("Burdah Memorization Helper")

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
df = load_lines('audio_lines.csv')

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
1. **Select start and end lines**: Choose the verses you want to memorize.
2. **Set repeat times**: Set how many times you'd like to repeat the selected verses.
3. **Play the audio**: Listen to the verses repeatedly to aid memorization.
""")

# Slider to select start and end lines
start_line = st.number_input("Select start line", min_value=1, max_value=len(df), value=1)
end_line = st.number_input("Select end line", min_value=start_line, max_value=len(df), value=start_line)

# Input for repeat times
repeat_times = st.number_input("Number of times to repeat the selection", min_value=1, max_value=100, value=1)

# Extract the selected lines from the audio
start_time = df.iloc[start_line - 1]['start_time'] * 1000  # Convert to milliseconds
end_time = df.iloc[end_line - 1]['end_time'] * 1000  # Convert to milliseconds
audio_clip = audio[start_time:end_time]

# Use concatenate instead of multiplying the audio clip
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