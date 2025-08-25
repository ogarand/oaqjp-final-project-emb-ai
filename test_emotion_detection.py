import unittest
from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("dominant_emotion"), "joy")

    def test_anger(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result.get("dominant_emotion"), "anger")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result.get("dominant_emotion"), "disgust")

    def test_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result.get("dominant_emotion"), "sadness")

    def test_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result.get("dominant_emotion"), "fear")

    # Test optionnel : validation d’entrée
    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            emotion_detector("")


if __name__ == "__main__":
    unittest.main()