# Emotional Impact Analyzer for Movie Scripts

**Created by: Aryan Chavan**

An AI-powered tool that analyzes movie scripts and predicts their emotional impact on the human brain. This project uses Natural Language Processing (NLP) and Machine Learning to detect the primary emotion conveyed by a script and maps it to specific brain regions that would be activated.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
  - [1. Synthetic Dataset Generation](#1-synthetic-dataset-generation)
  - [2. Model Training](#2-model-training)
  - [3. Emotion Analysis Application](#3-emotion-analysis-application)
- [Emotion Categories](#emotion-categories)
- [Brain Region Mapping](#brain-region-mapping)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Web Application](#running-the-web-application)
  - [Generating a New Dataset](#generating-a-new-dataset)
  - [Retraining the Model](#retraining-the-model)
- [Technical Details](#technical-details)
  - [Dataset](#dataset)
  - [Text Vectorization](#text-vectorization)
  - [Machine Learning Model](#machine-learning-model)
  - [Streamlit App](#streamlit-app)
- [File Format Support](#file-format-support)
- [License](#license)

## Overview

The **Emotional Impact Analyzer** leverages machine learning to bridge the gap between storytelling and neuroscience. By analyzing the text of a movie script, it:

1. Detects the **primary emotion** (happy, sad, angry, fearful, surprised, disgusted)
2. Measures the **emotional intensity** on a scale of 0 to 1
3. Identifies which **brain regions** are most affected by the detected emotion
4. Provides a visual **brain activation chart** for the affected regions

## Features

- **Emotion Detection**: Classifies movie scripts into 6 emotion categories using a Multinomial Naive Bayes classifier
- **Intensity Scoring**: Estimates the emotional intensity based on script length and content
- **Brain Region Mapping**: Links each emotion to specific neuroanatomical regions
- **Interactive Dashboard**: Built with Streamlit for a user-friendly experience
- **Multi-format Support**: Accepts TXT, PDF, CSV, and DOCX file uploads
- **Downloadable Reports**: Export analysis results as text files
- **Example Script**: Built-in example to demonstrate functionality
- **Synthetic Training Data**: Automatically generated dataset for model training

## Project Structure

```
emotional_impact_analyzer/
│
├── emotional_impact_analyzer/
│   ├── app.py                     # Streamlit web application
│   ├── create_synthetic_dataset.py # Generates synthetic training data
│   └── train_model.py             # Trains the ML model
│
├── emotion_model.pkl              # Trained emotion classification model
├── vectorizer.pkl                 # TF-IDF vectorizer for text transformation
├── synthetic_movie_scripts.csv    # Generated synthetic dataset
├── README.md                      # Project documentation
```

## How It Works

### 1. Synthetic Dataset Generation

**File:** `emotional_impact_analyzer/create_synthetic_dataset.py`

Since real-world labeled movie script datasets are scarce, the project generates a **synthetic dataset** of 1,000 movie scripts. Each script is:

- Randomly assigned one of 6 emotions
- Constructed using the Faker library to generate realistic dialogue
- Injected with emotion-specific keywords (e.g., "joy", "laughter" for happy; "fear", "terror" for fearful)
- Annotated with intensity values and associated brain regions

This approach allows the model to learn patterns associated with different emotional tones in text.

### 2. Model Training

**File:** `emotional_impact_analyzer/train_model.py`

The training pipeline:

1. **Loads** the synthetic dataset from `synthetic_movie_scripts.csv`
2. **Splits** the data into training (80%) and testing (20%) sets
3. **Vectorizes** the text using **TF-IDF** (Term Frequency-Inverse Document Frequency) with:
   - Maximum 5,000 features
   - Unigram and bigram (n-gram range 1–2)
4. **Trains** a **Multinomial Naive Bayes** classifier
5. **Evaluates** the model using accuracy and classification report
6. **Saves** both the trained model and vectorizer as `.pkl` files for use in the application

### 3. Emotion Analysis Application

**File:** `emotional_impact_analyzer/app.py`

The Streamlit web application provides:

- **File Upload**: Users can upload movie scripts in TXT, PDF, CSV, or DOCX format
- **Emotion Analysis**: Processes the script through the trained ML model to predict the primary emotion
- **Intensity Calculation**: Computes emotional intensity based on the number of words (capped at 1.0 for scripts with 1,000+ words)
- **Brain Region Display**: Shows which regions of the brain are activated by the detected emotion
- **Bar Chart Visualization**: Displays activation levels for each brain region
- **Example Script**: A built-in coffee shop scene demonstrates the tool's capabilities
- **Download Functionality**: Analysis results can be exported as text files

## Emotion Categories

| Emotion    | Description                           |
|------------|---------------------------------------|
| Happy      | Joy, laughter, celebration, happiness |
| Sad        | Tears, sorrow, grief, melancholy      |
| Angry      | Rage, anger, fury, wrath              |
| Fearful    | Fear, terror, horror, panic           |
| Surprised  | Shock, amazement, astonishment, wonder|
| Disgusted  | Disgust, repulsion, loathing, revulsion|

## Brain Region Mapping

Each detected emotion is mapped to brain regions based on neuroscientific research:

| Emotion    | Brain Regions Activated              | Region Function                                    |
|------------|--------------------------------------|----------------------------------------------------|
| Happy      | Prefrontal Cortex, Ventral Striatum  | Decision making, reward processing, motivation     |
| Sad        | Amygdala, Hippocampus                | Emotion processing, memory formation, regulation   |
| Angry      | Amygdala, Prefrontal Cortex          | Emotion processing, decision making                |
| Fearful    | Amygdala, Insula                     | Fear processing, body awareness, emotion processing|
| Surprised  | Prefrontal Cortex, Parietal Cortex   | Decision making, sensory processing, spatial awareness|
| Disgusted  | Insula, Prefrontal Cortex            | Disgust processing, body awareness, decision making|

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone or download the repository**

2. **Navigate to the project directory**

   ```bash
   cd emotional_impact_analyzer
   ```

3. **Install the required dependencies**

   ```bash
   pip install pipenv  # if not already installed
   pip install streamlit pandas numpy scikit-learn joblib pillow faker PyPDF2 python-docx
   ```

   Or create a `requirements.txt` file:

   ```
   streamlit
   pandas
   numpy
   scikit-learn
   joblib
   pillow
   faker
   PyPDF2
   python-docx
   base64
   ```

   Then install with:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

```bash
streamlit run emotional_impact_analyzer/app.py
```

1. Open the URL shown in the terminal (typically `http://localhost:8501`)
2. Upload a script file (TXT, PDF, CSV, DOCX) or try the built-in example
3. Click **"Analyze Emotional Impact"** to see results
4. View the detected emotion, intensity score, affected brain regions, and activation chart
5. Download the analysis report using the download button

### Generating a New Dataset

```bash
python emotional_impact_analyzer/create_synthetic_dataset.py
```

This will create a new `synthetic_movie_scripts.csv` file with 1,000 synthetic scripts.

### Retraining the Model

```bash
python emotional_impact_analyzer/train_model.py
```

This will:
- Load the dataset
- Train a new Multinomial Naive Bayes model
- Display accuracy metrics
- Save the updated `emotion_model.pkl` and `vectorizer.pkl` files

## Technical Details

### Dataset

- **Size**: 1,000 synthetic movie scripts
- **Features**: `script_id`, `emotion`, `script`, `intensity`, `brain_regions`, `length`
- **Generation**: Uses the Faker library to create realistic dialogue with emotion-specific keywords

### Text Vectorization

- **Method**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Max Features**: 5,000
- **N-gram Range**: 1 to 2 (single words and two-word phrases)

### Machine Learning Model

- **Algorithm**: Multinomial Naive Bayes
- **Task**: Multi-class text classification (6 emotion categories)
- **Training/Test Split**: 80% / 20%
- **Output**: Predicted emotion label

### Streamlit App

- **Framework**: Streamlit (Python web framework)
- **Features**:
  - File upload with 4 format types
  - Interactive emotion analysis
  - Brain activation bar chart
  - Downloadable reports in TXT format
  - Sidebar with example script

## File Format Support

| Format | Extension | Library Used    |
|--------|-----------|-----------------|
| Text   | `.txt`    | Built-in (utf-8)|
| PDF    | `.pdf`    | PyPDF2          |
| CSV    | `.csv`    | Pandas          |
| Word   | `.docx`   | python-docx     |

## License

This project is open-source. Feel free to modify and distribute it as needed.

---

*Built with Python, Streamlit, and Scikit-learn by Aryan Chavan*