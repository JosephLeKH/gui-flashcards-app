# Flashcards GUI App

This is a simple flashcards application built with Python using the `Tkinter` library for the graphical interface and `Pandas` for data handling. The app is designed to help users learn new information in a fun and interactive way by flipping flashcards with paired information from a CSV file.

---

## Features
- **Interactive Flashcards**: Flip cards to reveal translations or other paired information.
- **Customizable Content**: Replace the default CSV file to use the app for different learning purposes.
- **Progress Tracking**: Correctly answered cards are removed from the deck and saved in a separate file.

---

## Screenshots
### Front Card:
![Front Card](images/screenshot_main.png)

### Back Card:
![Back Card](images/screenshot_main.png)


---

## Purpose
The app demonstrates how to:
1. Build a graphical user interface (GUI) with Tkinter.
2. Use Pandas to manage data from CSV files.
3. Randomly display and update flashcards dynamically.

By default, this app includes an example CSV file (`data/french_words.csv`) containing English-to-French translations to help users learn French vocabulary. However, you can replace this file with your own data to use the flashcards for different purposes, such as:
- Learning new languages
- Memorizing historical dates
- Preparing for exams
- And more!

---

## How to Use

### Prerequisites
Ensure you have Python installed with the following libraries:
- `tkinter` (built-in with Python)
- `pandas`

### Running the App
1. Clone or download this repository.
2. Navigate to the project folder in your terminal.
3. Run the app using:
   ```bash
   python flashcards.py
   ```
4. The app will launch a GUI with flashcards. 

### Interacting with Flashcards
- **Start**: Click the buttons to begin.
- **Correct**: Click the ✅ button if you remember the translation.
- **Incorrect**: Click the ❌ button to try again later.

---

## Customizing the Flashcards

### Replacing the Default Dataset
1. Prepare your dataset in CSV format with two columns (e.g., `Front` and `Back`).
   - Example (English-to-Spanish):
     ```csv
     English,Spanish
     Apple,Manzana
     Hello,Hola
     ```
2. Save your file as `data/<your_file>.csv`.
3. Update the app to load your CSV file by replacing `"data/french_words.csv"` in the code.

---

## Acknowledgments
- **Icons**: The icons for correct and incorrect answers are sourced from [Flaticon](https://www.flaticon.com/).
- **Images**: Flashcard backgrounds are provided in the `images` folder.

Happy Learning!
