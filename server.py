 Executing this file initiates the emotion detector over the Flask 
    channel and deployed on localhost:5000.
''''''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector. The output returned shows the confidence
        score for each of the 5 emotions and the dominanat emotion.
    '''
    txt = request.args.get('textToAnalyze')
    rsp = emotion_detector(txt)
    if rsp['dominant_emotion']:
        return "For the given statement, the system response is " + \
            f"'anger': {rsp['anger']}, " + \
            f"'disgust': {rsp['disgust']}, " + \
            f"'fear': {rsp['fear']}, " + \
            f"'joy': {rsp['joy']} and " + \
            f"'sadness': {rsp['sadness']}. " + \
            f"The dominant emotion is <b>{rsp['dominant_emotion']}</b>."

    # Return for the error case
    return "<b>Invalid text! Please try again!</b>"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #  This functions executes the flask app and deploys it on localhost:5000
    app.run(debug=True, port=5000)
