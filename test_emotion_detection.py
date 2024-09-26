from EmotionDetection.emotion_detection import emotion_detector
import unittest 


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        resp = emotion_detector('I am glad this happened')
        self.assertEqual(resp['dominant_emotion'], 'joy')
        
        resp = emotion_detector('I am really mad about this')
        self.assertEqual(resp['dominant_emotion'], 'anger')

        resp = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(resp['dominant_emotion'], 'disgust')
 
        resp = emotion_detector('I am so sad about this')
        self.assertEqual(resp['dominant_emotion'], 'sadness')

        resp = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(resp['dominant_emotion'], 'fear')


unittest.main()