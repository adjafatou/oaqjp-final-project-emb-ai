import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am so happy to do this!")
        print(result)  # Affiche les résultats pour diagnostiquer
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am really angry about this")
        print(result)  # Affiche les résultats pour diagnostiquer
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("I am feeling so sad")
        print(result)  # Affiche les résultats pour diagnostiquer
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am afraid of this situation")
        print(result)  # Affiche les résultats pour diagnostiquer
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_disgust(self):
        result = emotion_detector("This situation disgusts me")
        print(result)  # Affiche les résultats pour diagnostiquer
        self.assertEqual(result['dominant_emotion'], 'disgust')

if __name__ == "__main__":
    unittest.main()
