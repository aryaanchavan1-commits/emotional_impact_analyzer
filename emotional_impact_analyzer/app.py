import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from PIL import Image
import base64

# Load the trained model and vectorizer
model = joblib.load('emotion_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Define brain regions for each emotion
BRAIN_REGIONS = {
    'happy': ['prefrontal_cortex', 'ventral_striatum'],
    'sad': ['amygdala', 'hippocampus'],
    'angry': ['amygdala', 'prefrontal_cortex'],
    'fearful': ['amygdala', 'insula'],
    'surprised': ['prefrontal_cortex', 'parietal_cortex'],
    'disgusted': ['insula', 'prefrontal_cortex']
}

# Define brain region descriptions
BRAIN_DESCRIPTIONS = {
    'prefrontal_cortex': 'Responsible for decision making, personality expression, and moderating social behavior',
    'ventral_striatum': 'Involved in reward processing and motivation',
    'amygdala': 'Processes emotions like fear and pleasure',
    'hippocampus': 'Important for memory formation and emotional regulation',
    'insula': 'Processes emotions and body awareness',
    'parietal_cortex': 'Processes sensory information and spatial awareness'
}

def analyze_emotional_impact(script):
    """Analyze the emotional impact of a movie script"""
    # Vectorize the script
    script_vec = vectorizer.transform([script])
    
    # Predict the emotion
    emotion = model.predict(script_vec)[0]
    
    # Get intensity (simulated based on script length)
    intensity = min(1.0, len(script.split()) / 1000)
    
    # Get brain regions
    brain_regions = BRAIN_REGIONS[emotion]
    
    return {
        'emotion': emotion,
        'intensity': intensity,
        'brain_regions': brain_regions
    }

def create_brain_activation_chart(brain_regions):
    """Create a brain activation chart"""
    chart_data = {
        'Brain Region': [],
        'Activation Level': [],
        'Description': []
    }
    
    for region in brain_regions:
        chart_data['Brain Region'].append(region)
        chart_data['Activation Level'].append(np.random.uniform(0.7, 1.0))
        chart_data['Description'].append(BRAIN_DESCRIPTIONS[region])
    
    return pd.DataFrame(chart_data)

def get_file_content_as_string(path):
    """Read file content as string"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def download_button(object_to_download, download_filename, button_text):
    """Create a download button for the given object"""
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    
    b64 = base64.b64encode(object_to_download.encode()).decode()
    button = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{button_text}</a>'
    st.markdown(button, unsafe_allow_html=True)

def main():
    st.title("Emotional Impact Analyzer for Movie Scripts")
    st.markdown("""
    Upload your movie script and get insights into its emotional impact and how it affects the human brain.
    """)
    
    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "csv", "docx"])
    
    if uploaded_file is not None:
        # Read the file content
        if uploaded_file.name.endswith('.pdf'):
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            script = ""
            for page in reader.pages:
                script += page.extract_text()
        elif uploaded_file.name.endswith('.docx'):
            from docx import Document
            doc = Document(uploaded_file)
            script = "\n".join([para.text for para in doc.paragraphs])
        elif uploaded_file.name.endswith('.csv'):
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            script = " ".join(df['script'].tolist())
        else:  # txt file
            script = uploaded_file.read().decode('utf-8')
        
        # Analyze the script
        if st.button("Analyze Emotional Impact"):
            result = analyze_emotional_impact(script)
            
            # Display results
            st.success("Emotional Impact Analysis Complete!")
            
            st.subheader("Primary Emotion Detected")
            st.write(f"**{result['emotion'].capitalize()}** (Intensity: {result['intensity']:.2f})")
            
            st.subheader("Brain Regions Affected")
            for region in result['brain_regions']:
                st.write(f"- **{region.replace('_', ' ').capitalize()}**: {BRAIN_DESCRIPTIONS[region]}")
            
            st.subheader("Brain Activation Chart")
            chart_data = create_brain_activation_chart(result['brain_regions'])
            st.bar_chart(chart_data[['Brain Region', 'Activation Level']])
            
            st.subheader("Detailed Analysis")
            analysis = f"""
            Your movie script primarily evokes **{result['emotion']}** emotions. 
            The intensity of this emotional impact is **{result['intensity']:.2f}** on a scale of 0 to 1.
            
            This emotional pattern activates the following brain regions:
            """
            for region in result['brain_regions']:
                analysis += f"\n- **{region.replace('_', ' ').capitalize()}**: {BRAIN_DESCRIPTIONS[region]}"
            
            st.write(analysis)
            
            # Download results
            st.subheader("Download Results")
            download_button(analysis, "emotional_impact_analysis.txt", "Download Analysis")
    
    # Example script
    st.sidebar.title("Try an Example")
    if st.sidebar.button("Load Example Script"):
        example_script = """
        INT. COFFEE SHOP - DAY
        
        JANE sits at a table, nervously stirring her coffee. Her hands tremble slightly.
        
        JOHN enters, spots Jane, and approaches with a warm smile.
        
        JOHN
        Hey, you made it.
        
        JANE
        (forcing a smile)
        Yeah, I... I wanted to talk.
        
        The tension is palpable as they sit in awkward silence.
        """
        st.sidebar.text_area("Example Script", value=example_script, height=200)
        if st.sidebar.button("Analyze Example"):
            result = analyze_emotional_impact(example_script)
            st.sidebar.success(f"Detected emotion: {result['emotion']}")

if __name__ == "__main__":
    main()