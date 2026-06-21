"""Flask server for the Emotion Detector application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Analyze the text provided and return the formatted emotion output."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the main landing page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)