import os
from flask import Flask, request, render_template, send_file
import openai
from gtts import gTTS
import uuid
import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip
import requests

# Set up the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a Flask app
app = Flask(__name__)

# Ensure the static directory exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    audio_file = None
    video_file = None
    error_message = None
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            
            # Text Generation
            try:
                chat_completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": user_input}
                    ]
                )
                response = chat_completion.choices[0].message.content.strip()
            except Exception as e:
                error_message = f"Error during text generation: {str(e)}"
                raise

            # Text-to-Speech
            try:
                tts = gTTS(text=response, lang='en')
                audio_filename = f"static/{uuid.uuid4().hex}.mp3"
                tts.save(audio_filename)
                audio_file = audio_filename
            except Exception as e:
                error_message = f"Error during text-to-speech conversion: {str(e)}"
                raise

            # Image Generation and Download
            image_filenames = []
            try:
                for i in range(5):
                    image_prompt = f"{response} - image {i+1}"
                    image_response = openai.Image.create(
                        prompt=image_prompt,
                        n=1,
                        size="512x512"
                    )
                    image_url = image_response['data'][0]['url']
                    image_data = requests.get(image_url).content
                    image_array = np.asarray(bytearray(image_data), dtype=np.uint8)
                    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                    image_filename = f"static/{uuid.uuid4().hex}.png"
                    cv2.imwrite(image_filename, image)
                    image_filenames.append(image_filename)
            except Exception as e:
                error_message = f"Error during image generation or download: {str(e)}"
                raise

            # Video Creation
            try:
                clip = ImageSequenceClip(image_filenames, fps=1)
                video_filename = f"static/{uuid.uuid4().hex}.mp4"
                clip.write_videofile(video_filename, codec='libx264')
                video_file = video_filename
            except Exception as e:
                error_message = f"Error during video creation: {str(e)}"
                raise

    except Exception as e:
        response = error_message or f"An unexpected error occurred: {str(e)}"

    return render_template("index.html", response=response, audio_file=audio_file, video_file=video_file, error_message=error_message)

# Route to serve the audio file
@app.route("/audio/<filename>")
def get_audio(filename):
    return send_file(f"static/{filename}", as_attachment=True)

# Route to serve the video file
@app.route("/video/<filename>")
def get_video(filename):
    return send_file(f"static/{filename}", as_attachment=True)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
