"""Flask application for emotion detection.

This Flask application provides an endpoint for processing user input and
detecting emotions using the EmotionDetection module. It renders the
home page (`index.html`) and handles POST requests to the `/emotionDetector`
endpoint.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detection  # Corrected import

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page template (index.html)."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """Processes user input, detects emotions using emotion_detection,
    and returns the analyzed results as JSON.
    
    Returns:
        JSON: 
            - anger: Detected anger score (None if not detected)
            - disgust: Detected disgust score (None if not detected)
            - fear: Detected fear score (None if not detected)
            - joy: Detected joy score (None if not detected)
            - sadness: Detected sadness score (None if not detected)
            - dominant_emotion: The emotion with the highest score
            - error (optional): Error message if statement is invalid
    """
    statement = request.form['statement']

    if not statement.strip():
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': "Texte invalide ! Veuillez réessayer !"
        })

    result = emotion_detection.emotion_detector(statement)

    if result.get('dominant_emotion') is None:
        return jsonify({
            'error': "Texte invalide ! Veuillez réessayer !"
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
