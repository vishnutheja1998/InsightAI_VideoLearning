# InsightAI - Interactive Learning Platform

**InsightAI** is an innovative, AI-powered online learning platform that enables users to explore any topic of their choice. Leveraging the powerful ChatGPT API, InsightAI automatically generates detailed scripts and engaging video content based on the user’s input topic. This repository contains the core files to run InsightAI’s web application, allowing for an interactive learning experience that combines AI-driven scripting and video creation.

### Demo Video
[Watch the InsightAI Demo on YouTube](https://youtu.be/UjxwArLXS2w)

### Screeenshot of INSIGHTAI Before and After Running:
BEFORE EXECUTING: Executed with the content "Types of Dogs" in the Search box of below image.
<img width="1508" alt="Screenshot 2024-10-25 at 8 52 47 PM" src="https://github.com/user-attachments/assets/f1c29d51-e417-4fe5-a99a-b5f77b1125a5">
AFTER EXECUTING:
<img width="1495" alt="image" src="https://github.com/user-attachments/assets/4a932e6c-99d7-472a-9cd2-31eded45f35a">

---

## Features
- **AI-Powered Topic Generation:** Users can input any topic of interest, and InsightAI generates an informative, accurate script.
- **Audio and Video Learning:** InsightAI converts the generated script into audio using TTS (Text-to-Speech) and produces a dynamic video with relevant visuals to reinforce learning.
- **User-Friendly Interface:** The web UI allows for easy input, with intuitive playback controls for audio and video learning.

---

## Getting Started

### Prerequisites
To run InsightAI locally, ensure you have the following installed:
- Python 3.7+
- Flask
- OpenAI API (API key required)
- gTTS (Google Text-to-Speech)
- moviepy
- requests
- numpy, cv2 (OpenCV)

### INSTALLATIONS

1. **Clone this repository**:
   ```bash
   git clone https://github.com/vishnutheja1998/InsightAI_VideoLearning.git
   cd insightai

2. **Install dependencies**:
    ```bash
    pip install Flask openai gTTS moviepy requests numpy opencv-python

3. **Set up OpenAI API key**: Obtain your API key from OpenAI and set it in your environment variables:
    ```bash
    export OPENAI_API_KEY='your-api-key'

### USAGE

1. **Run the application**:
   ```bash
   python Insight_App.py

 2. **Accessing the applicaiton**:
    Access the web interface: Open your browser and go to http://127.0.0.1:5000. Enter a topic of choice, and InsightAI will generate a response along with audio and video content.


### Project Files
1. Insight_App.py: The main application file containing the Flask app and logic for text generation, TTS, image generation, and video creation.
2. index.html: The HTML template for the user interface, allowing topic input, error feedback, and playback of audio and video outputs.

