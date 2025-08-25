"""
Final project web server Flask app
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Detect emotion from the 'textToAnalyze' query parameter.

    Returns:
        tuple[str, int, dict[str, str]]: HTML content, status code, headers.
    """
    text = request.args.get("textToAnalyze", "").strip()
    if not text:
        html = (
            "<!doctype html><html><head><meta charset='utf-8'><title>Emotion Result</title></head>"
            "<body><p><strong>Invalid text! Please try again!</strong></p></body></html>"
        )
        return html, 200, {"Content-Type": "text/html; charset=utf-8"}

    try:
        result = detect_emotion(text)
    except Exception as exc:  # pylint: disable=broad-except
        html = (
            "<!doctype html><html><head><meta charset='utf-8'><title>Error</title></head>"
            f"<body><p><strong>Error processing request:</strong> {exc}</p></body></html>"
        )
        return html, 500, {"Content-Type": "text/html; charset=utf-8"}

    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant = result.get("dominant_emotion", "")

    if dominant in (None, "", "None"):
        html = (
            "<!doctype html><html><head><meta charset='utf-8'><title>Emotion Result</title></head>"
            "<body><p><strong>Invalid text! Please try again!</strong></p></body></html>"
        )
        status = 200
    else:
        html = (
            "<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>Emotion Result</title></head><body>"
            f"<p>For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is <strong>{dominant}</strong>.</p></body></html>"
        )
        status = 200

    return html, status, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def generate_template():
    """
    Render index template.
    """
    return render_template("index.html")

def main():
    """Run development server."""
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    main()
