from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text = request.args.get("textToAnalyze", "").strip()
    result = emotion_detector(text)

    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant = result.get("dominant_emotion", "")

    response_html = ""
    if dominant == 'None':
        response_html = (
            "<!doctype html><html><head><meta charset='utf-8'><title>Emotion Result</title></head><body>"
            f"<p><strong>Invalid text! Please try again!</strong>.</p>"
            "</body></html>"
        )
    else:
        response_html = (
            "<!doctype html><html><head><meta charset='utf-8'><title>Emotion Result</title></head><body>"
            f"<p>For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is <strong>{dominant}</strong>.</p>"
            "</body></html>"
        )
    return response_html, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def generateTemplate():
    return render_template("index.html")

if __name__ == "__main__":
    # IMPORTANT: une seule app, toutes les routes définies AVANT run
    app.run(host="0.0.0.0", port=5000, debug=True)