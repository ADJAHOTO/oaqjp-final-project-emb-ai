"""
Server module for the Emotion Detector web application.
This module uses Flask to expose an API endpoint that analyzes
the emotions in a given text using the Watson NLP library.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotions in a text provided as a query parameter.

    Returns:
        str: A formatted string with the emotion scores and the
             dominant emotion, or an error message if the text is empty.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the main HTML index page of the application.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    