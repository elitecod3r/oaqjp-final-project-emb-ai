import requests  
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    response_dict = json.loads(response.text)

    # set default values in case of error
    anger_score = None 
    disgust_score = None 
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None

    if response.status_code == 200: 
        response_dict = json.loads(response.text)
        emotion_dict = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust'] 
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']
        max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

        if max_score == anger_score:
            dominant_emotion = 'anger'
        elif max_score == disgust_score: 
            dominant_emotion = 'disgust'
        elif max_score == fear_score: 
            dominant_emotion = 'fear'          
        elif max_score == joy_score: 
            dominant_emotion = 'joy'
        else:
            dominant_emotion = 'sadness'

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion,
    }
