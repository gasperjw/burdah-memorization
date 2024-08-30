# Burdah Memorization Helper

## Overview

The **Burdah Memorization Helper** is a web application designed to assist students in memorizing the famous **Qasidah Burdah**, a revered poem composed by **Imam al-Busiri** in praise of the Prophet Muhammad (peace be upon him). This app allows you to select specific verses, set the number of repetitions, and listen to them on repeat to facilitate effective memorization.

## Features

- **Chapter and Verse Selection**: Choose the specific chapter and verses you want to focus on for memorization.
- **Repeat Functionality**: Set the number of times you want the selected verses to repeat.
- **Audio Playback**: Listen to the selected verses on loop to enhance memorization.

## How to Use

1. **Select Chapter and Line Range**: Use the dropdown menus to choose the starting and ending lines from the selected chapter.
2. **Set Repeat Times**: Specify how many times you'd like the selected verses to repeat.
3. **Play the Audio**: Click the play button to listen to the repeated verses and start memorizing.

## Installation

To run this app locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/burdah-memorization-helper.git
   cd burdah-memorization-helper
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## File Structure

- **`streamlit_app.py`**: Main application file containing the Streamlit app.
- **`burdah.mp3`**: Audio file of the Burdah poem (ensure this file is placed in the correct path).
- **`Burdah_Lines - Sheet3.csv`**: CSV file containing preprocessed lines with start and end times for each verse.

## Additional Resources

- [Read the full Burdah Poem](https://sunnah.org/2019/09/15/qasidat-al-burdah/)
- [Learn more about Imam al-Busiri](https://www.islamicfinder.org/biography/imam-busiri/)
- [Memorization Tips](https://productivemuslim.com/10-tips-memorize-quran/)

## Contributing

If you'd like to contribute to the development of this app, feel free to fork the repository and submit a pull request.

---

**Note**: This app is a tool to aid in memorization and should be used as a complement to your regular study and practice.
