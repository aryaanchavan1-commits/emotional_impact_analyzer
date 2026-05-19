import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Define emotions and their characteristics
EMOTIONS = {
    'happy': {'intensity_range': (0.7, 1.0), 'brain_regions': ['prefrontal_cortex', 'ventral_striatum']},
    'sad': {'intensity_range': (0.6, 0.9), 'brain_regions': ['amygdala', 'hippocampus']},
    'angry': {'intensity_range': (0.8, 1.0), 'brain_regions': ['amygdala', 'prefrontal_cortex']},
    'fearful': {'intensity_range': (0.7, 1.0), 'brain_regions': ['amygdala', 'insula']},
    'surprised': {'intensity_range': (0.5, 0.8), 'brain_regions': ['prefrontal_cortex', 'parietal_cortex']},
    'disgusted': {'intensity_range': (0.6, 0.9), 'brain_regions': ['insula', 'prefrontal_cortex']}
}

def generate_script(emotion, length=100):
    """Generate a synthetic movie script with the given emotion"""
    script = []
    for _ in range(length):
        # Generate random dialogue with emotional words
        dialogue = fake.sentence()
        # Add emotional words based on the emotion
        if emotion == 'happy':
            dialogue += " " + random.choice(["joy", "laughter", "celebration", "happiness"])
        elif emotion == 'sad':
            dialogue += " " + random.choice(["tears", "sorrow", "grief", "melancholy"])
        elif emotion == 'angry':
            dialogue += " " + random.choice(["rage", "anger", "fury", "wrath"])
        elif emotion == 'fearful':
            dialogue += " " + random.choice(["fear", "terror", "horror", "panic"])
        elif emotion == 'surprised':
            dialogue += " " + random.choice(["shock", "amazement", "astonishment", "wonder"])
        elif emotion == 'disgusted':
            dialogue += " " + random.choice(["disgust", "repulsion", "loathing", "revulsion"])
        script.append(dialogue)
    return " ".join(script)

def create_synthetic_dataset(num_scripts=1000):
    """Create a synthetic dataset of movie scripts with emotional labels"""
    data = []
    for i in range(num_scripts):
        emotion = random.choice(list(EMOTIONS.keys()))
        script = generate_script(emotion)
        intensity = np.random.uniform(*EMOTIONS[emotion]['intensity_range'])
        brain_regions = EMOTIONS[emotion]['brain_regions']
        
        data.append({
            'script_id': i,
            'emotion': emotion,
            'script': script,
            'intensity': intensity,
            'brain_regions': ",".join(brain_regions),
            'length': len(script.split())
        })
    
    df = pd.DataFrame(data)
    df.to_csv('synthetic_movie_scripts.csv', index=False)
    print(f"Created dataset with {num_scripts} synthetic movie scripts")

if __name__ == "__main__":
    create_synthetic_dataset()